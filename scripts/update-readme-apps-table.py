#!/usr/bin/env python3

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
BUCKET = ROOT / "bucket"

START = "<!-- apps-table:start -->"
END = "<!-- apps-table:end -->"


def manifest_data(path: Path) -> dict[str, str]:
    data = json.loads(path.read_text(encoding="utf-8"))
    return {
        "version": str(data.get("version", "")),
        "homepage": str(data.get("homepage", "")),
    }


def load_base_versions(path: Path) -> dict[str, str]:
    if not path.exists():
        return {}
    versions = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        parts = line.split("\t", 1)
        if len(parts) == 2:
            versions[parts[0].strip()] = parts[1].strip()
    return versions


def save_base_versions(path: Path, versions: dict[str, str]) -> None:
    lines = [f"{name}\t{versions[name]}" for name in sorted(versions)]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def generate_table(base_versions: dict[str, str], manifest_info: dict[str, dict[str, str]]) -> str:
    rows = [
        "| Nombre | Versión base | Última versión | Sitio oficial |",
        "|---|---|---|---|",
    ]
    for name in sorted(manifest_info):
        latest_version = manifest_info[name]["version"]
        homepage = manifest_info[name]["homepage"]
        rows.append(f"| {name} | {base_versions[name]} | {latest_version} | {homepage} |")
    return "\n".join(rows)


def replace_table(content: str, table: str) -> str:
    start_idx = content.find(START)
    end_idx = content.find(END)
    if start_idx == -1 or end_idx == -1 or end_idx < start_idx:
        block = f"{START}\n{table}\n{END}"
        return content.rstrip() + "\n\n## Apps del bucket\n\n" + block + "\n"

    before = content[: start_idx + len(START)]
    after = content[end_idx:]
    return before + "\n" + table + "\n" + after


def main() -> None:
    manifests = sorted(BUCKET.glob("*.json"))
    base_file = ROOT / ".github" / "apps-base-versions.tsv"
    base_versions = load_base_versions(base_file)

    manifest_info = {}
    for manifest in manifests:
        name = manifest.stem
        info = manifest_data(manifest)
        latest = info["version"]
        manifest_info[name] = info
        if name not in base_versions:
            base_versions[name] = latest

    # Keep only current manifests
    base_versions = {k: v for k, v in base_versions.items() if k in manifest_info}
    save_base_versions(base_file, base_versions)

    table = generate_table(base_versions, manifest_info)
    readme_content = README.read_text(encoding="utf-8")
    README.write_text(replace_table(readme_content, table), encoding="utf-8")


if __name__ == "__main__":
    main()
