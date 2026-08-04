# Tasks: Scoop Bucket Cleanup Sweep

## Review Workload Forecast

| Field | Value |
|-------|-------|
| Estimated changed lines | ~160 (range 130–190) |
| 400-line budget risk | Low |
| Chained PRs recommended | No |
| Suggested split | single PR |
| Delivery strategy | ask-on-risk (default) |
| Chain strategy | pending |

Decision needed before apply: No
Chained PRs recommended: No
Chain strategy: pending
400-line budget risk: Low

### Suggested Work Units

| Unit | Goal | Likely PR | Notes |
|------|------|-----------|-------|
| 1 | Config-file foundation (3 new files) | PR 1 | Independent; low risk |
| 2 | Existing-file fixes (auto-pr, template, CI) | PR 1 | Independent of Unit 1 |
| 3 | README rewrite incl. topic doc | PR 1 | Depends on knowing bucket manifest list |

All units map to a single PR — no chained PRs needed. Commits should split by
work unit (config foundation / fixes / README) per work-unit-commits.

## Parallelism & Ordering

- Phase 1 (1.1–1.3) and Phase 2 (2.1–2.2) are fully **parallel** — independent files.
- Phase 3.1 (`formatjson` local verify) MUST precede 3.2 (CI step) to avoid breaking main.
- Phase 4.1 (README rewrite) precedes 4.2 (topic doc) — same file.
- Optimal order: Phase 3 first (gate CI safety), then 1 → 2 → 4, then Phase 5 verify.

## Phase 1: Verification Gate (must precede CI change)

- [x] 1.1 Run `pwsh -File bin/formatjson.ps1` locally; confirm exit 0 against `bucket/sonarpad.json` and `bucket/vetube.json` (Scenario: Good manifests)
- [x] 1.2 If any manifest fails, fix the manifest BEFORE adding the CI step (out of scope? surface as blocker)

## Phase 2: Configuration File Foundation (new files, parallel)

- [x] 2.1 Create `PSScriptAnalyzerSettings.psd1` at repo root; loadable by `.vscode/settings.json` (`powershell.scriptAnalysis.settingsPath`), OTBS preset, include `DSC*` and `PSUse*` common rules (Scenario: VS Code finds settings)
- [x] 2.2 Create `.github/dependabot.yml` — `github-actions` ecosystem, `/.github/workflows` dir, weekly schedule, `open-pull-requests-limit: 5`, group github-actions updates (Scenario: Opens version PRs)
- [x] 2.3 Create `.github/stale.yml` — stale after 60 days, close after 90 more, exempt labels `pinned`/`triage`, `operations/` and `bucket/` exempt where appropriate (Scenarios: Stale issue warned, Exempt issue skipped)

## Phase 3: Existing-File Fixes (parallel, independent of Phase 2)

- [x] 3.1 Replace `bin/auto-pr.ps1` `$upstream` default `"<username>/<bucketname>:main"` with `"Row0902/scoop-bucket:master"` (Scenario: Default upstream correct)
- [x] 3.2 Replace `.github/ISSUE_TEMPLATE/package-request.yml` placeholder `Criteria 1/2/3` with real criteria: open-source license, stable release tag, not already in ScoopInstaller main buckets (Scenarios: No placeholder criteria, Real criteria visible)
- [x] 3.3 Add `formatjson` step to `.github/workflows/ci.yml` test job — runs `.\my_bucket\bin\formatjson.ps1` with `SCOOP_HOME` set, fails build on bad JSON (Scenario: Bad JSON). Depends on 1.1 passing first.

## Phase 4: README Personalization (same file, sequential)

- [x] 4.1 Rewrite `README.md` — replace `<username>`/`<bucketname>` with `Row0902`/`scoop-bucket`; uncomment + fix CI and Excavator badge URLs; add license badge; add bucket description; add **Manifests** list enumerating `sonarpad` and `vetube`; remove the "How do I use this template?" section (Scenarios: Placeholders removed, Badges resolve, Manifests list present)
- [x] 4.2 Add a **Maintenance** section documenting the manual GitHub `scoop-bucket` topic requirement for scoop.sh indexing (Scenario: Topic step documented)

## Phase 5: Verification

- [x] 5.1 `Select-String -Path README.md, bin/auto-pr.ps1 -Pattern '<username>','<bucketname>'` returns no matches
- [x] 5.2 `pwsh -File bin/formatjson.ps1` exits 0 locally
- [x] 5.3 Open VS Code in repo → no PSScriptAnalyzer "settings file not found" warning
- [ ] 5.4 Push → CI formatjson step passes; badges render on GitHub README

## Notes

- `strict_tdd: true` in `openspec/config.yaml` does not apply here: deliverables are static config files with no Pester-testable behavior. Verification uses spec's Verification Approach (grep, local command, VS Code observation, post-merge observation) instead of RED-GREEN-REFACTOR.
- Scope note: no `design.md` was produced; orchestrator supplied only proposal + spec. For a mechanical cleanup change with no architectural decisions, design is degenerate. Proceed to apply.
- Rollback: each file revertible independently via `git revert <commit>`.