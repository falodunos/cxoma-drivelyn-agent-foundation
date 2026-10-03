#!/usr/bin/env python3
"""Offline observe-only maintenance primitives. No external writes or source rewrites."""
import argparse
import hashlib
import json
import posixpath
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent

def fingerprint(kind, repo, rule, path=''):
    # Hash metadata; never expose external log content or credentials as identifiers.
    value = json.dumps([kind, repo, rule, path], separators=(',', ':'))
    return kind + ':' + hashlib.sha256(value.encode()).hexdigest()[:24]

def finding(kind, repo, rule, path, classification, evidence, scope, identity=None):
    return {'fingerprint': fingerprint(kind, repo, rule, path if identity is None else identity), 'classification': classification,
            'rule': rule, 'path': path, 'evidence': evidence, 'scope': scope,
            'status': 'PROPOSED_FINDING', 'mutation_performed': False}

def deduplicate(findings, known):
    existing = {item['fingerprint']: item for item in known}
    for item in findings:
        previous = existing.get(item['fingerprint'])
        if previous:
            item['status'] = 'KNOWN_UNRESOLVED' if previous.get('state') == 'open' else 'REVIEW_CLOSED_EQUIVALENT'
            item['issue_reference'] = previous.get('issue_reference')
        else:
            item['duplicate_search'] = 'UNAVAILABLE: live open/closed issue search required before creation'
    return findings

def documentation(root):
    findings = []
    paths = [root/'README.md',root/'AGENTS.md',root/'ARCHITECTURE.md',*(root/'docs').rglob('*.md')]
    for file in paths:
        if not file.is_file(): continue
        rel = str(file.relative_to(root))
        for target in re.findall(r'\]\(([^)]+)\)',file.read_text()):
            target = target.strip('<>').split('#',1)[0]
            if not target or re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:',target): continue
            resolved = (file.parent/target).resolve()
            if not resolved.is_relative_to(root.resolve()) or not resolved.exists():
                findings.append(finding('docs-drift',root.name,'broken-local-link',rel,'DOCUMENTATION_DRIFT',
                    {'target':target},'Restore or correct the local instruction/document link', identity=rel+':'+posixpath.normpath(target)))
    mapping = root/'config/docs-freshness.json'
    if mapping.exists():
        for rule in json.loads(mapping.read_text()).get('rules',[]):
            claim = root/rule['claim_path']; source = root/rule['source_path']
            if not claim.is_file() or not source.is_file():
                findings.append(finding('docs-drift',root.name,rule['id'],rule['claim_path'],'DOCUMENTATION_DRIFT',
                    {'source':rule['source_path'],'reason':'mapped source/claim missing'},'Restore source mapping or documentation'))
            elif re.search(rule['claim_pattern'],claim.read_text(),re.M) and not re.search(rule['source_pattern'],source.read_text(),re.M):
                findings.append(finding('docs-drift',root.name,rule['id'],rule['claim_path'],'DOCUMENTATION_DRIFT',
                    {'source':rule['source_path'],'reason':'claim no longer supported by mapped source'},rule['scope']))
    return findings

def eligible_lesson(item):
    return (item.get('repository_wide') is True and item.get('durable') is True and
        item.get('repeatedly_useful') is True and item.get('mechanically_enforced') is False and
        item.get('better_in_deep_docs') is False and isinstance(item.get('proposal'),str) and
        0 < len(item['proposal']) <= 280 and len(set(item.get('evidence',[]))) >= 2 and
        item.get('source_type') in {'completed-plan','recurring-review','recurring-ci','stable-command','durable-constraint','repeated-mistake','canonical-skill'})

def agents_proposals(root, evidence):
    return [finding('agents',root.name,'durable-lesson',item['proposal'],'HARNESS_DRIFT',
        {'sources':item['evidence'],'shared':item.get('shared',False)},
        'Propose foundation release first' if item.get('shared') else 'Propose concise local instruction change')
        | {'proposal':item['proposal'],'requires_review':['documentation','architecture if engineering behavior changes']}
        for item in evidence if eligible_lesson(item)]

CI_RULES = [
 ('PERMISSION/SECRET',r'permission denied|resource not accessible|bad credentials|secret.*(?:missing|unavailable)|403 forbidden'),
 ('INFRASTRUCTURE_TRANSIENT',r'runner.*(?:lost|offline)|service unavailable|502 bad gateway|network.*timed out|connection reset'),
 ('TOOLCHAIN_SETUP',r'failed to find package|sdk.*not found|java.*not found|unsupported class file|incompatible.*kotlin'),
 ('DEPENDENCY_RESOLUTION',r'could not resolve|could not find.*(?:artifact|dependency)|could not transfer artifact'),
 ('ARCHITECTURE_CHECK',r'architecture.*(?:violation|failed)|archunit.*(?:failure|violation)'),
 ('STATIC_ANALYSIS',r'(?:spotless|detekt|lint).*(?:failed|violation)|formatting violations'),
 ('TEST_FAILURE',r'tests run:.*(?:failures: [1-9]|errors: [1-9])|(?:test|assertion).*(?:failed|failure)|assertionerror'),
 ('CI_CONFIGURATION',r'invalid workflow|unrecognized named-value|unexpected value.*workflow')]

def classify_ci(log):
    for number,line in enumerate(log.splitlines(),1):
        for category,pattern in CI_RULES:
            if re.search(pattern,line,re.I): return category,number
    return 'UNKNOWN',None

def ci_report(root, log, workflow, step):
    category,line = classify_ci(log)
    result = finding('ci',root.name,category,workflow+':'+step,'RELIABILITY',
        {'workflow':workflow,'normalized_step':step,'first_material_line':line,'failure_class':category},
        'Investigate first material failure; reproduce locally before bounded repair')
    result['repair_candidate'] = category not in {'UNKNOWN','INFRASTRUCTURE_TRANSIENT','PERMISSION/SECRET'}
    result['issue_candidate'] = category not in {'UNKNOWN','INFRASTRUCTURE_TRANSIENT'}
    return result

def repair_authority(instruction, *, explicit=False, bounded=False, validation=False):
    text=instruction.lower()
    if re.search(r'observe only|report only|dry.run',text): return 'OBSERVE_ONLY'
    if re.search(r'no commit|do not commit|no pr|manual commit|human.controlled|no autonomous|i will commit|don.t.*(?:commit|pr)',text): return 'HUMAN_CONTROLLED'
    return 'REPAIR_CANDIDATE' if explicit and bounded and validation else 'OBSERVE_ONLY'

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('workflow',choices=['docs','agents','ci'])
    parser.add_argument('--evidence',type=Path,help='local lesson evidence JSON array; CI log path for ci')
    parser.add_argument('--known-findings',type=Path,help='local confirmed issue fingerprint metadata JSON array')
    parser.add_argument('--workflow-name',default='manual')
    parser.add_argument('--step',default='failed-step')
    parser.add_argument('--check',action='store_true',help='fail on actionable deterministic docs findings')
    parser.add_argument('--dry-run',action='store_true',help='explicit observe mode (all executions are observe-only)')
    args=parser.parse_args()
    try:
        if args.workflow=='docs': items=documentation(ROOT)
        elif args.workflow=='agents': items=agents_proposals(ROOT,json.loads(args.evidence.read_text()) if args.evidence else [])
        else: items=[ci_report(ROOT,args.evidence.read_text(),args.workflow_name,args.step)] if args.evidence else []
        items=deduplicate(items,json.loads(args.known_findings.read_text()) if args.known_findings else [])
    except (OSError,ValueError,KeyError,TypeError) as error:
        sys.exit('Invalid local evidence/configuration: '+str(error))
    print(json.dumps({'mode':'OBSERVE','status':'FINDINGS' if items else 'NO ACTIONABLE FINDINGS',
        'findings':items,'mutation_performed':False,'limitations':[
        'Semantic review and live duplicate search are separate; no issue creation or repair here',
        'No CI claim without supplied actual failed log; no AGENTS proposal without eligible repeated evidence']},indent=2))
    if args.check and args.workflow=='docs' and items: raise SystemExit(1)
if __name__=='__main__': main()
