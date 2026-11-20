# L/R — Koleksi Repository berdasarkan Kategori


## Navigasi cepat

[Buka katalog berdasarkan jenis file](navigasi-file/README.md)

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


## Menghapus repository sumber (opsional, tidak dijalankan otomatis)

Dari 40 sumber yang disalin, **38 repository biasa** memenuhi syarat untuk menjadi kandidat penghapusan. Repository pusat `sandbox_projects` dan repository profil khusus `lamberthrumpaidus` tetap dilindungi, selain ketujuh repository website. Repository profil khusus tidak boleh dihapus hanya karena `README.md`-nya sudah disalin: penghapusan akan menghilangkan tampilan profil GitHub tersebut.

Program [`scripts/prune_original_repos.py`](../scripts/prune_original_repos.py) adalah **dry-run secara default**. Dengan opsi `--execute`, program akan:
1. Membuat cadangan **full Git mirror** dari setiap repository sumber (semua commit, branch, dan tag).
2. Memeriksa tiap cadangan dengan `git fsck --full`.
3. Meminta konfirmasi ketik `HAPUS 38 REPOSITORY` sebelum menghapus sumber melalui GitHub CLI.

Contoh pada terminal lokal:

```bash
python scripts/prune_original_repos.py
python scripts/prune_original_repos.py --execute --backup-dir ./cadangan-github
```

Dibutuhkan `git`, Python 3, GitHub CLI (`gh`), dan otorisasi `delete_repo`. Cadangan mirror **tidak menyertakan issues, PR, pengaturan repository, atau tautan lama**. Simpan atau ekspor data tersebut secara terpisah jika diperlukan. Penghapusan repository tidak dapat dibatalkan secara aman hanya dengan adanya salinan berkas di koleksi.
