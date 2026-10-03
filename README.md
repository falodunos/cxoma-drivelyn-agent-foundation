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

Initial version: 1.0.0, recorded in VERSION. PATCH clarifies without behavioral workflow change; MINOR adds compatible shared rules/templates; MAJOR changes shared rules/workflows requiring consumer review.

To update a consumer, review upstream changes and technology-specific conflicts, copy the four principles files into `.drivelyn-shared/`, record version and SHA-256 of exact bytes in MANIFEST.toml, and run consumer validation and independent review. Commit snapshot, manifest and any integration changes together. Dates are omitted to keep generated snapshots reproducible. Never silently refresh snapshots or require upstream access. Reviewer/skill templates are adapted locally only when needed.

Run `./scripts/validate-foundation` with Python 3.11+; no third-party packages, network or credentials are needed. Consumer integrity checks verify local content against the local manifest, not cryptographic upstream authenticity. Compare upstream deliberately during upgrades.
