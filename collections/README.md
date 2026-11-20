# L/R — Koleksi Repository berdasarkan Kategori

Koleksi ini menyatukan **salinan file** dari 40 repository publik yang **tidak memiliki file `index.html`**. Seluruh file sumber disimpan di subfolder `collections/<kategori>/<nama-repository>/`, termasuk gambar, audio, arsip ZIP, notebook, dan berkas biner lain jika ada.

## Aturan keselamatan

- Tujuh repository website **dikecualikan sepenuhnya**: `Rubaka`, `Portfolio`, `3D-Portfolio`, `Arcade_Collection_Game`, `Omni_Science`, `pixelpay`, dan `LANDLORD`.
- Tidak ada repository sumber yang diubah, diganti nama, diarsipkan, atau dihapus.
- Setiap repository memiliki folder sendiri agar nama file sama tidak saling menimpa.
- Koleksi ini menyalin *file pada branch utama yang terdaftar*, bukan menggabungkan seluruh histori commit atau semua branch.
- File asli yang sudah berada di root `sandbox_projects` tetap dipertahankan; salinannya ditempatkan di `collections/01-programming-languages/sandbox_projects/`.
- `collections/sync-report.json` berisi jumlah file dan SHA commit sumber untuk audit hasil (dibuat setelah sinkronisasi berhasil).

## 11 kategori

| Folder | Isi | Repository |
|---|---|---:|
| `01-programming-languages` | Bahasa pemrograman, praktikum, algoritma, kalkulator | 8 |
| `02-desktop-games` | Game desktop dan proyek PlayStation sederhana | 3 |
| `03-ai-data-and-automation` | AI, data, bot, skrip unduhan dan penerjemah | 7 |
| `04-windows-guides` | Windows, konfigurasi, tutorial dan utilitas | 7 |
| `05-operating-systems-and-privacy` | Linux, macOS, perbandingan OS, Tor | 4 |
| `06-spotify-customization` | Tema, ekstensi, personalisasi Spotify | 4 |
| `07-social-media-tools` | Panduan dan alat TikTok | 2 |
| `08-security-research` | Penelitian dan alat pencarian keamanan | 1 |
| `09-developer-resources` | Lisensi dan README profil GitHub | 2 |
| `10-music-tools` | Tutorial dan alat musik | 1 |
| `11-hardware-iot` | Proyek perangkat keras/IoT | 1 |

## Cara kerja

1. Daftar sumber: `collections/manifest.json`.
2. Penyalin: `scripts/sync_collections.py`.
3. GitHub Actions mengunduh repository sumber publik pada branch yang tercantum, kemudian menyalin file berdasarkan kategori.
4. Hasilnya di-commit ke repository ini oleh `github-actions[bot]`.

**Perhatian:** jangan hapus repository asal sebelum jumlah file dan fitur yang diperlukan diverifikasi secara mandiri. Bila ada repo yang nantinya menambahkan `index.html`, penyalinan dihentikan dan repo tersebut harus dikeluarkan dari daftar.
