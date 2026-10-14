# Validation portability

Status: COMPLETE; human-controlled, no commit/push/issue/PR authority for this task.

## Scope
Keep shared authoring validation portable: LF attributes, explicit UTF-8 text reads and same-interpreter subprocess invocation in disposable behavioral tests. Consumer implementation and operating-system setup stay local to consumers. Shared snapshot contents/version are unchanged.

## Gates
Run the validator, two behavioral tests and six proactive tests with Python 3.11+. Inspect diff and preserved working trees. Independent architecture/test and documentation review are required for the harness changes. Record results here after final validation; no native/product acceptance belongs to this plan.

## Evidence
Focused validator, behavioral (2) and proactive (6) checks pass on the current host. Independent architecture/test and documentation reviews completed with no remaining material findings. Final diff and unchanged-index checks passed. No product feature or deferred automation was added.
