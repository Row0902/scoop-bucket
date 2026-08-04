# Proposal: Scoop Bucket Cleanup Sweep

## Intent

The bucket is in early state — forked from ScoopInstaller/BucketTemplate with unreplaced placeholders, missing files, and no discoverability. This change cleans up every broken or placeholder artifact so the repo is self-consistent, properly configured, and discoverable on scoop.sh.

## Scope

### In Scope
- Personalize README.md: replace `<username>/<bucketname>`, add badges, app list, bucket description
- Fix `bin/auto-pr.ps1` upstream to `Row0902/scoop-bucket:master`
- Fill placeholder criteria in `.github/ISSUE_TEMPLATE/package-request.yml`
- Create missing `PSScriptAnalyzerSettings.psd1`
- Add `formatjson.ps1` lint step to `.github/workflows/ci.yml`
- Add Dependabot config (`.github/dependabot.yml`) for GitHub Actions
- Add stale bot config (`.github/stale.yml`) for issue management
- Document `scoop-bucket` GitHub topic requirement (requires GitHub UI)

### Out of Scope
- Adding new manifests or changing existing ones
- Changing test infrastructure or test runner
- Schema validation changes or JSON schema overhaul
- Adding CODEOWNERS, SECURITY.md, or CONTRIBUTING.md
- Moving to `main` branch from `master`

## Capabilities

This change is pure cleanup — no new capabilities, no spec-level behavior changes. All deliverables are structural/configuration fixes.

### New Capabilities
None — no new specs required.

### Modified Capabilities
None — no existing capabilities to modify.

## Approach

Identify every place the template left a `<placeholder>`, a missing file reference, or a missing automation guard, then fix each one in a focused pass. No architectural decisions, no refactors — just mechanical cleanup with verification via CI.

## Affected Areas

| Area | Impact | Description |
|------|--------|-------------|
| `README.md` | Modified | Replace placeholders, add badges + app list |
| `bin/auto-pr.ps1` | Modified | Fix `$upstream` default value |
| `.github/ISSUE_TEMPLATE/package-request.yml` | Modified | Fill real criteria for this bucket |
| `.github/workflows/ci.yml` | Modified | Add `formatjson.ps1` check step |
| `PSScriptAnalyzerSettings.psd1` | Created | Missing file referenced by VS Code |
| `.github/dependabot.yml` | Created | Auto-update GitHub Actions versions |
| `.github/stale.yml` | Created | Close stale issues/PRs after 60 days |

## Risks

| Risk | Likelihood | Mitigation |
|------|------------|------------|
| `formatjson.ps1` fails on existing manifests | Low | Run locally first, fix any issues before CI change |
| Stale bot closes valid issues too aggressively | Low | Use 60-day warn, 90-day close with exempt labels |
| GitHub topic needs manual UI action | High (cannot automate) | Document clearly in README and pinned issue |

## Rollback Plan

Revert each file individually via `git revert <commit>`. The changes are independent — any single file can be rolled back without affecting others.

## Dependencies

- None — all changes are self-contained within this repo

## Success Criteria

- [ ] `README.md` has no `<username>` or `<bucketname>` placeholder strings
- [ ] `bin\auto-pr.ps1` defaults to `Row0902/scoop-bucket:master`
- [ ] `package-request.yml` shows real criteria, not "Criteria 1/2/3"
- [ ] `PSScriptAnalyzerSettings.psd1` exists and VS Code finds it
- [ ] CI workflow runs `formatjson.ps1` on push/PR and fails on bad JSON
- [ ] Dependabot opens weekly PRs for GitHub Actions version bumps
- [ ] Stale bot marks issues/PRs inactive after 60 days
