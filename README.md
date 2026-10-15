# Drivelyn agent foundation

Authoritative shared authoring source for Drivelyn-wide principles and portable Codex templates. Each application owns its implementation architecture and a self-contained `.drivelyn-shared/` snapshot. Normal development never needs this repository alongside it.

## Contents

- [Agent entry point](AGENTS.md)
- [Core principles](principles/drivelyn-core-principles.md)
- [Learning safety](principles/learning-safety.md)
- [Issue policy](principles/issue-policy.md)
- [Review policy](principles/review-policy.md)
- [Autonomous work policy](principles/autonomous-work-policy.md)
- [Proactive automation policy](principles/proactive-automation-policy.md)
- [Learning-safety reviewer](reviewer-templates/learning-safety-reviewer.toml)
- [Skill templates](skill-templates/README.md)
- [Contract governance](contract-governance/api-consumer-rules.md)
- [Codex evaluation](templates/codex-evaluation.md)
- [Reviewer triggers](templates/reviewer-trigger-matrix.md)

## Drivelyn MVP evidence pack

The completed MVP/POC physical-device user journey is documented in an evidence pack produced from the physical-device acceptance run and supporting screenshots. The [Markdown journey](https://github.com/falodunos/cxoma-drivelyn-mobile/blob/master/output/pdf/drivelyn-mvp-user-journey.md) provides the textual narrative, and the [PDF walkthrough](https://github.com/falodunos/cxoma-drivelyn-mobile/blob/master/output/pdf/drivelyn-mvp-user-journey.pdf) provides the visual walkthrough. The [screenshot inventory](https://github.com/falodunos/cxoma-drivelyn-mobile/blob/master/output/pdf/drivelyn-mvp-screenshot-inventory.md) records screenshots used and excluded, evidence levels, and privacy-redaction decisions.

The pack belongs in `cxoma-drivelyn-mobile` as product/mobile evidence; this foundation references it as an example output of the Codex/agent-assisted development workflow supported by repository instructions (`AGENTS.md`), execution plans, reusable skills, specialist reviewers/subagents, scope discipline, CI triage and bounded repair, and shared agent-foundation principles. The screenshots demonstrate interface and user-journey behavior. Where the acceptance build used synthetic route data, they are not evidence of real learner driving performance.

The [five-minute MVP pitch deck](https://github.com/falodunos/cxoma-drivelyn-mobile/blob/master/output/Drivelyn_5_Minute_MVP_Pitch_Deck.pptx) is also available in the mobile repository.

## Drivelyn applications

This foundation provides shared principles and portable authoring templates for the two Drivelyn application repositories. It is not a runtime dependency; each application keeps its implementation architecture and a locally materialized snapshot of shared guidance.

- [Drivelyn API](https://github.com/falodunos/cxoma-drivelyn-api) — the backend service that owns authoritative analysis and review for scoring and publishes the public API contract consumed by client applications.
- [Drivelyn Mobile](https://github.com/falodunos/cxoma-drivelyn-mobile) — the learner-facing mobile client for Drivelyn’s driving-learning system.


## Request access to the private application repositories

The Drivelyn Agent Foundation is public, while the application repositories are kept private.

Judges and authorized reviewers can request temporary access here:

**[Request access to Drivelyn Mobile / API](https://github.com/falodunos/cxoma-drivelyn-agent-foundation/issues/new?template=private-repository-access-request.yml)**

Please provide only your GitHub username and the repository you need to review. Do not include passwords, tokens, private email addresses, or other sensitive information.

Approved reviewers will be granted access manually through GitHub.


## Versioning and materialization

Current version: 1.2.0, recorded in VERSION. PATCH clarifies without behavioral workflow change; MINOR adds compatible shared rules/templates; MAJOR changes shared rules/workflows requiring consumer review.

To update a consumer, review upstream changes and technology-specific conflicts, copy all six files in `principles/` into `.drivelyn-shared/`, record version and SHA-256 of exact bytes in MANIFEST.toml, and run consumer validation and independent review. Commit snapshot, manifest and any integration changes together. Dates are omitted to keep generated snapshots reproducible. Never silently refresh snapshots or require upstream access. Reviewer/skill templates are adapted locally only when needed.

Run `./scripts/validate-foundation` with Python 3.11+; no third-party packages, network or credentials are needed. Consumer integrity checks verify local content against the local manifest, not cryptographic upstream authenticity. Compare upstream deliberately during upgrades.

## Release history

Stage 2 (1.1.0) added compatible opt-out-aware issue-workflow capabilities, leaving product principles, runtime behavior and contributor permission controls intact. The default applies to suitable authorized engineering tasks, not speculative backlog expansion or unattended scheduling. Consumers review and materialize this minor upgrade. Task instructions and enforced tool permissions always take precedence.

- [Issue-to-PR template](skill-templates/drivelyn-issue-to-pr/SKILL.md)
- [Draft PR template](templates/draft-pr.md)

At Stage 2 bootstrap acceptance, remotes/authentication were unavailable and external handoff was blocked. This is historical evidence. Later Stage 3 publication repair confirmed the existing published master and opened [foundation draft PR #1](https://github.com/falodunos/cxoma-drivelyn-agent-foundation/pull/1); see the [publication correction](docs/codex-evaluation.md#stage-3-publication-correction--2026-10-03). No recursive bootstrap issue/PR was created.

[Stage 2 acceptance evidence](docs/stage-2-acceptance.md). Run shared behavioral checks with `python3 scripts/test_foundation.py`.

Stage 3 (1.2.0) adds compatible observe-first proactive workflows without changing runtime or external permission controls. Consumers should review and materialize this minor upgrade. See [proactive policy](principles/proactive-automation-policy.md) and [execution plan](docs/exec-plans/completed/stage-3-proactive.md).

[Stage 3 evaluation](docs/codex-evaluation.md) separates local acceptance from unverified hosted observers.

## Portable validator invocation

Use an explicit Python 3.11+ interpreter when a host does not execute shebang files:

```sh
python3 -X utf8 scripts/validate-foundation
python3 -X utf8 scripts/test_foundation.py
python3 -X utf8 -m unittest discover -s automation-templates -p 'test*.py'
```

Maintained text uses LF and explicit UTF-8 reads; behavioral tests launch the validator with the same interpreter. This authoring repository does not own consumer toolchains or operating-system setup. See the [validation portability plan](docs/exec-plans/completed/validation-portability.md).
