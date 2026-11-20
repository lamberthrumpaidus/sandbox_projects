# uDork - Google Search Tool

Alat ini adalah skrip yang dirancang untuk melakukan pencarian Google yang canggih, mengungkapkan informasi yang tersedia secara publik, seperti dokumen, perangkat, dan rincian aplikasi web.

## Status Update

Alat ini tidak lagi berfungsi karena perubahan dalam sistem Facebook, yang mempengaruhi cara mengirim permintaan. Meskipun demikian, alat ini pernah menjadi sumber yang berharga bagi mereka yang ingin belajar tentang pengungkapan informasi sensitif di web.

## Setup Instructions:

### Step 1: Cloning the Repository

Untuk mulai menggunakan alat ini, pengguna perlu mengkloning repositori dan mengatur izin eksekusi. Berikut adalah perintah yang disediakan:
```bash
$ git clone https://github.com/lamberthrumpaidus/uDork
$ cd uDork
$ chmod +x uDork.sh
```

### Step 2: Configuration

Untuk membuat alat ini berfungsi, pengguna perlu mendapatkan cookie dari sesi Facebook yang sudah masuk. Cookie ini diperlukan untuk mengautentikasi permintaan yang dibuat oleh skrip.

### Step 3: Obtaining Cookies (with Images)

#### 3.1 - Menggunakan Firefox:
- Pertama, pengguna perlu masuk ke Facebook, lalu buka Messenger di browser yang sama.
- Kemudian, mereka akan menggunakan alat pengembang browser untuk memeriksa cookie. Dengan mengklik kanan pada halaman dan memilih "Inspect," mereka bisa mengakses tab "Network" dan mengambil nilai cookie yang diperlukan.
  

- Di bawah "Network," pengguna akan memilih baris yang terkait dengan "www.messenger.com."
- Dengan pergi ke tab "Cookies," mereka bisa menyalin nilai dari "c_user" dan "xs" dan memasukkannya ke dalam skrip.


#### 3.2 - Menggunakan Google Chrome:
- Mirip dengan Firefox, pengguna perlu mengklik kanan pada halaman dan memilih "Inspect."


- Di jendela alat pengembang, pengguna akan menavigasi ke tab "Application," lalu menemukan bagian "Cookies" untuk mengekstrak cookie yang diperlukan.


### Step 4: Running the Tool

Setelah cookie diatur dengan benar, alat dapat dijalankan menggunakan perintah:
```bash
$ ./uDork.sh -h
```
Ini akan menampilkan menu bantuan dengan berbagai opsi untuk menggunakan alat.

## Usage Overview (with Images):

### Menu:
Setelah dikonfigurasi, alat ini menawarkan beberapa opsi untuk melakukan berbagai jenis pencarian Google.


### Contoh Mencari File PDF:
Pengguna dapat mencari dokumen PDF menggunakan kueri yang sudah ditentukan.


### Contoh Mencari Ekstensi Default:
Alat ini juga memungkinkan pencarian jenis file tertentu.


### Contoh Mencari Rute yang Mengandung Kata "Password":
Contoh ini menunjukkan bagaimana pengguna bisa mencari URL yang mengandung kata kunci sensitif seperti "password."


### Daftar Dorks:
Alat ini memanfaatkan dork Google yang sudah ditentukan, yang merupakan kueri pencarian yang dirancang untuk menemukan jenis informasi tertentu.

### Contoh Pencarian Dork Massal:
Pengguna dapat melakukan pencarian skala besar menggunakan beberapa kueri sekaligus.


### Contoh Pencarian Semua Dorks (Direkomendasikan untuk Audit dan Pentesting):
Untuk pengujian penetrasi dan audit, pengguna dapat menjalankan semua dork yang tersedia.

---

### Penjelasan:
Alat **uDork** dirancang sebagai sumber yang berguna untuk menemukan informasi yang terekspos secara publik menggunakan kueri pencarian Google. Meskipun tidak lagi berfungsi karena perubahan dalam sistem Facebook, alat ini berfungsi sebagai alat pendidikan untuk hacking etis dan audit keamanan. Alat ini tidak secara langsung menyerang sistem mana pun, tetapi digunakan untuk menemukan data yang tersedia secara publik melalui teknik pencarian lanjutan.

### Pencipta: [*lamberthrumpaidus*](https://github.com/lamberthrumpaidus)
