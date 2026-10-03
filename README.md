# Drivelyn agent foundation

Authoritative shared authoring source for Drivelyn-wide principles and portable Codex templates. Each application owns its implementation architecture and a self-contained `.drivelyn-shared/` snapshot. Normal development never needs this repository alongside it.

## Contents

- [Agent entry point](AGENTS.md)
- [Core principles](principles/drivelyn-core-principles.md)
- [Learning safety](principles/learning-safety.md)
- [Issue policy](principles/issue-policy.md)
- [Review policy](principles/review-policy.md)
- [Learning-safety reviewer](reviewer-templates/learning-safety-reviewer.toml)
- [Skill templates](skill-templates/README.md)
- [Contract governance](contract-governance/api-consumer-rules.md)
- [Codex evaluation](templates/codex-evaluation.md)
- [Reviewer triggers](templates/reviewer-trigger-matrix.md)

## Versioning and materialization

Current version: 1.1.0, recorded in VERSION. PATCH clarifies without behavioral workflow change; MINOR adds compatible shared rules/templates; MAJOR changes shared rules/workflows requiring consumer review.

To update a consumer, review upstream changes and technology-specific conflicts, copy the five principles files into `.drivelyn-shared/`, record version and SHA-256 of exact bytes in MANIFEST.toml, and run consumer validation and independent review. Commit snapshot, manifest and any integration changes together. Dates are omitted to keep generated snapshots reproducible. Never silently refresh snapshots or require upstream access. Reviewer/skill templates are adapted locally only when needed.

Run `./scripts/validate-foundation` with Python 3.11+; no third-party packages, network or credentials are needed. Consumer integrity checks verify local content against the local manifest, not cryptographic upstream authenticity. Compare upstream deliberately during upgrades.

## Stage 2 decision

1.1.0 adds compatible opt-out-aware issue-workflow capabilities, leaving product principles, runtime behavior and contributor permission controls intact. The default applies to suitable authorized engineering tasks, not speculative backlog expansion or unattended scheduling. Consumers review and materialize this minor upgrade. Task instructions and enforced tool permissions always take precedence.

- [Autonomous work policy](principles/autonomous-work-policy.md)
- [Issue-to-PR template](skill-templates/drivelyn-issue-to-pr/SKILL.md)
- [Draft PR template](templates/draft-pr.md)

Stage 2 bootstrap uses dedicated local branches and scoped commits after acceptance. No remotes or valid GitHub authentication were available; external handoff remains blocked. No recursive bootstrap issue/PR is created.

[Stage 2 acceptance evidence](docs/stage-2-acceptance.md). Run shared behavioral checks with `python3 scripts/test_foundation.py`.
