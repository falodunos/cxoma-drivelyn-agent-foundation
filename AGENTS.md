# Shared Drivelyn foundation

Read [core principles](principles/drivelyn-core-principles.md), [learning safety](principles/learning-safety.md), [issue policy](principles/issue-policy.md) and [review policy](principles/review-policy.md). This repository is an upstream authoring/template source, never a runtime prerequisite.

Keep guidance technology-neutral. Implementation architecture belongs in each consumer repository. Materialize actual versioned content locally; no sibling dependency or symlinks. Validate with `./scripts/validate-foundation`. Significant changes need reproducible validation and independent documentation/architecture review. Do not add credentials, personal configuration, product features or deferred automation.

Read [autonomous-work policy](principles/autonomous-work-policy.md) for default suitable issue handling, task opt-out and completion/commit gates. No auto-merge; user owns merge. Consumer commands and technology-specific matrices stay local.
