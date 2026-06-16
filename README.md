## Identitas
* **Nama** : [Trayya Azzahra Baso]
* **NIM** : [F5512520100]
* **Program Studi** : [Teknik Informatika]
* **Kelas** : [C]

---

# Analisis Faktor Prediksi Penjualan Produk E-Commerce (Tokopedia)

Sebuah proyek *Data Science* dan Pemodelan Statistik untuk menganalisis faktor-faktor yang paling mempengaruhi jumlah penjualan produk di platform e-commerce menggunakan algoritma **Multiple Linear Regression**.

---

## Deskripsi Proyek
Fenomena *imbalanced data* pada sistem rating e-commerce di Indonesia membuat variabel "Rating" tidak lagi cukup untuk memprediksi kesuksesan suatu produk. Proyek ini bertujuan untuk membangun model regresi matematis yang dapat membuktikan secara statistik seberapa besar pengaruh **Harga, Persentase Diskon, Jumlah Ulasan, dan Rating** terhadap total produk yang terjual (*Sold Count*).

---

## 📊 Informasi Dataset
Data yang digunakan adalah data sekunder berupa sampel produk riil dari platform e-commerce. 

* **Sumber Referensi & Lisensi Data:**
  > Fiki Pratama. (2025). *Tokopedia Products Dataset (2025)* [Data set]. Kaggle. https://doi.org/10.34740/kaggle/ds/9118061

| Atribut | Keterangan |
| :--- | :--- |
| **Jumlah Sampel** | 1.200 baris data produk |
| **Variabel Dependen (Y)** | `sold_count` (Total Penjualan) |
| **Variabel Independen (X)**| `price`, `discount_percent`, `review_count`, `rating` |

---

## Hasil & Kesimpulan Utama
Berdasarkan pengujian menggunakan pustaka `scikit-learn`, model regresi berhasil dievaluasi dengan hasil yang sangat baik:

* **Akurasi Model (R-Squared): `0.9396`**
  Artinya, 93.96% variasi jumlah penjualan produk dapat dijelaskan secara akurat oleh keempat faktor di atas secara bersama-sama.
* **Faktor Paling Berpengaruh:**
  Berdasarkan analisis koefisien dan *Feature Importance*, variabel **Jumlah Ulasan (`review_count`)** merupakan pendorong utama (faktor paling signifikan) yang membuat sebuah produk laris terjual di platform Tokopedia.

---

## Struktur Repositori
Proyek ini menggunakan arsitektur modular standar *Data Science*:

> ```text
> 📁 PROJECT
> ┣ 📂 Dataset
> ┃ ┗ 📄 products.csv               # Data mentah
> ┣ 📂 Notebook
> ┃ ┗ 📓 analisis_regresi.ipynb      # Eksplorasi Data (EDA) & Visualisasi
> ┣ 📂 src
> ┃ ┗ 🐍 analisis_regresi.py         # Source code utama (Production)
> ┗ 📄 requirements.txt              # Daftar library yang dibutuhkan
> ```

---

## Cara Menjalankan Proyek Secara Lokal

1. **Clone Repositori Ini**
    ```bash
    git clone [https://github.com/trayyaazzahra7777-a11y/Project-Statistika-Scikit-Learn]

2. **Install Dependencies**
Pastikan Python sudah terinstal, lalu jalankan perintah ini di terminal:
    ```bash
    pip install -r requirements.txt

3. **Eksekusi Program**
    Untuk melihat proses interaktif dan grafik: Buka folder Notebook dan jalankan analisis_regresi.ipynb.

    Untuk menjalankan script secara otomatis: Buka terminal dan jalankan python src/analisis_regresi.py.