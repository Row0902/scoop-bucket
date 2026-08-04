# Row0902's Scoop Bucket

[![CI](https://github.com/Row0902/scoop-bucket/actions/workflows/ci.yml/badge.svg)](https://github.com/Row0902/scoop-bucket/actions/workflows/ci.yml)
[![Excavator](https://github.com/Row0902/scoop-bucket/actions/workflows/excavator.yml/badge.svg)](https://github.com/Row0902/scoop-bucket/actions/workflows/excavator.yml)
[![License](https://img.shields.io/github/license/Row0902/scoop-bucket)](LICENSE)

Personal [Scoop](https://scoop.sh) bucket for Windows packages that are not available in the official ScoopInstaller buckets.

## Manifests

| App | Description |
|-----|-------------|
| [sonarpad](bucket/sonarpad.json) | SonarPad audio tool |
| [vetube](bucket/vetube.json) | VeTube media utility |

## How do I install these manifests?

After manifests have been committed and pushed, run the following:

```pwsh
scoop bucket add scoop-bucket https://github.com/Row0902/scoop-bucket
scoop install scoop-bucket/<manifestname>
```

## How do I contribute new manifests?

To make a new manifest contribution, please read the [Contributing
Guide](https://github.com/ScoopInstaller/.github/blob/main/.github/CONTRIBUTING.md)
and [App Manifests](https://github.com/ScoopInstaller/Scoop/wiki/App-Manifests)
wiki page.

## Maintenance

To have this bucket indexed on `https://scoop.sh`, the repository must have the
`scoop-bucket` topic configured. This is a manual action in the GitHub UI:

1. Open the repository on GitHub.
2. Click the gear icon next to **About** on the right-hand sidebar.
3. Under **Topics**, add `scoop-bucket`.
4. Click **Save changes**.
