from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
COLLECTIONS = ROOT / "collections"
NAV = COLLECTIONS / "navigasi-file"
REPO = "lamberthrumpaidus/sandbox_projects"

GROUPS = [
    ("01-python", "Kode Python", "Script dan aplikasi Python"),
    ("02-c-cpp", "Kode C dan C++", "Program dan header C/C++"),
    ("03-csharp", "Kode C# / .NET", "Program C#"),
    ("04-javascript", "Kode JavaScript", "Program dan script JavaScript"),
    ("05-css-shell", "CSS dan Shell", "Stylesheet CSS serta script shell"),
    ("06-dokumentasi", "Dokumentasi & lisensi", "README, Markdown dan lisensi"),
    ("07-data", "Dataset & notebook", "CSV, notebook Jupyter dan data"),
    ("08-gambar", "Gambar", "Gambar dan ikon proyek"),
    ("09-audio-font", "Audio & font", "Audio game dan file font"),
    ("10-arsip-aplikasi", "ZIP & aplikasi", "Arsip ZIP dan executable"),
    ("11-konfigurasi", "Konfigurasi proyek", "Manifest dan file konfigurasi proyek"),
    ("12-build-debug", "Hasil build & debug", "File compiler, cache dan log"),
    ("13-referensi-keamanan", "Referensi keamanan", "Daftar teks penelitian keamanan"),
    ("14-lainnya", "Lainnya", "File tanpa kelompok khusus"),
]
BUILD_EXT = {".obj", ".pdb", ".ilk", ".idb", ".tlog", ".log", ".cache", ".recipe", ".lastbuildstate"}
PROJECT_EXT = {".json", ".ini", ".sln", ".csproj", ".vcxproj", ".filters", ".user", ".props", ".targets"}

def classify(path: Path) -> str:
    ext = path.suffix.lower()
    name = path.name.lower()
    if ext in {".py", ".pyw"}: return "01-python"
    if ext in {".c", ".cpp", ".cc", ".h", ".hpp"}: return "02-c-cpp"
    if ext == ".cs": return "03-csharp"
    if ext in {".js", ".mjs", ".jsx", ".ts", ".tsx"}: return "04-javascript"
    if ext in {".css", ".scss", ".sh", ".bash"}: return "05-css-shell"
    if ext in {".md", ".rst", ".pdf"} or name in {"license", "copying", "notice"}: return "06-dokumentasi"
    if ext in {".csv", ".ipynb", ".xlsx", ".parquet", ".sqlite"}: return "07-data"
    if ext in {".png", ".jpg", ".jpeg", ".webp", ".gif", ".svg"}: return "08-gambar"
    if ext in {".wav", ".mp3", ".ogg", ".flac", ".ttf", ".otf"}: return "09-audio-font"
    if ext in {".zip", ".rar", ".7z", ".tar", ".exe", ".msi"}: return "10-arsip-aplikasi"
    if ext == ".txt" and "dorks" in path.parts: return "13-referensi-keamanan"
    if ext in BUILD_EXT or name.startswith("project.assets."): return "12-build-debug"
    if ext in PROJECT_EXT: return "11-konfigurasi"
    return "14-lainnya"

def size_label(size: int) -> str:
    if size >= 1048576: return "%.1f MB" % (size / 1048576)
    if size >= 1024: return "%.1f KB" % (size / 1024)
    return str(size) + " B"

def link(path: Path) -> str:
    return "https://github.com/" + REPO + "/blob/main/" + quote(path.relative_to(ROOT).as_posix(), safe="/-_.~")

def main() -> None:
    report = json.loads((COLLECTIONS / "sync-report.json").read_text(encoding="utf-8"))
    records = defaultdict(list)
    for group in sorted(COLLECTIONS.iterdir()):
        if not group.is_dir() or group.name == NAV.name:
            continue
        for project in sorted(p for p in group.iterdir() if p.is_dir()):
            for file in sorted(project.rglob("*")):
                if not file.is_file(): continue
                record = {
                    "proyek": project.name,
                    "kelompok_asli": group.name,
                    "file": file.name,
                    "path": file.relative_to(ROOT).as_posix(),
                    "url": link(file),
                    "ukuran_bytes": file.stat().st_size,
                }
                records[classify(file.relative_to(COLLECTIONS))].append(record)

    total = sum(len(row) for row in records.values())
    expected = report["copied_files"]
    if total != expected:
        raise SystemExit("Cannot index: file count mismatch (%d found, %d expected)" % (total, expected))

    NAV.mkdir(parents=True, exist_ok=True)
    md = [
        "# Katalog file berdasarkan jenis",
        "",
        "Navigasi tingkat kedua untuk file yang sudah dikelompokkan berdasarkan proyek.",
        "Semua file tetap berada di lokasi asalnya supaya program dan dependensi tidak rusak.",
        "",
        "**%d file** dari **%d repository sumber**, dalam **%d kelompok file**." % (total, report["source_repositories"], len(GROUPS)),
        "",
        "| Kelompok file | Jumlah | Keterangan |",
        "|---|---:|---|",
    ]
    for key, title, description in GROUPS:
        items = records.get(key, [])
        md.append("| [%s](%s/README.md) | %d | %s |" % (title, key, len(items), description))
        directory = NAV / key
        directory.mkdir(parents=True, exist_ok=True)
        sub = [
            "# " + title,
            "",
            "%d file — %s." % (len(items), description),
            "",
            "[Semua kategori](../README.md) | [Koleksi utama](../../README.md)",
            "",
        ]
        by_project = defaultdict(list)
        for item in items: by_project[item["proyek"]].append(item)
        for project, files in sorted(by_project.items()):
            sub += ["## %s (%d file)" % (project, len(files)), "", "| File | Ukuran | Asal |", "|---|---:|---|"]
            for item in sorted(files, key=lambda x: x["path"]):
                name = item["file"].replace("|", " / ")
                rel = item["path"].replace("|", " / ")
                sub.append("| [%s](%s) | %s | %s |" % (name, item["url"], size_label(item["ukuran_bytes"]), rel))
            sub.append("")
        if not items: sub.append("Belum ada file.")
        (directory / "README.md").write_text("\n".join(sub) + "\n", encoding="utf-8")

    md += [
        "",
        "[Lihat semua file dan lokasinya (JSON)](katalog.json)",
        "",
        "[Kembali ke pengelompokan proyek](../README.md)",
        "",
        "Katalog ini berisi tautan ke file, bukan duplikat atau pemindahan fisik.",
    ]
    (NAV / "README.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    (NAV / "katalog.json").write_text(json.dumps({
        "total_file": total,
        "repository_sumber": report["source_repositories"],
        "jumlah_kelompok": len(GROUPS),
        "tidak_memindahkan_file": True,
        "kategori": {key: records.get(key, []) for key, _, _ in GROUPS},
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    old = (COLLECTIONS / "README.md").read_text(encoding="utf-8")
    marker = "[Buka katalog berdasarkan jenis file](navigasi-file/README.md)"
    if marker not in old:
        lines = old.splitlines(keepends=True)
        lines.insert(2, "\n## Navigasi cepat\n\n" + marker + "\n\n")
        (COLLECTIONS / "README.md").write_text("".join(lines), encoding="utf-8")

    readme = ROOT / "README.md"
    root_text = readme.read_text(encoding="utf-8")
    root_marker = "[Katalog 193 file berdasarkan jenis](collections/navigasi-file/README.md)"
    if root_marker not in root_text:
        rows = root_text.splitlines(keepends=True)
        rows.insert(2, "\n## Koleksi repository yang sudah dikelompokkan\n\n" + root_marker + "\n\n")
        readme.write_text("".join(rows), encoding="utf-8")

    print("Secondary organization generated successfully: %d files / %d groups." % (total, len(GROUPS)))
    for key, _, _ in GROUPS:
        print(key, len(records.get(key, [])))

if __name__ == "__main__":
    main()
