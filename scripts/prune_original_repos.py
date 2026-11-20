from __future__ import annotations
import argparse
import json
import shutil
import subprocess
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "collections" / "manifest.json"
OWNER = "lamberthrumpaidus"

def run(*args: str, cwd: Path | None = None) -> str:
    result = subprocess.run(args, cwd=cwd, text=True, check=True, capture_output=True)
    return result.stdout.strip()

def candidates() -> list[str]:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    protected = set(manifest["protected_repositories_with_index_html"])
    protected.add(manifest["destination"])
    protected.add(OWNER)
    protected.add("lamberthrumpaidus")
    names = list(dict.fromkeys(r["name"] for group in manifest["groups"] for r in group["repositories"]))
    result = [name for name in names if name not in protected]
    if len(names) != 40 or len(result) != 38 or len(protected) != 9:
        raise RuntimeError("Repository safety verification failed")
    return result

def main() -> None:
    parser = argparse.ArgumentParser(description="Back up 38 repository histories before optional GitHub deletion.")
    parser.add_argument("--execute", action="store_true", help="Back up and ask to confirm deletions")
    parser.add_argument("--backup-dir", type=Path)
    args = parser.parse_args()
    if not MANIFEST.is_file():
        raise SystemExit("Source manifest is missing")
    names = candidates()
    print("Seven website repositories, sandbox_projects, and the GitHub profile repository are protected.")
    print("Deletion candidates:", len(names))
    for name in names:
        print(" ", OWNER + "/" + name)
    if not args.execute:
        print("DRY RUN. No repositories have been deleted.")
        print("Run with --execute to create full Git history backups and request a final confirmation.")
        return

    for program in ("git", "gh"):
        if not shutil.which(program):
            raise SystemExit(program + " is not installed")
    run("gh", "auth", "status")
    backup = args.backup_dir or (Path.cwd() / ("github-history-backup-" + datetime.now().strftime("%Y%m%d-%H%M%S")))
    backup = backup.expanduser().resolve()
    if backup.exists() and any(backup.iterdir()):
        raise SystemExit("Choose an empty backup directory.")
    backup.mkdir(parents=True, exist_ok=True)

    for name in names:
        destination = backup / (name + ".git")
        print("Backing up", name, flush=True)
        run("git", "clone", "--mirror", "https://github.com/" + OWNER + "/" + name + ".git", str(destination))
        run("git", "fsck", "--no-reflogs", "--full", cwd=destination)
        refs = run("git", "show-ref", cwd=destination)
        if not refs:
            raise RuntimeError("No Git refs were saved for " + name)
    print("All 38 mirrors validated successfully.")
    print("Complete Git history backup:", backup)
    print("Deletion also removes GitHub-hosted issues, PRs, repository settings and old URLs.")
    typed = input("To delete the 38 original repositories, type HAPUS 38 REPOSITORY: ")
    if typed != "HAPUS 38 REPOSITORY":
        print("Cancelled. Original repositories remain untouched.")
        return
    for name in names:
        print("Deleting", OWNER + "/" + name, flush=True)
        subprocess.run(["gh", "repo", "delete", OWNER + "/" + name, "--yes"], check=True)
    print("Finished. Full mirror backups are stored at", backup)

if __name__ == "__main__":
    main()
