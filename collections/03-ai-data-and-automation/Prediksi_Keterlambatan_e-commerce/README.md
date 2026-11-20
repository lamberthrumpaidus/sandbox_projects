# 📦 Prediksi Keterlambatan Pengiriman E-Commerce

**Big Data & Machine Learning dengan Apache Spark**

Proyek ini bertujuan untuk memprediksi apakah suatu pengiriman e-commerce akan **terlambat atau tepat waktu** menggunakan pendekatan **Big Data Analytics** dan **Machine Learning** berbasis **Apache Spark (PySpark)**.

---

## 🚀 Latar Belakang

Keterlambatan pengiriman merupakan salah satu permasalahan utama dalam sistem e-commerce yang dapat memengaruhi kepuasan pelanggan. Dengan memanfaatkan data historis pengiriman dan teknik machine learning, proyek ini mencoba membangun model prediksi keterlambatan secara efisien menggunakan pemrosesan data terdistribusi.

---

## 📊 Dataset

* **Sumber**: Kaggle – *E-Commerce Shipping Data*
* **Link**: [https://www.kaggle.com/datasets/prachi13/customer-analytics](https://www.kaggle.com/datasets/prachi13/customer-analytics)
* **File**: `Train.csv`
* **Target (Label)**: `label`

  > Merupakan hasil *rename* dari kolom `Reached.on.Time_Y.N`

Dataset disimpan di **Google Drive** dan digunakan sebagai alternatif **HDFS** untuk keperluan pemrosesan data.

---

## 🛠️ Teknologi yang Digunakan

* **Python**
* **Apache Spark (PySpark)**
* **Spark MLlib**
* **Google Colab**
* **Google Drive**
* **Pandas & Matplotlib** (visualisasi)

---

## 🔄 Alur Proses (Pipeline)

1. Load data dari Google Drive
2. Pemrosesan data terdistribusi dengan Spark
3. Exploratory Data Analysis (EDA)
4. Preprocessing & feature engineering
5. Pemodelan machine learning
6. Hyperparameter tuning
7. Evaluasi model
8. Analisis hasil prediksi

---

## 🤖 Model Machine Learning

Dua algoritma *supervised learning* digunakan dan dibandingkan:

* **Logistic Regression**
* **Random Forest Classifier**

Hyperparameter tuning dilakukan pada Random Forest menggunakan **CrossValidator** dan **ParamGridBuilder**.

---

## 📈 Evaluasi Model

* **Metrik Evaluasi**: AUC (Area Under Curve)
* Evaluasi dilakukan untuk:

  * Logistic Regression
  * Random Forest (default)
  * Random Forest (tuned)

Hasil evaluasi menunjukkan bahwa **Random Forest dengan parameter default** memberikan performa terbaik pada dataset ini.

---

## 🔍 Contoh Hasil Prediksi

Model menghasilkan output berupa:

* `label` → nilai aktual
* `prediction` → hasil prediksi model
* `probability` → tingkat keyakinan model

Hal ini membuktikan bahwa model tidak hanya dievaluasi secara numerik, tetapi juga mampu menghasilkan prediksi pada data uji.

---

## 📌 Kesimpulan

Berdasarkan hasil eksperimen, pendekatan Big Data menggunakan Apache Spark dan MLlib mampu digunakan secara efektif untuk memprediksi keterlambatan pengiriman e-commerce. Model Random Forest dengan konfigurasi default menunjukkan performa terbaik, sementara hyperparameter tuning tidak selalu meningkatkan hasil pada dataset dengan ukuran terbatas.

---

## 👤 Author

**Nama**: *Lamberth Rumpaidus*

---

## Hubungi Saya

Jika Anda memiliki pertanyaan atau perlu bantuan lebih lanjut, jangan ragu untuk menghubungi [saya](https://github.com/lamberthrumpaidus).

