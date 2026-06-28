# Spec: Scoop Bucket Cleanup Sweep

Pure structural/configuration cleanup. No existing specs to delta against; this
change introduces a new `bucket-cleanup` domain with one requirement per
deliverable.

## ADDED Requirements

### Requirement: README Personalization

`README.md` MUST replace template identifiers (`<username>`, `<bucketname>`)
with `Row0902` and `scoop-bucket`, add a bucket description, a manifests list,
and working CI/Excavator/license badges resolving to this repo's workflow runs.
It SHOULD NOT retain the "How do I use this template?" onboarding section.

#### Scenario: Placeholders removed

- GIVEN README.md
- WHEN searched for `<username>` or `<bucketname>`
- THEN no matches remain

#### Scenario: Badges resolve

- GIVEN the README badges
- WHEN opened in a browser
- THEN CI, Excavator, and license badges resolve to this repo's actions/metadata

#### Scenario: Manifests list present

- GIVEN `bucket/` contains manifests
- WHEN the README is read
- THEN an app list section enumerates each manifest

### Requirement: auto-pr Upstream Fix

`bin/auto-pr.ps1` `$upstream` param default MUST be `Row0902/scoop-bucket:master`,
matching the repo default branch.

#### Scenario: Default upstream correct

- GIVEN `auto-pr.ps1` invoked with no `-upstream`
- WHEN the param binds
- THEN `$upstream` equals `Row0902/scoop-bucket:master`

#### Scenario: Branch rename handled

- GIVEN the repo migrates to `main`
- WHEN the param default is unchanged
- THEN auto-pr fails against the missing `master` branch (signal to update)

### Requirement: Package Request Template Criteria

`.github/ISSUE_TEMPLATE/package-request.yml` MUST replace placeholder
`Criteria 1/2/3` with real acceptance criteria for this bucket (open-source
license, stable release tag, not already in ScoopInstaller main buckets).

#### Scenario: No placeholder criteria

- GIVEN the rendered template
- WHEN inspected
- THEN no checkbox labeled `Criteria 1`, `Criteria 2`, or `Criteria 3`

#### Scenario: Real criteria visible

- GIVEN an issue opener
- WHEN they read the Criteria section
- THEN they see specific, actionable acceptance rules

### Requirement: PSScriptAnalyzer Settings File

`PSScriptAnalyzerSettings.psd1` MUST exist at repo root and be loadable by the
VS Code PowerShell extension per `.vscode/settings.json`.

#### Scenario: VS Code finds settings

- GIVEN `.vscode/settings.json` references `PSScriptAnalyzerSettings.psd1`
- WHEN the PowerShell extension loads
- THEN no "settings file not found" warning appears

#### Scenario: Invalid settings file

- GIVEN the `.psd1` has syntax errors
- WHEN PSScriptAnalyzer runs on save
- THEN it fails loudly with a parse error

### Requirement: formatjson CI Step

`.github/workflows/ci.yml` MUST run `bin/formatjson.ps1` on push/PR and fail the
build on malformed manifests.

#### Scenario: Good manifests

- GIVEN all manifests are valid JSON matching the Scoop schema
- WHEN CI runs the formatjson step
- THEN the step succeeds

#### Scenario: Bad JSON

- GIVEN a manifest with broken JSON
- WHEN CI runs the formatjson step
- THEN the workflow fails

### Requirement: Dependabot Config

`.github/dependabot.yml` MUST enable weekly checks for the `github-actions`
ecosystem covering `/.github/workflows`.

#### Scenario: Opens version PRs

- GIVEN a pinned action has a newer release
- WHEN Dependabot runs weekly
- THEN a PR bumps the pinned version with a changelog summary

### Requirement: Stale Bot Config

`.github/stale.yml` MUST mark issues/PRs stale after 60 days, close after 90
more days of inactivity, and exempt issues labeled `pinned` or `triage`.

#### Scenario: Stale issue warned

- GIVEN an issue with no activity for 60 days
- WHEN Stale bot runs
- THEN a stale warning comment is posted and the `stale` label applied

#### Scenario: Exempt issue skipped

- GIVEN an issue labeled `pinned`
- WHEN Stale bot runs
- THEN it is not marked stale

### Requirement: scoop-bucket Topic Documentation

The README MUST document the GitHub `scoop-bucket` topic requirement for
scoop.sh indexing, noting it is a manual UI action.

#### Scenario: Topic step documented

- GIVEN the README maintenance section
- WHEN read
- THEN it instructs the owner to add the `scoop-bucket` topic via GitHub UI

---

## Verification Approach

- `grep -c '<username>\|<bucketname>' README.md bin/auto-pr.ps1` MUST return 0.
- `pwsh -File bin/formatjson.ps1` MUST exit 0 locally before CI commit.
- Open VS Code in repo: no PSScriptAnalyzer "settings not found" warning.
- After merge, observe: Dependabot opens an action-bump PR within one week;
  Stale bot posts on a >60-day issue; badges resolve on README render.
- Manually add the `scoop-bucket` GitHub topic and confirm the repo appears on
  `https://scoop.sh`.

## Edge Cases

- Template-regression: future re-fork could reintroduce placeholders — guard
  with a CI grep step (optional, out of scope here).
- Stale bot false-positive on slow-but-valid requests — mitigated by `pinned`
  and `triage` exempt labels.
- Dependabot noise — keep `open-pull-requests-limit: 5` and group github-actions.
- Branch rename to `main` would silently break `auto-pr.ps1` default; track via
  a follow-up if/when migration happens.