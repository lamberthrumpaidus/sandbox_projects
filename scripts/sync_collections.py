#!/usr/bin/env python3
# ALL Create by LamberthRumpaidus
"""Collect all files from non-website repositories without touching their originals.

Runs in the destination GitHub Actions workspace. Copies tracked files from the
source repositories' default branches, including binary assets and hidden files.
No force pushes, source modifications, source deletions, or renames.
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COLLECTIONS = ROOT / "collections"
MANIFEST = json.loads((COLLECTIONS / "manifest.json").read_text(encoding="utf-8"))
OWNER = MANIFEST["owner"]
DESTINATION = MANIFEST["destination"]
PROTECTED = set(MANIFEST["protected_repositories_with_index_html"])

def git(*args: str, cwd: Path | None = None) -> str:
    env = {**os.environ, "GIT_TERMINAL_PROMPT": "0"}
    res = subprocess.run(
        ["git", *args], cwd=cwd, env=env, check=True,
        text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    )
    return res.stdout.strip()

def assert_no_index_html(path: Path) -> None:
    if path.is_dir():
        for item in path.rglob("*"):
            if item.is_file() and item.name.casefold() == "index.html":
                raise RuntimeError(
                    f"Index HTML appeared in {path.name}: {item.relative_to(path)}; "
                    "stopping to protect websites."
                )

def copy_local_source(destination: Path) -> None:
    # Only the original sandbox_projects tracked files; excludes collection infra.
    names = subprocess.run(
        ["git", "ls-files", "-z"], cwd=ROOT, check=True,
        stdout=subprocess.PIPE,
    ).stdout.split(b"\0")
    for raw in names:
        if not raw:
            continue
        relative = Path(os.fsdecode(raw))
        if relative.parts[0] in {".github", "collections", "scripts"}:
            continue
        src = ROOT / relative
        if not src.is_file():
            continue
        out = destination / relative
        out.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, out)

def copy_clone(source: Path, destination: Path) -> None:
    shutil.copytree(
        source, destination, dirs_exist_ok=True,
        ignore=lambda d, children: {".git"} & set(children),
        copy_function=shutil.copy2,
    )

def main() -> None:
    groups = MANIFEST["groups"]
    repos = [r["name"] for g in groups for r in g["repositories"]]
    if len(repos) != len(set(repos)) or set(repos) & PROTECTED:
        raise RuntimeError("Source list contains duplicate or protected repositories.")
    if DESTINATION not in repos:
        raise RuntimeError("Destination project must be represented in the source list.")

    # Download first; do not modify the checkout unless all copies succeeded.
    with tempfile.TemporaryDirectory(prefix="lr-github-collection-") as tmp:
        scratch = Path(tmp)
        clones: dict[str, Path] = {}
        revisions: dict[str, str] = {}
        for group in groups:
            for repo in group["repositories"]:
                name, branch = repo["name"], repo["branch"]
                if name == DESTINATION:
                    clones[name] = ROOT
                    revisions[name] = git("rev-parse", "HEAD", cwd=ROOT)
                    continue
                location = scratch / name
                url = f"https://github.com/{OWNER}/{name}.git"
                print(f"Fetching {OWNER}/{name} ({branch})", flush=True)
                git("clone", "--quiet", "--depth", "1", "--single-branch",
                    "--branch", branch, url, str(location))
                assert_no_index_html(location)
                clones[name] = location
                revisions[name] = git("rev-parse", "HEAD", cwd=location)

        report: list[dict[str, object]] = []
        for group in groups:
            folder = group["folder"]
            target_group = COLLECTIONS / folder
            if target_group.exists():
                shutil.rmtree(target_group)
            target_group.mkdir(parents=True)
            for repo in group["repositories"]:
                name = repo["name"]
                target = target_group / name
                if name == DESTINATION:
                    target.mkdir()
                    copy_local_source(target)
                else:
                    copy_clone(clones[name], target)
                files = [p for p in target.rglob("*") if p.is_file()]
                report.append({
                    "category": folder,
                    "repository": name,
                    "branch": repo["branch"],
                    "source_commit": revisions[name],
                    "file_count": len(files),
                    "bytes": sum(p.stat().st_size for p in files),
                })
                print(f"Collected {name}: {len(files)} files", flush=True)

    (COLLECTIONS / "sync-report.json").write_text(
        json.dumps({
            "origin": f"https://github.com/{OWNER}",
            "target_repository": DESTINATION,
            "protected_repositories": sorted(PROTECTED),
            "source_repositories": len(repos),
            "copied_files": sum(int(x["file_count"]) for x in report),
            "details": report,
        }, indent=2, ensure_ascii=False) + "\n", encoding="utf-8",
    )
    print("Completed copying all non-website repositories.", flush=True)

if __name__ == "__main__":
    main()
