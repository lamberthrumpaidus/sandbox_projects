# Sandbox Projects — Koleksi Proyek Terstruktur

Koleksi source code, latihan, eksperimen, dan aset yang disusun **berdasarkan jenis proyek**. Setiap proyek punya folder sendiri; seluruh file pendukung tetap berada di dalam folder proyek tersebut.

**11 kategori · 49 folder proyek · 193 file asli · arsip dari 40 repository sumber.**

## Buka kategori

| Jenis proyek | Jumlah proyek | Jumlah file |
|---|---:|---:|
| [Bahasa pemrograman & aplikasi dasar](collections/01-programming-languages/README.md) | 10 | 69 |
| [Game desktop](collections/02-desktop-games/README.md) | 3 | 45 |
| [AI, data & otomatisasi](collections/03-ai-data-and-automation/README.md) | 11 | 18 |
| [Panduan dan utilitas Windows](collections/04-windows-guides/README.md) | 7 | 7 |
| [Sistem operasi & privasi](collections/05-operating-systems-and-privacy/README.md) | 4 | 4 |
| [Kustomisasi Spotify](collections/06-spotify-customization/README.md) | 4 | 23 |
| [Alat media sosial](collections/07-social-media-tools/README.md) | 2 | 2 |
| [Riset keamanan & OSINT](collections/08-security-research/README.md) | 3 | 20 |
| [Sumber daya developer & arsip profil](collections/09-developer-resources/README.md) | 2 | 2 |
| [Alat musik](collections/10-music-tools/README.md) | 1 | 1 |
| [Hardware & IoT](collections/11-hardware-iot/README.md) | 2 | 2 |

## Cara mengakses proyek

1. Pilih salah satu kategori pada tabel di atas.
2. Pilih **folder proyek** (misalnya `Flask-Web-App`, `Python`, `FlappyGhost`, atau `Raspberry-Pi-GPIO`).
3. Buka kode dan aset di dalam folder proyek. Path relatif antarkode proyek asal dipertahankan.

**[Lihat semua folder proyek](collections/README.md)** · **[Katalog 193 file berdasarkan jenis](collections/navigasi-file/README.md)**

Contoh struktur:

```text
sandbox_projects/
├── collections/
│   ├── 01-programming-languages/
│   │   ├── CPP/
│   │   ├── Python/
│   │   └── Flask-Web-App/
│   ├── 03-ai-data-and-automation/
│   │   ├── Email-Automation/
│   │   └── Pandas-Data-Processing/
│   ├── 08-security-research/
│   │   ├── uDork/
│   │   └── Python-Port-Scanner/
│   └── ... 8 kategori lainnya
├── scripts/                # Alat pengelolaan repository
├── .github/workflows/      # Pemeriksaan otomatis
└── README.md
```

## Integritas dan cadangan

- Semua file proyek ditempatkan secara fisik dalam folder kategori/proyek. **Tidak ada lagi skrip yang tercecer di halaman utama.**
- Sembilan skrip proyek kecil dipisahkan menurut fungsinya; salinan kembar pada root dan folder `sandbox_projects` yang lama dirapikan tanpa mengganti isi file.
- `collections/manifest.json` dan `collections/sync-report.json` merupakan **catatan impor historis** dari 40 repository. Setelah repository asal dihapus, proses impor ulang tidak lagi otomatis.
- Cadangan mirror Git lengkap yang dibuat pengguna sebelumnya tetap terpisah di komputer lokal. Perubahan struktur ini bisa ditelusuri melalui riwayat commit.
- Repository website lain, termasuk Portfolio dan LANDLORD, tidak disentuh.

## Penggunaan lokal

```bash
git clone https://github.com/lamberthrumpaidus/sandbox_projects.git
cd sandbox_projects
```
