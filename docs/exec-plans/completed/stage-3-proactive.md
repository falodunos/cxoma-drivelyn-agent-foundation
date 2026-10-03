# Stage 3 proactive maintenance

## Objective, scope and baseline

Build repeatable observe-first contract, documentation, dependency, AGENTS-proposal and CI-triage workflows. No runtime/product changes, upgrades or backlog cleanup. Mobile PR #2 merged into accepted master (5cc4f39) with hosted checks green. Foundation/API remotes exist but GitHub default branch is unpublished; cross-repo automation cannot assume remote artifact availability. Clean initial trees; dedicated codex/chore-stage-3-proactive branches.

## Decision

Foundation 1.2.0 adds compatible proactive policies/templates under minor-version rules. Existing authority, opt-outs, product principles and permissions remain intact. Contract export chooses reliable source representation; no runtime redesign. Observer schedules read-only and weekly/manual; repair uses existing gated issue-to-PR workflow.

## Sub-stages

- 3A contract export/snapshot/classification: local acceptance complete.
- 3B deterministic docs baseline + semantic workflow: local acceptance complete.
- 3C evidence-driven dependency/toolchain observation: local acceptance complete.
- 3D eligibility-gated AGENTS proposals: local acceptance complete.
- 3E reusable CI triage/first failure classification: local acceptance complete.

## Acceptance and evidence

Focused offline tests, foundation/consumer native harness and full checks, observe demonstrations, isolated portability, self-review and independent architecture/test/docs/security review required. No live GitHub dependency for local checks. Actual scheduled runs and unverified integrations recorded separately.

## Risks / stop conditions

Stop for runtime redesign, nondeterministic contract, broad cross-repo secret requirements, scheduled write access, upgrade-bot behavior, AGENTS churn or unreliable classification. UNKNOWN CI requires investigation. Local observation may pass with unavailable upstream but must disclose limitation. Local validation/self-review/independent review complete; hosted execution unverified.

## Completed acceptance

[Evaluation](../../codex-evaluation.md) records scoped evidence and limitations. Foundation validator, eight tests, consumer native/full checks and isolated portability passed. No runtime changes. API/foundation published default prerequisites remain blocked; no default publication or merge authorized implicitly.
