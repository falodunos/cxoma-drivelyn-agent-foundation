# Shared foundation Stage 3 evaluation


## Stage 3 proactive maintenance — 2026-10-03

Historical sections above describe their original acceptance state; this section supersedes current Stage 3 configuration and GitHub readiness claims.

VERIFIED: foundation 1.2.0 is a compatible minor extension with six exact-byte local policy snapshots. No runtime source, build dependency or product configuration changed. Shared policy preserves task opt-outs, human merge authority, observe-first gates and task → AGENTS/policies → architecture → untrusted issue/log data hierarchy.

VERIFIED: deterministic contract artifact and snapshot integrity; explicit local upstream comparison reports NO_DRIFT. Eight public routes and thirteen schemas derive from API mappings/records/enums/annotations plus canonical contract prose. No implementation source paths or internal service bodies exported. Per-route/field/enum/error/constraint/semantic fingerprints distinguish unrelated findings; direction changes and malformed candidates are covered. Source-only provenance changes are non-actionable. Mechanical compatibility remains conservative; supported source grammar and documented logical String enums/nullability require exporter review when architecture changes. Local mobile check validates its snapshot without API; actual drift detection needs an explicitly obtained candidate, not a claim of observing unavailable upstream.

VERIFIED: docs baseline detects broken local links and configured source mappings; distinct broken targets do not collide. Separate independent semantic review found API provider-language drift, deduplicated against all open/closed API issues, creating [API issue #1](https://github.com/falodunos/cxoma-drivelyn-api/issues/1). Backlog repair intentionally separate. No current actionable mobile docs issue; closed ownership issue is not recreated.

VERIFIED: dependency inventories and ten tests per repository classify explicit supplied evidence as SECURITY_RELEVANT, REQUIRED_COMPATIBILITY, SAFE_UPDATE_CANDIDATE, TOOLCHAIN_CASCADE_RISK or INFORMATIONAL. Different advisory IDs and compatibility rule IDs have distinct fingerprints. Mobile compatibility matrix is evaluated together. No automatic upgrades or isolated toolchain recommendations. Managed API versions remain NOT_RESOLVED where not explicitly pinned. No live release/advisory lookup or resolved dependency graph was executed; empty baseline means no supplied actionable evidence, not proof of security or latest versions.

VERIFIED: AGENTS eligibility, proposal-only reports and negative/eligible fixtures. Repository-wide, durable, repeatedly useful, concise lessons need at least two distinct durable evidence references and must not already be enforced or belong in deeper docs. Reviewer validates actual references. Shared lessons propose foundation first; consumer lessons stay local. Observe baseline has no eligible proposal; no automated instruction rewrite occurred.

VERIFIED: reusable CI-triage skill and first-material-failure classifier/opt-out tests. Actual historical mobile failed [run 37121457322](https://github.com/falodunos/cxoma-drivelyn-mobile/actions/runs/37121457322) classifies TOOLCHAIN_SETUP; confirmed green reruns 37122632491 and 37122635979 show resolution. [PR #2](https://github.com/falodunos/cxoma-drivelyn-mobile/pull/2) is merged; Stage 3 began from accepted master 5cc4f39. No new failure/repair or duplicate CI issue claimed. UNKNOWN requires investigation; logs do not confer repair authority. Raw logs remain disposable and uncommitted.

VERIFIED: deterministic fingerprint stability/open-known suppression/closed-equivalent review and per-task opt-out behavior. Live duplicate search remains required before mutation; supplied known-findings metadata is not a replacement. Observation does not mutate issues, commits, PRs or instructions. Repair follows existing gated issue-to-PR procedure, relevant independent reviewers and full validation, then draft PR and stop before merge.

CONFIGURED BUT UNVERIFIED: Monday 07:30 UTC/manual maintenance artifact workflow. It executes deterministic docs, dependency inventory and proposal/CI baselines without model review. Semantic docs/release-advisory fetching are reusable Codex procedures, not secretly scheduled agents. Immutable pinned Actions, contents:read, persist-credentials:false, bounded timeout/concurrency and no issue/PR write access. No auto-merge. Event-driven privileged CI mutation is DEFERRED.

INITIAL OBSERVATION: during original Stage 3 execution the GitHub probe returned an empty default-branch name, the optional remote contract fetch reported BLOCKED, and the API/foundation task commits remained local. The conclusion that their default branches were unpublished was not established by those observations and is corrected below. The failed fetch remains historical evidence; it does not prove upstream absence or successful comparison. Scheduled observers, mobile upstream comparison and cross-repo issue creation remain CONFIGURED BUT UNVERIFIED until actually exercised.

VERIFIED: native fast/deep safe config and exact enabled repo-scoped health, issue, CI and maintenance skill discovery without model turns. All new skills pass official quick validation. Native custom-role/model execution remains CONFIGURED BUT UNVERIFIED.

VERIFIED: full local checks, isolated harness copies without either sibling/GitHub/schedules, self-review and independent documentation/architecture/test/security review. Review resolved docs/dependency fingerprint collisions, contract direction detection, nested candidate validation and distinct contract keys; final independent review has no material findings. Isolated full application rebuild not attempted; full builds use installed toolchains/caches. No emulator/device run needed for harness-only changes.

Foundation validation and two existing plus six proactive behavioral tests pass. Consumer contract/dependency logic stays repo-specific.

## Stage 3 publication correction — 2026-10-03

VERIFIED: before publication repair, the existing Stage 2 `master` was already published at `673366dbea3a6812d115194850f4314df1e4e7d9`. The Stage 3 task branch had not been pushed and had no existing PR. Repair published the original commits (b230a14) unchanged on `codex/chore-stage-3-proactive`, creating [draft PR #1](https://github.com/falodunos/cxoma-drivelyn-agent-foundation/pull/1) against `master`. No reconstruction, force push or default-branch commit was needed. The earlier unpublished-default conclusion is corrected; the earlier empty probe and blocked fetch observations are preserved.

VERIFIED: publication reran current local validation, full API checks (32 Python tests, 30 unit/security/architecture tests and 14 PostgreSQL integration tests), foundation validation and eight tests, with clean diff checks. Explicit self-review and fresh independent documentation/architecture and test/scope review confirmed harness-only scope, unchanged public contract/runtime sources and unchanged API issue #1 specification. Review found stale publication claims; this bounded evidence correction resolves them without adding automation or shared policy.

VERIFIED: API original head `0ff280e` passed hosted push verification (run 37128268766), PR verification (37128275593) and authoritative export observation (37128268763). This proves API export execution, not mobile cross-repo comparison or scheduled observer execution. Foundation PR has no hosted PR checks attached. Subsequent documentation-only heads require their own actual check results; no prior green result is attributed to a new head.

Drafts remain unmerged with no auto-merge request. Remote master baselines are unchanged. Mobile PR #3 is untouched; no product behavior changed.

## Stage 3.5 hosted verification — 2026-10-03

This section supersedes earlier current-state publication and hosted-readiness claims; prior observations remain historical evidence. Stage 3 is merged in all three repositories. Verification used published `master`, not the former task branches.

### Preflight and exact baselines

All repositories are public. Authenticated contributor access included push/maintain/admin and workflow dispatch. Existing contributor checkouts were clean on `codex/chore-stage-3-proactive`, tracking that task branch; their `origin/master` refs were stale. Isolated clean checkouts from GitHub were used for evidence edits on `codex/chore-stage-3-5-hosted-verification`; existing contributor checkouts were preserved.

| Repository | Published default `master` SHA exercised | Original local HEAD | Original local `origin/master` |
| --- | --- | --- | --- |
| Foundation | `67353a512dd358c5c04c4947ee73cb4b5d9cc779` | `4813ac01c89ea08f241d63288c184e761b2904fc` | `673366dbea3a6812d115194850f4314df1e4e7d9` |
| API | `867f4e9efa80e4febe2c3f23dacb5f6397390aaf` | `8a9b9d6337c00b25e4bd7b86d782e5d25ba07202` | `f4c255665f7a7ff4e8b8ed6860643f9b5313e658` |
| Mobile | `6b36cc588f3071045eb5095be152ff7a48ac8b76` | `c6fbb23fce1bf068f9cb6567374ef0dfb8ccc441` | `5cc4f3930d76cd4abc83fa3a73357a3a00d66e05` |

Stage 3 observer workflows, scripts, policies and reusable CI-triage guidance were present in the merged checkouts. GitHub workflow inventory confirmed enabled dispatch workflows. Default SHAs were unchanged when checked again after all five runs.

### Inspected hosted evidence

Every run below was `workflow_dispatch`, completed successfully on the corresponding exact SHA above, and had its job/step metadata, logs and downloaded artifact contents inspected. Checkout, Python setup, intended observation/check step and artifact upload all succeeded. Artifact names below refer to uploaded report bundles, not a claim that cron or model review ran.

| Capability | Hosted run | Artifact | Inspected result |
| --- | --- | --- | --- |
| Foundation manual maintenance | [37129950475](https://github.com/falodunos/cxoma-drivelyn-agent-foundation/actions/runs/37129950475) | `maintenance-observation` | `docs.json`, `agents.json`: `NO ACTIONABLE FINDINGS`, `mutation_performed: false` |
| API manual maintenance | [37129952799](https://github.com/falodunos/cxoma-drivelyn-api/actions/runs/37129952799) | `maintenance-observation` | Docs/AGENTS/CI: `NO ACTIONABLE FINDINGS`; dependency inventory: `NO_ACTIONABLE_FINDINGS` |
| API authoritative export check/upload | [37129955393](https://github.com/falodunos/cxoma-drivelyn-api/actions/runs/37129955393) | `drivelyn-public-contract` | Log: `VERIFIED: authoritative contract export matches local sources`; `contract.json`, `MANIFEST.json`, `README.md` inspected |
| Mobile manual maintenance | [37129957773](https://github.com/falodunos/cxoma-drivelyn-mobile/actions/runs/37129957773) | `maintenance-observation` | Docs/AGENTS/CI: `NO ACTIONABLE FINDINGS`; dependency inventory: `NO_ACTIONABLE_FINDINGS` |
| Mobile published API comparison | [37130008819](https://github.com/falodunos/cxoma-drivelyn-mobile/actions/runs/37130008819) | `contract-observation` | `fetch.json`: `FETCHED_UNTRUSTED_CANDIDATE`; `drift.json`: `NO_DRIFT`, `upstreamCompared: true`, empty findings |

Foundation hosted maintenance exercised only the docs and AGENTS deterministic observers. It did not run foundation validation, a dependency observer or a CI observer. API/mobile maintenance exercised their deterministic docs freshness, dependency/toolchain inventory, AGENTS proposal baseline and CI baseline. No failed CI log was supplied, so CI baseline execution is not new operational failure triage. AGENTS reports contained no eligible proposal: **NO ELIGIBLE PROPOSAL**; no instructions or AGENTS PR were generated. Stage 2.6 mobile CI triage remains prior operational evidence, with the reusable skill still present; no intentional CI failure was introduced.

### Authoritative contract and cross-repository provenance

The API workflow recomputed the contract from current checked-out source in memory, verified snapshot structure/manifest integrity and compared exact serialized bytes with the committed export before uploading it. It did not rewrite the committed export. This supports **VERIFIED HOSTED** authoritative export validation and artifact publication on merged API `master`.

Artifact API version: `v1`; actual endpoint count: **8**; schema count: **13**. `contract.json` SHA-256: `4851e33456d9df1923c326d4b4f12cd2b5a7260aa283dbd8c6d1bad9ac3da092`. Manifest/source digest: `f0a142027d89d83cb3f973b9629b57681d7da5795c3285c3f3f46b316ad2fd10`. Manifest original export `sourceCommit`: `f4c255665f7a7ff4e8b8ed6860643f9b5313e658`; hosted checkout/source ref: `867f4e9efa80e4febe2c3f23dacb5f6397390aaf`. These are deliberately distinct: the hosted check proves current-source byte equivalence, not a regenerated manifest claiming the merge SHA. The exported public JSON contains contract fields and digests, with no internal implementation file paths or service bodies.

Mobile inputs were explicitly `api_repository=falodunos/cxoma-drivelyn-api`, `api_ref=867f4e9efa80e4febe2c3f23dacb5f6397390aaf`, `artifact_path=contracts/drivelyn-api/contract.json`, confirmed from API configuration and GitHub contents. The fetched candidate was byte-identical to the downloaded API hosted export. The comparison validated candidate structure and source-digest format, verified the local snapshot manifest/content digest, and compared contract fields/source digest. Independent byte hashing tied the fetched candidate to the hosted API artifact digest above; the fetch step alone does not authenticate a candidate manifest. `NO_DRIFT` was observed in the downloaded report, not assumed.

The existing GitHub Contents API fetch succeeded with the mobile workflow's repository-scoped `GITHUB_TOKEN` against the public API repository. No public-fetch fallback, personal token, permission expansion or workflow fix was needed. Fetched candidate JSON remained untrusted data and was not executed.

### Status boundaries and security

**VERIFIED HOSTED:** all three manual maintenance observers and report uploads; API authoritative export validation/publication; mobile hosted published-contract fetch/validation/comparison/report; read-only GitHub execution. **VERIFIED LOCAL:** prior deterministic fixture/negative-path and harness checks retain their earlier scope.

**CONFIGURED BUT UNVERIFIED:** Monday 07:30 UTC schedules. GitHub schedule-event queries returned no runs in all three repositories; manual dispatch does not verify cron execution. Semantic model documentation review and native custom-role/model execution remain unverified/manual procedures. Live release/advisory fetching and resolved dependency graphs remain unverified. Empty dependency findings mean no supplied actionable evidence, not that versions are latest or secure. Privileged/event-driven automatic repair remains **DEFERRED**.

Workflow definitions and hosted setup logs showed only `contents: read` plus implicit `metadata: read`; no issue/PR/content write permission. Checkout used immutable pinned Action SHAs and `persist-credentials: false`; setup/upload Actions were pinned, timeouts bounded. Scripts and workflow steps contained no GitHub issue/PR creation, source push or auto-merge path. Report mutation flags were false where provided. Post-run issue/PR inventories contained only pre-existing items, all created before these runs, and all default SHAs were unchanged. Artifact upload is expected report output; no repository source, issue or PR mutation was observed. No new issue was warranted by clean deterministic reports. The existing API documentation issue remains separate work.

### Explicit self-review

1. Truly hosted: the five linked dispatch runs and their intended steps above.
2. Only configured: cron schedules, semantic agent execution and live advisory lookup.
3. Actually inspected: job/step metadata and logs, all three maintenance report bundles, API contract/manifest/README, mobile fetch/candidate/drift bundle.
4. Repository mutation: none observed from workflows; clean reports, read-only token, unchanged defaults and no new issue/PR support this bounded claim.
5. Permissions above intended scope: none in exercised workflows; implicit metadata read is documented.
6. Real published API artifact: exact published API SHA and configured contract path, byte-identical to hosted export.
7. `NO_DRIFT`: actually observed with `upstreamCompared: true` and empty findings.
8. Scheduled execution: not exercised; no schedule-event history found.
9. Product/runtime code: unchanged; this evidence update changes only this evaluation document.

### Evidence-change validation and review

`./scripts/validate-foundation`, two existing foundation tests, six proactive behavioral tests and `git diff --check` passed. Explicit diff/self-review confirmed only this evaluation document changes; no runtime, workflow, contract or shared-policy edit. Independent read-only documentation, security and test/workflow reviewers inspected actual diffs, definitions and saved hosted metadata/logs/artifacts and reported no actionable findings. Review used downloaded evidence without new external calls; no third-party Action implementation audit, device run or private-upstream access test was claimed. Scoped draft publication retains human merge authority; no auto-merge.
