from pathlib import Path
from collections import defaultdict
from urllib.parse import quote
import re,json

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/"collections"
PROFILE="https://github.com/lamberthrumpaidus/lamberthrumpaidus"
CATS=[
("01-programming-languages","Pemrograman","Contoh program dan latihan dasar."),
("02-desktop-games","Permainan desktop","Kumpulan aplikasi permainan untuk komputer."),
("03-ai-data-and-automation","Data dan otomatisasi","Pemrosesan data, AI, dan otomasi."),
("04-windows-guides","Panduan Windows","Panduan penggunaan dan pemeliharaan Windows."),
("05-operating-systems-and-privacy","Sistem operasi dan privasi","Materi Linux, macOS, dan privasi."),
("06-spotify-customization","Kustomisasi Spotify","Penyesuaian tema dan antarmuka Spotify."),
("07-social-media-tools","Perangkat media sosial","Panduan penggunaan alat pendukung media sosial."),
("08-security-research","Riset keamanan","Eksperimen keamanan informasi dan OSINT."),
("09-developer-resources","Referensi pengembangan","Dokumentasi lisensi dan referensi."),
("10-music-tools","Perangkat musik","Panduan pembuatan musik berbantuan AI."),
("11-hardware-iot","Perangkat keras dan IoT","Eksperimen perangkat keras dan IoT.")]
TYPES=[
("01-python","Python"),("02-c-cpp","C dan C++"),("03-csharp","C#"),
("04-javascript","JavaScript"),("05-css-shell","CSS dan shell"),
("06-dokumentasi","Dokumentasi"),("07-data","Data dan notebook"),
("08-gambar","Gambar"),("09-audio-font","Audio dan font"),
("10-arsip-aplikasi","Arsip dan aplikasi"),("11-konfigurasi","Konfigurasi"),
("12-build-debug","Hasil kompilasi"),("13-referensi-keamanan","Referensi keamanan"),
("14-lainnya","Berkas lain")]
PROJECTS={
"CPP":("Latihan C++","Contoh pemrograman C++ yang mencakup algoritma dan perhitungan dasar."),
"FINAL_PROJECT_ALGORITMA":("Perhitungan nilai rata-rata","Aplikasi konsol untuk menghitung nilai rata-rata, dikerjakan sebagai proyek kelompok."),
"JavaScript":("Latihan JavaScript","Kumpulan latihan logika dan pemrograman JavaScript."),
"Matematika":("Modul matematika Python","Implementasi fungsi matematika dasar, geometri, dan statistika dengan Python."),
"Python":("Latihan Python","Contoh program untuk pembelajaran Python dan algoritma dasar."),
"sandbox_projects":("Arsip eksperimen","Dokumentasi awal kumpulan eksperimen pemrograman."),
"FlappyGhost":("Flappy Ghost","Permainan C++ untuk menghindari rintangan dengan mengendalikan lompatan karakter."),
"Mini-PlayStation":("Mini PlayStation","Kumpulan permainan sederhana melalui terminal."),
"PlayStation-Sederhana":("PlayStation Sederhana","Koleksi permainan sederhana berbasis Python."),
"ChatGPT":("Panduan ChatGPT","Panduan menyusun permintaan dan mengevaluasi jawaban dalam penggunaan ChatGPT."),
"DownloadYoutube":("Pengunduh video","Skrip Python untuk pengunduhan video dan audio dengan yt-dlp."),
"Membuat-Karakter_AI":("Pembuatan karakter AI","Panduan penyusunan karakter percakapan menggunakan Character.AI."),
"Prediksi_Keterlambatan_e-commerce":("Prediksi keterlambatan pengiriman","Eksperimen pemodelan keterlambatan pengiriman dengan Apache Spark."),
"Python_Translate_File":("Penerjemahan dokumen Python","Eksperimen penerjemahan dokumen PDF menjadi DOCX."),
"WA-Bot-Char-AI":("Bot WhatsApp berbasis AI","Contoh integrasi percakapan WhatsApp dengan layanan AI."),
"ai-char-Lam":("AI Lam","Eksperimen karakter percakapan berbasis AI."),
"Cek-Keaslian-Windows":("Pemeriksaan aktivasi Windows","Panduan pemeriksaan status aktivasi Windows."),
"Instal-ulang-windows":("Instalasi ulang Windows","Panduan persiapan dan pemasangan ulang Windows."),
"Lock_Folders_-WINDOWS-":("Pengaturan folder Windows","Contoh pengaturan akses folder melalui skrip dan perintah Windows."),
"Melihat-isi-Wa-yang-dihapus":("Riwayat notifikasi WhatsApp","Catatan mengenai riwayat notifikasi dan pesan WhatsApp."),
"Shortcut-KeyWindows11":("Pintasan keyboard Windows 11","Referensi pintasan untuk navigasi di Windows 11."),
"Tips-and-Trik-agar-Windows11-lancar":("Pemeliharaan Windows 11","Panduan pengaturan dan pemeliharaan dasar Windows."),
"Winutil":("Winutil","Catatan penggunaan utilitas PowerShell untuk Windows."),
"Cara-Gunakan-TorBrowser":("Panduan Tor Browser","Panduan instalasi dan penggunaan Tor Browser."),
"Instal-ulang-macOS":("Instalasi ulang macOS","Panduan pencadangan data dan instalasi ulang macOS."),
"Install-Linux":("Instalasi Linux","Panduan menyiapkan media dan memasang sistem operasi Linux."),
"Linux-VS-Windows-VS-macOS":("Perbandingan sistem operasi","Perbandingan Linux, Windows, dan macOS dari segi penggunaan."),
"Custome-Spotify":("Pengaturan Spicetify","Panduan instalasi dan konfigurasi Spicetify."),
"Shadowed-Orchid":("Tema Shadowed Orchid","Dokumentasi tema Shadowed Orchid untuk Spotify."),
"Spotify_AdBlock":("Kustomisasi klien Spotify","Dokumentasi eksperimen modifikasi antarmuka Spotify."),
"Spotify_NoAD_CustomTheme":("Tema Spotify kustom","Panduan pemasangan tema kustom Spotify."),
"Remove_Tiktok_Liked_Videos":("Pengelolaan video TikTok","Panduan penggunaan ekstensi untuk mengelola video yang disukai."),
"Tiktok_Remove_Repost":("Pengelolaan repost TikTok","Panduan penggunaan ekstensi untuk mengelola repost."),
"uDork":("uDork","Dokumentasi penelitian informasi terbuka dan pengujian keamanan."),
"Lisensi-pada-Github":("Lisensi GitHub","Penjelasan jenis lisensi perangkat lunak dan penerapannya."),
"lamberthrumpaidus":("Arsip profil pengembang","Dokumentasi profil lama dan referensi portofolio."),
"Make-Music-SUNO.AI":("Panduan Suno","Panduan pemanfaatan layanan Suno untuk pembuatan musik.")}

def scrub(t):
    t=re.sub(r"(?ms)^## (?:Tentang Penulis|Hubungi Saya|Kontak)\s*\n.*?(?=^## |\Z)","",t,flags=re.I)
    t=re.sub(r"\[([^\]]+)\]\(https://github.com/lamberthrumpaidus/?\)",lambda m:"Lamberth Rumpaidus" if m.group(1).lower() in ("saya","lamberthrumpaidus") else m.group(1),t,flags=re.I)
    out=[];fence=False
    for line in t.splitlines():
        if line.strip().startswith(chr(96)*3): fence=not fence
        elif not fence:
            if re.match(r"(?i)^\s*(selamat datang|mari kita mulai|terima kasih telah|jangan ragu)",line): continue
            if line.startswith(">") and re.search("dibuat oleh|diciptakan oleh",line,re.I): continue
            line=re.sub(r"[\U0001F000-\U0001FAFF\u2600-\u27BF]\ufe0f?","",line)
            line=re.sub(r"\bkamu\b","Anda",line,flags=re.I)
            line=re.sub(r"\bnggak\b|\bgak\b","tidak",line,flags=re.I)
            line=re.sub(r"\b(mendownload)\b","mengunduh",line,flags=re.I)
        out.append(line.rstrip())
    return re.sub(r"\n{3,}","\n\n","\n".join(out)).strip()

def archives():
    n=0
    for folder in BASE.iterdir():
        if not(folder.is_dir() and re.match(r"^\d\d-",folder.name)):continue
        for project in folder.iterdir():
            if not project.is_dir():continue
            f=project/"README.md"
            if not f.is_file():continue
            title,summary=PROJECTS[project.name]
            raw=f.read_text(encoding="utf-8")
            if "[Profil utama]("+PROFILE+")" in raw[:600]:continue
            start=re.search(r"(?m)^##\s+[^#\n]+",raw)
            body=raw[start.start():] if start else "\n".join(raw.splitlines()[1:])
            body=scrub(body)
            if project.name=="lamberthrumpaidus":
                body="Dokumen ini merupakan arsip profil terdahulu. Informasi terbaru tersedia pada profil utama."
            head="# "+title+"\n\n"+summary+"\n\n[Profil utama]("+PROFILE+") · [Indeks proyek](../../../README.md)\n\n"
            content=head+body.strip()+"\n"
            if content.count(PROFILE)!=1:raise RuntimeError("Tautan kredit ganda: "+str(f))
            f.write_text(content,encoding="utf-8")
            n+=1
    return n

def size(n):
    return (str(round(n/1024,1))+" KB") if n>=1024 else str(n)+" B"

def indexes():
    meta=[]
    for slug,title,summary in CATS:
        folder=BASE/slug
        projects=sorted((p for p in folder.iterdir() if p.is_dir()),key=lambda p:p.name.lower())
        counts={p.name:sum(pth.is_file() for pth in p.rglob("*")) for p in projects}
        meta.append((slug,title,len(projects),sum(counts.values())))
        lines=["# "+title,"",summary,"",
        "[Profil utama]("+PROFILE+") · [Indeks kategori](../README.md)","","## Daftar proyek","",
        "| Proyek | Jumlah berkas |","|---|---:|"]
        for p in projects:lines.append("| ["+p.name+"](./"+quote(p.name)+"/) | "+str(counts[p.name])+" |")
        (folder/"README.md").write_text("\n".join(lines)+"\n",encoding="utf-8")
    if sum(x[3] for x in meta)!=193:raise RuntimeError("Perubahan jumlah berkas sumber.")
    lines=["# Indeks proyek","","Koleksi proyek disusun berdasarkan bidang. Pilih kategori untuk membuka daftar proyek beserta berkasnya.","",
    "[Profil utama]("+PROFILE+") · [Halaman repository](../README.md) · [Indeks berkas](navigasi-file/README.md)","",
    "| Kategori | Proyek | Berkas |","|---|---:|---:|"]
    lines += ["| ["+t+"]("+s+"/README.md) | "+str(p)+" | "+str(n)+" |" for s,t,p,n in meta]
    (BASE/"README.md").write_text("\n".join(lines)+"\n",encoding="utf-8")
    catalog_path=BASE/"navigasi-file"/"katalog.json"
    catalog=json.loads(catalog_path.read_text(encoding="utf-8"))
    if catalog["total_file"]!=193:raise RuntimeError("Katalog tidak sesuai.")
    for _,items in catalog["kategori"].items():
        for item in items:
            fp=ROOT/item["path"]
            if not fp.is_file():raise RuntimeError("File tidak ditemukan: "+str(fp))
            item["ukuran_bytes"]=fp.stat().st_size
    catalog_path.write_text(json.dumps(catalog,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    nav=BASE/"navigasi-file"
    listing=["# Indeks berkas","","Berkas disajikan berdasarkan jenis untuk memudahkan pencarian. Struktur direktori proyek tetap dipertahankan.","",
    "[Profil utama]("+PROFILE+") · [Indeks proyek](../README.md)","",
    "| Jenis berkas | Jumlah |","|---|---:|"]
    for slug,title in TYPES:
        items=catalog["kategori"][slug]
        listing.append("| ["+title+"]("+slug+"/README.md) | "+str(len(items))+" |")
        doc=["# "+title,"","Daftar berkas dalam kategori ini, dikelompokkan menurut proyek.","",
        "[Profil utama]("+PROFILE+") · [Seluruh jenis berkas](../README.md) · [Indeks proyek](../../README.md)",""]
        grouped=defaultdict(list)
        for item in items:grouped[item["proyek"]].append(item)
        for project,records in sorted(grouped.items()):
            doc+=["## "+project,"","| Berkas | Ukuran |","|---|---:|"]
            for item in sorted(records,key=lambda r:r["path"]):
                doc.append("| ["+item["file"].replace("|","/")+"]("+item["url"]+") | "+size(item["ukuran_bytes"])+" |")
            doc.append("")
        if not items:doc+=["Belum terdapat berkas pada kategori ini.",""]
        (nav/slug/"README.md").write_text("\n".join(doc).rstrip()+"\n",encoding="utf-8")
    listing+=["","[Indeks data JSON](katalog.json)",""]
    (nav/"README.md").write_text("\n".join(listing),encoding="utf-8")

def root():
    source=(ROOT/"README.md").read_text(encoding="utf-8")
    if "collection-mark.svg" not in source:raise RuntimeError("Logo koleksi hilang.")
    lines=['<div align="center">','  <img src="./assets/collection-mark.svg" alt="Identitas Sandbox Projects" width="84" />',
    '  <h1>Sandbox Projects</h1>','  <p>Koleksi kode, panduan, dan eksperimen pengembangan perangkat lunak.</p>',
    '  <p><a href="'+PROFILE+'">Profil utama</a> · <a href="./collections/README.md">Daftar proyek</a></p>',
    '</div>','','---','','## Koleksi','',
    'Repository ini menyimpan contoh program, dokumentasi teknis, dan eksperimen yang disusun berdasarkan bidang pengembangan.',
    'Terdapat **11 kategori, 49 direktori proyek, dan 193 berkas**.',
    '','[Jelajahi kategori proyek](collections/README.md) · [Temukan berkas berdasarkan jenis](collections/navigasi-file/README.md)',
    '','## Penggunaan','',
    'Salin repository untuk meninjau atau menjalankan proyek secara lokal:',
    '',chr(96)*3+'bash',
    'git clone https://github.com/lamberthrumpaidus/sandbox_projects.git',chr(96)*3,'',
    'Petunjuk pelaksanaan tersedia pada dokumentasi masing-masing proyek. Beberapa proyek lama mungkin membutuhkan penyesuaian versi dependensi.',
    '']
    (ROOT/"README.md").write_text("\n".join(lines),encoding="utf-8")

def validate():
    files=[ROOT/"README.md",BASE/"README.md"] + list((BASE/"navigasi-file").glob("**/README.md"))
    files+=list(BASE.glob("[0-9][0-9]-*/README.md"))+list(BASE.glob("[0-9][0-9]-*/*/README.md"))
    files=list(set(files))
    if len(files)!=65:raise RuntimeError("Jumlah README pertama: "+str(len(files)))
    for file in files:
        s=file.read_text(encoding="utf-8")
        if s.count(PROFILE)!=1:raise RuntimeError("Profil utama harus tertaut sekali: "+str(file))
        if "Universitas Amikom" in s or "bukan pintasan buatan" in s:raise RuntimeError("Kalimat tidak sesuai: "+str(file))
    print("README kurasi diverifikasi:",len(files))

if __name__=="__main__":
    print("Arsip yang disunting:",archives())
    indexes()
    root()
    validate()
