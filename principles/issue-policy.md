# Evidence-based issue discovery

An agent may propose or create an issue only when concrete evidence exists, the problem is still current, impact is understandable, scope is actionable, acceptance criteria can be stated and duplicate search has been performed. Record search terms, scope and results. If access is unavailable, record the limitation and defer issue creation until duplicate search is possible. Follow repository authorization for external writes.

Acceptable evidence includes test or CI failure, security findings, architecture violations, documentation or contract drift, technical debt recorded in plans, recurring reviewer findings and dependency/toolchain risk. Confirm the evidence against current repository state. Speculative product ideation must not autonomously generate issues.

## Issue structure

- Title: concrete problem and affected scope.
- Evidence: reproducible command, observed result, relevant file/line or finding; duplicate search results.
- Impact: affected users, engineering work or safety.
- Scope: bounded actionable change.
- Non-goals: explicit exclusions.
- Acceptance criteria: observable outcomes and validation.
- Suggested reviewers: roles justified by the change.
- Source: discovery type and concrete evidence.

Read-only discovery labels findings PROPOSED ISSUE. Only confirmed external creation may be labeled CREATED GITHUB ISSUE. Offline proposals explicitly record unavailable duplicate search; creation is deferred.
