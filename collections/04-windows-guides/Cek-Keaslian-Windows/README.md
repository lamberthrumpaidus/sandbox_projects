# Cara Mengecek Keaslian Windows

Panduan ini menjelaskan cara mengecek apakah Windows yang Anda gunakan asli atau tidak.

## Menggunakan Command Prompt (CMD)

1. Tekan tombol **Windows + R** untuk membuka jendela Run.
2. Ketik `cmd` dan tekan Enter.
3. Di jendela CMD, ketik perintah berikut dan tekan Enter:
   ```bash
   slmgr /xpr
   ```
4. Jika muncul pesan "The machine is permanently activated," berarti Windows Anda asli.

## Menggunakan Program Run

1. Tekan tombol **Windows + R**.
2. Ketik `slmgr.vbs /dli` dan tekan Enter.
3. Jendela Windows Script Host akan muncul. Periksa baris **Description**:
   - Jika tertulis **Volume_KMSclient**, berarti Windows diaktivasi menggunakan tool aktivator dan tidak asli.
   - Jika tertulis **Retail** atau **OEM**, berarti Windows Anda asli.

## Memeriksa Sertifikat Keaslian (COA)

1. Carilah **Sertifikat Keaslian (COA)** pada perangkat Anda. Biasanya berupa stiker dengan hologram dan kode lisensi.

## Sumber

- [BagiTekno](https://www.bagitekno.net/windows/cara-cek-windows-10-ori-atau-tidak.html)
- [DimensiData](https://blog.dimensidata.com/begini-cara-mengetahui-dan-cek-windows-10-asli-atau-bajakan/)
- [Microsoft Support](https://support.microsoft.com/id-id/windows/tentang-windows-asli-0b88ba3d-f799-7c15-9f36-2be445a56493)

