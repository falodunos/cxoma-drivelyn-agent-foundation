# Reviewer trigger baseline

Select reviewers by actual impact. Adapt with documented local reasons; do not invoke every role mechanically. Required roles are independent; authors implement findings. Trivial edits may use proportionate self-review under the local review policy.

| Change | Architecture | Security | Test | Docs | Learning Safety |
| --- | --- | --- | --- | --- | --- |
| Auth/session/JWT/OIDC | as needed | required | required | as needed | no |
| Persistence/schema | required | as needed | required | as needed | no |
| Concurrency/idempotency | required | as needed | required | optional | no |
| Telemetry/scoring | as needed | as needed | required | as needed | required |
| Active-driving UI | as needed | as needed | required | as needed | required |
| API contract | optional | as needed | required | required | if semantics change |
| Documentation only | no | no | optional | required | if learning claims change |
| Harness/Codex workflow | required | if external access | required | required | if learning claims change |
