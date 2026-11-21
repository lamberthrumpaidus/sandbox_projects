# Pengaturan folder Windows

Contoh pengaturan akses folder melalui skrip dan perintah Windows.

[Profil utama](https://github.com/lamberthrumpaidus/lamberthrumpaidus) · [Indeks proyek](../../../README.md)

## Prasyarat

* Sistem Operasi: Windows 7 / 8 / 10 / 11
* Hak akses sebagai **Administrator**
* Folder target bernama **`lam_folder`**

---

## Versi Tanpa .bat (Manual CMD)

1. Masuk ke folder yang ingin dikunci (`lam_folder`).
2. Klik **Address Bar** di bagian atas Windows Explorer.
3. Hapus teksnya lalu ketik:

   ```
   cmd
   ```

   → Tekan **Enter**, maka Command Prompt terbuka di lokasi folder.

### Lock Folder

Jalankan perintah berikut untuk mengunci:

```bat
icacls "lam_folder" /deny Everyone:(F)
```

### Unlock Folder

Jalankan perintah berikut untuk membuka kunci:

```bat
icacls "lam_folder" /grant Everyone:(F)
```

---

## Versi Dengan .bat (Script Otomatis)

### 1. Lock Folder Script

Buat file baru bernama **`lock_lam_folder_icacls.bat`** lalu isi dengan:

```bat
@echo off
title Lock lam_folder
echo Mengunci folder lam_folder dengan icacls...
icacls "lam_folder" /deny Everyone:(F)
echo Folder lam_folder berhasil dikunci!
pause
```

### 2. Unlock Folder Script

Buat file baru bernama **`unlock_lam_folder_icacls.bat`** lalu isi dengan:

```bat
@echo off
title Unlock lam_folder
echo Membuka kunci folder lam_folder dengan icacls...
icacls "lam_folder" /grant Everyone:(F)
echo Folder lam_folder berhasil dibuka!
pause
```

### Cara Menggunakan

1. Pastikan folder **`lam_folder`** sudah ada di lokasi yang sama dengan file `.bat`.
2. Klik 2x `lock_lam_folder_icacls.bat` → folder terkunci.
3. Klik 2x `unlock_lam_folder_icacls.bat` → folder terbuka kembali.

---

## Catatan Penting

* **Run as Administrator** sangat disarankan agar tidak gagal.
* Jika ingin folder selain `lam_folder`, cukup ganti nama folder di dalam kode.
* `icacls` lebih modern dan disarankan dibandingkan `cacls` (deprecated).

---
