# Penerjemahan dokumen Python

Eksperimen penerjemahan dokumen PDF menjadi DOCX.

[Profil utama](https://github.com/lamberthrumpaidus/lamberthrumpaidus) · [Indeks proyek](../../../README.md)

##  Fitur Utama

*  **Dukung PDF ke DOCX penuh halaman**
*  **Pilih bahasa dengan nama biasa**, bukan kode ISO (contoh: “Indonesia”, “Spanyol”)
*  **Penerjemahan otomatis berbasis GoogleTranslator**
*  **Pembersihan karakter aneh & retry otomatis jika gagal**
*  **Progress bar real-time per halaman (`tqdm`)**
*  **Mode interaktif & mode argumen (CLI)**

---

##  Struktur Proyek

```
Python_Translate_File/
│
├── translate_pdf_to_docx.py      # Skrip utama
├── example.pdf                   # Contoh file PDF input
├── hasil_terjemahan.docx         # Hasil terjemahan
└── README.md                     # Dokumentasi proyek
```

---

##  Instalasi

1. Pastikan Python ≥ 3.8 sudah terpasang.

2. Instal dependensi berikut:

   ```bash
   pip install PyMuPDF deep-translator python-docx tqdm
   ```

3. (Opsional) Siapkan file PDF di direktori yang sama dengan skrip.

---

##  Cara Menjalankan

###  Mode Interaktif

Langsung jalankan perintah:

```bash
python translate_pdf_to_docx.py
```

Lalu isi prompt yang muncul:

```
📂 Masukkan nama file PDF (mis. file.pdf): faludi-introducing-a-theory-of-planning
💾 Nama file output DOCX (mis. hasil_terjemahan.docx): Faludi_Terjemahan
🌍 Masukkan bahasa tujuan (contoh: Indonesia, Inggris, Jepang): Indonesia
```

Hasilnya akan tersimpan di:

```
Faludi_Terjemahan.docx
```

---

###  Mode Otomatis (CLI)

Anda juga bisa langsung tentukan argumen tanpa input manual:

```bash
python translate_pdf_to_docx.py --input faludi.pdf --output hasil.docx --lang Prancis
```

> Bahasa bisa ditulis bebas:
> `Indonesia`, `Inggris`, `Prancis`, `Spanyol`, `Jepang`, `Jerman`, `Arab`, `Mandarin`, `Korea`, dll.

---

##  Contoh Hasil

**Input (Bahasa Inggris):**

```
Planning theory explains how decisions are made and justified.
```

**Output (Bahasa Indonesia):**

```
Teori perencanaan menjelaskan bagaimana keputusan dibuat dan dibenarkan.
```

---

##  Bahasa yang Didukung

| Bahasa              | Penulisan                         | Kode Otomatis |
| :------------------ | :-------------------------------- | :------------ |
| Indonesia           | `Indonesia`, `Bahasa Indonesia`   | `id`          |
| Inggris             | `Inggris`, `English`              | `en`          |
| Prancis             | `Prancis`, `French`               | `fr`          |
| Spanyol             | `Spanyol`, `Spanish`              | `es`          |
| Jepang              | `Jepang`, `Japanese`              | `ja`          |
| Jerman              | `Jerman`, `German`                | `de`          |
| Arab                | `Arab`, `Arabic`                  | `ar`          |
| Korea               | `Korea`, `Korean`                 | `ko`          |
| Mandarin / Tiongkok | `Mandarin`, `Chinese`, `Tiongkok` | `zh-cn`       |

> Jika bahasa tidak dikenali, sistem otomatis memilih Bahasa Indonesia.

---

##  Catatan Penting

* Pastikan file PDF **berisi teks yang dapat diekstrak** (bukan hasil scan).
* Gunakan koneksi internet yang stabil agar proses terjemahan tidak terputus.
* File besar (100+ halaman) disarankan dijalankan bertahap untuk menghindari timeout.
* Sistem otomatis melakukan **retry hingga 3 kali** jika koneksi terputus.

---

##  Teknologi yang Digunakan

| Library                                | Fungsi                                     |
| :------------------------------------- | :----------------------------------------- |
| **PyMuPDF (fitz)**                     | Membaca dan mengekstrak teks dari file PDF |
| **Deep Translator (GoogleTranslator)** | Melakukan penerjemahan teks                |
| **python-docx**                        | Menulis hasil terjemahan ke file Word      |
| **tqdm**                               | Menampilkan progress bar selama proses     |

---

##  Lisensi

Proyek ini dirilis di bawah **MIT License**.
Silakan gunakan, modifikasi, atau sebarkan dengan tetap mencantumkan atribusi pembuat.
