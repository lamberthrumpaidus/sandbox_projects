# DownloadYoutube

Proyek ini adalah skrip Python untuk mengunduh video atau audio dari YouTube menggunakan `yt-dlp`.

## Fitur

- Mengunduh video dalam berbagai resolusi (4K, 2K, 1080p, 720p, 480p, 360p).
- Mengunduh audio dalam format MP3.
- Mendukung pengunduhan dari URL video individual (tidak mendukung playlist).

## Prerequisites

Sebelum menjalankan skrip ini, pastikan Anda telah menginstal:

- Python 3.x
- `yt-dlp`
- FFmpeg (untuk mengonversi audio)

## Instalasi

1. Clone repository ini:
   ```bash
   git clone https://github.com/lamberthrumpaidus/DownloadYoutube.git
   cd DownloadYoutube
   ```

2. Instal dependensi:
   ```bash
   pip install yt-dlp
   ```

3. (Opsional) Pastikan FFmpeg terinstal di sistem Anda. Anda bisa mengunduhnya dari [sini](https://ffmpeg.org/download.html).

## Cara Menggunakan

1. Jalankan skrip:
   ```bash
   python youtubedownload.py
   ```

2. Masukkan URL video YouTube yang ingin Anda unduh.

3. Pilih format yang diinginkan dari daftar yang muncul.

4. Skrip akan mengunduh video atau audio sesuai pilihan Anda.

## Contoh
```
Masukkan URL video YouTube: https://www.youtube.com/watch?v=example
Pilih format:
1. Video 4K (2160p)
2. Video 2K (1440p)
3. Video 1080p
4. Video 720p
5. Video 480p
6. Video 360p
7. Audio (mp3)
Masukkan pilihan (1/2/3/4/5/6/7): 3
```

## Hubungi Saya

Untuk informasi lebih lanjut dan pembaruan, Anda dapat menghubungi [saya](https://github.com/lamberthrumpaidus).
