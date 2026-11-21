# Kustomisasi klien Spotify

Dokumentasi eksperimen modifikasi antarmuka Spotify.

[Profil utama](https://github.com/lamberthrumpaidus/lamberthrumpaidus) · [Indeks proyek](../../../README.md)

## Tampilan Aplikasi
<div align="center">
  <img src="Screenshot 2026-05-04 110120.png" width="800" alt="Spotify AdBlock Preview" style="border: 2px solid #3b82f6; border-radius: 10px;">
  <p><i>Adblock by Lamberth Rumpaidus telah terpasang dan aktif sempurna</i></p>
</div>

---

## Fitur Utama
Ekstensi ini dirancang khusus untuk memodifikasi client Spotify Desktop melalui Spicetify dengan fitur:

*  **Blokir Iklan Audio:** Menghilangkan jeda iklan suara antar lagu secara otomatis.
*  **Bersihkan Iklan Visual:** Menghapus banner, sponsor, dan leaderboard yang mengganggu pemandangan.
*  **Premium UI Look:** Menghilangkan tombol "Upgrade" dan "Explore Premium" agar tampilan akun terlihat seperti Premium.
*  **Esperanto Engine Support:** Menggunakan manipulasi modul Webpack terbaru untuk stabilitas pada Spotify versi terbaru.

---

## Persyaratan Sistem
1. **Spotify Desktop** (Versi resmi dari Spotify.com, bukan versi Microsoft Store).
2. **Spicetify CLI** terpasang. [Cara Install Spicetify](https://spicetify.app/docs/getting-started).

---

## Panduan Instalasi

### 1. Simpan File Script
Unduh file `adblock.js` dan letakkan di folder ekstensi Spicetify Anda:
* **Windows:** `%AppData%\spicetify\Extensions\`
* **Mac/Linux:** `~/.config/spicetify/Extensions/`

### 2. Aktifkan via Terminal
Buka PowerShell atau CMD, lalu jalankan perintah berikut secara berurutan:

```powershell
# Mendaftarkan script ke dalam konfigurasi
spicetify config extensions adblock.js

# Mengaktifkan Developer Tools (Opsional, untuk cek status)
spicetify config devtools 1

# Terapkan perubahan
spicetify apply
```

### 3. Pembersihan Cache (Langkah Penting)
Jika iklan masih muncul, bersihkan sisa-sisa iklan di memori Spotify:
1. Log out dari Spotify.
2. Hapus folder: `%LocalAppData%\Spotify\Storage`.
3. Log in kembali.

---

## Cara Cek Status
Setelah Spotify terbuka, tekan tombol **`Ctrl + Shift + I`**. Klik pada tab **Console**. Jika berhasil, Anda akan melihat pesan:
> `Adblock oleh Lamberth Rumpaidus: Aktif`

---

## Lisensi & Disclaimer
Proyek ini dibuat untuk tujuan edukasi. Penggunaan script modifikasi pada pihak ketiga merupakan tanggung jawab pengguna masing-masing.

---
**Build with Power by Lamberth Rumpaidus**
---
