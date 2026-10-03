# Proportionate review

Use repository-local reviewer guidance. Significant architecture, security, feature-slice or harness changes require independent review; trivial changes may use documented self-review. Select roles by impact, not by a requirement to invoke every reviewer. Reviewers inspect actual changes and evidence read-only; authors implement fixes and own validation.

- Architecture reviewer: boundaries, dependency direction, ownership and portability.
- Security reviewer: identity, authorization, sensitive data, trust and input handling.
- Test reviewer: meaningful coverage, reproducibility, failure paths and truthful acceptance evidence.
- Documentation reviewer: accurate guidance, links, commands, scope and portability.
- Learning-safety reviewer: evidence, uncertainty, explainability, coaching and distraction.

Auth/security changes require security and test review. Schema changes require architecture and test review, with security as needed. Telemetry/scoring and active-driving UI require test and learning-safety review; architecture/security/docs depend on impact. Documentation-only changes need documentation review, plus learning-safety when learning claims change.

Report actionable severity, file/line, evidence and suggested correction. Record checks performed and limitations; no invented findings. Resolve material findings and rerun affected checks. Consumers may adapt the baseline with documented technology-specific reasons; record conflicts instead of silently resolving them.
