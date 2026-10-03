#!/usr/bin/env python3
import importlib.util
from pathlib import Path
import tempfile
import json
import unittest
spec=importlib.util.spec_from_file_location('proactive',Path(__file__).with_name('proactive.py'))
p=importlib.util.module_from_spec(spec);spec.loader.exec_module(p)
class ObserveTests(unittest.TestCase):
 def test_stable_fingerprint_and_known_suppression(self):
  key=p.fingerprint('docs','repo','rule','README.md')
  self.assertEqual(key,p.fingerprint('docs','repo','rule','README.md'))
  self.assertNotEqual(key,p.fingerprint('docs','repo','rule','AGENTS.md'))
  items=p.deduplicate([{'fingerprint':key}],[{'fingerprint':key,'state':'open','issue_reference':'#1'}])
  self.assertEqual(items[0]['status'],'KNOWN_UNRESOLVED')
 def test_docs_actual_broken_link_and_source_mismatch(self):
  with tempfile.TemporaryDirectory() as d:
   root=Path(d);(root/'README.md').write_text('[guide](missing.md)')
   self.assertEqual(p.documentation(root)[0]['rule'],'broken-local-link')
   (root/'README.md').write_text('[one](missing.md) [two](other.md)')
   items=p.documentation(root)
   self.assertEqual(len({item['fingerprint'] for item in items}),2)
 def test_source_mapping_detects_claim_drift(self):
  with tempfile.TemporaryDirectory() as d:
   root=Path(d);(root/'config').mkdir();(root/'README.md').write_text('capture disabled')
   (root/'flags.txt').write_text('capture=true')
   rule={'id':'capture-status','claim_path':'README.md','claim_pattern':'capture disabled','source_path':'flags.txt','source_pattern':'capture=false','scope':'Review status'}
   (root/'config/docs-freshness.json').write_text(json.dumps({'rules':[rule]}))
   self.assertEqual(p.documentation(root)[0]['rule'],'capture-status')
   (root/'flags.txt').write_text('capture=false')
   self.assertEqual(p.documentation(root),[])
 def test_agents_rejects_one_off_and_mechanical_lesson(self):
  lesson={'repository_wide':True,'durable':True,'repeatedly_useful':True,'mechanically_enforced':False,'better_in_deep_docs':False,'proposal':'Use canonical skill','evidence':['plan-a','review-b'],'source_type':'canonical-skill'}
  self.assertTrue(p.eligible_lesson(lesson))
  self.assertFalse(p.eligible_lesson(dict(lesson,evidence=['one-event'])))
  self.assertFalse(p.eligible_lesson(dict(lesson,mechanically_enforced=True)))
 def test_first_failure_and_unknown_are_not_repair(self):
  self.assertEqual(p.classify_ci("Failed to find package 'tools'\nTests run: 2, Failures: 1"),('TOOLCHAIN_SETUP',1))
  self.assertEqual(p.classify_ci('unclassified failure'),('UNKNOWN',None))
  self.assertFalse(p.ci_report(Path('repo'),'connection reset','ci','setup')['repair_candidate'])
 def test_opt_out_wins(self):
  for text in ['observe only','report only']:
   self.assertEqual(p.repair_authority(text,explicit=True,bounded=True,validation=True),'OBSERVE_ONLY')
  self.assertEqual(p.repair_authority('no PR',explicit=True,bounded=True,validation=True),'HUMAN_CONTROLLED')
  self.assertEqual(p.repair_authority('',explicit=True,bounded=True,validation=False),'OBSERVE_ONLY')
if __name__=='__main__':unittest.main()
