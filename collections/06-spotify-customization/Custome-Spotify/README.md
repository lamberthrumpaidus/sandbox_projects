# Free-Spotify

Panduan ini menjelaskan cara menginstal dan mengonfigurasi Spicetify menggunakan PowerShell di Windows.

## Prasyarat

Sebelum memulai, pastikan Anda telah menginstal:

- [Spotify](https://www.spotify.com)
- [Node.js](https://nodejs.org/) (versi terbaru yang stabil)

## Langkah-langkah Instalasi

1. **Buka PowerShell**:
   Tekan `Win + X` dan pilih `Windows PowerShell` atau `Windows Terminal`.

2. **Instal Spicetify CLI**:
   Jalankan perintah berikut untuk menginstal Spicetify CLI:
   ```powershell
   iwr -useb https://raw.githubusercontent.com/spicetify/cli/main/install.ps1 | iex
   ```

3. **Instal Resource Marketplace** (opsional):
   Jika Anda ingin menggunakan sumber daya tambahan, jalankan perintah ini:
   ```powershell
   iwr -useb https://raw.githubusercontent.com/spicetify/marketplace/main/resources/install.ps1 | iex
   ```

4. **Inisialisasi Spicetify**:
   Setelah instalasi selesai, inisialisasi Spicetify dengan perintah:
   ```powershell
   spicetify init
   ```

## Hubungi Saya

Jika Anda memiliki pertanyaan atau perlu bantuan lebih lanjut, jangan ragu untuk menghubungi [saya](https://github.com/lamberthrumpaidus).
Dengan cara ini, pengguna bisa langsung menginstal Spicetify tanpa perlu mengunduh dan menginstal manual. Pastikan juga untuk menambahkan detail tambahan jika diperlukan!
