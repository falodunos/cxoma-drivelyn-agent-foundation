# Stage 2 acceptance

Accepted 2026-10-03. Harness only; no product behavior, auth, scoring or trip development.

Foundation 1.1.0 is an additive workflow release with task opt-out, supported tool permissions and user merge authority preserved. Consumers materialize five principles assets with SHA-256 integrity. Technology-specific modes/matrices/skills remain consumer-local.

## Validation and review

- `./scripts/validate-foundation`: PASS.
- `python3 scripts/test_foundation.py`: two tests PASS (version drift, writable reviewer and missing policy rejection).
- All three `git diff --check`: PASS.
- Both consumer `./scripts/agent-check --codex`: PASS, including native fast/low and deep/high safe effective config and exact enabled repository issue-to-PR skill discovery.
- Issue-to-PR skill creator validation: PASS for shared template and both consumers.
- Three offline launcher/config behavior tests per consumer: PASS.
- API full check: PASS, 30 unit/security/architecture tests and 14 PostgreSQL integration tests; zero failures/errors/skips.
- Mobile full check: PASS, eight Python tests plus architecture, JVM tests, lint, Detekt, Spotless and debug assembly.
- Isolated consumer copies without foundation sibling: snapshot/native harness checks PASS with temporary Codex homes containing checkout trust only. No global Drivelyn config or live GitHub dependency. Application builds used existing environments, not isolated copies.
- Explicit self-review inspected actual diffs, policies and raw scripts: scope, credential separation, opt-out, no-merge, branch safety and runtime preservation confirmed.
- Independent read-only documentation/architecture/security/test review found one incomplete policy path in both discovery roles; corrected and re-reviewed. No material findings remain. Independent reviewer ran all eight new offline tests successfully.
- Forward review scenarios: no-PR opt-out disables commit/push/PR; unrelated unsafe dirty state stops implementation; unavailable GitHub permits accepted local commit and blocked external handoff with no fake references.

## Discovery and external integration

Read-only fallback discovery: API no grounded current issue found; mobile proposed current offline-sync account-partitioning documentation drift. Proposal, criteria and evidence recorded in the mobile evaluation. No backlog fix or issue creation performed. Duplicate search on GitHub unavailable.

GitHub CLI 2.83.1 exists; no GitHub connector/MCP exposed, no remotes in any of the three repositories and authentication fails outside sandbox. Optional probes report repository/read/search unavailable. GitHub mutation NOT TESTED. No credential handling or global Drivelyn configuration introduced.

## Commit outcome and limitations

Dedicated bootstrap branches: `codex/chore-stage-2-harness`. Scoped local commits after passing acceptance; actual SHAs reported in final handoff. No push, draft PR or merge; external handoff BLOCKED. No recursive issue/PR for bootstrap.

Native custom-role spawning, skill model execution and end-to-end GitHub issue-to-PR remain configured but unverified. Workflow policy is not server-side branch protection and does not revoke a contributor's privileges. Auto-merge is not enabled or implemented. Trip capture/sync, CI triage, dependency automation and scheduling remain deferred.
