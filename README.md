# Analisis Regresi Linear: Prediksi Penjualan Produk E-Commerce (Tokopedia)

Repositori ini berisi dokumentasi dan kode sumber untuk analisis faktor-faktor yang memengaruhi jumlah penjualan produk di Tokopedia menggunakan metode *Multiple Linear Regression*.

**Peneliti:** [Nama Kamu] | **NIM:** [NIM Kamu] | **Program Studi:** [Prodi Kamu] | [Universitas Kamu]

---

## Latar Belakang
Dalam ekosistem *e-commerce*, rating produk sering kali memiliki distribusi yang tidak merata (mayoritas produk memiliki rating tinggi), sehingga kurang ideal jika dijadikan acuan tunggal kesuksesan. Proyek ini bertujuan untuk menguji secara statistik sejauh mana **Harga, Persentase Diskon, Jumlah Ulasan, dan Rating** memengaruhi total produk yang terjual (*Sold Count*).

## Sumber Data
Data yang digunakan adalah data sekunder berupa sampel produk dari platform Tokopedia.

> **Referensi Dataset:**
> Fiki Pratama. (2025). *Tokopedia Products Dataset (2025)* [Data set]. Kaggle.  
> 🔗 **[https://doi.org/10.34740/kaggle/ds/9118061](https://doi.org/10.34740/kaggle/ds/9118061)**

| Atribut | Keterangan |
| :--- | :--- |
| **Total Observasi** | 1.200 baris data |
| **Variabel Dependen (Y)** | `sold_count` (Total produk terjual) |
| **Variabel Independen (X)**| `price`, `discount_percent`, `review_count`, `rating` |

## Temuan Utama
Model regresi yang dibangun menggunakan pustaka `scikit-learn` menghasilkan evaluasi sebagai berikut:

* **Nilai R-Squared ($R^2$): 0.9396**
  Hal ini mengindikasikan bahwa sekitar **93.96%** variasi jumlah penjualan produk dapat dijelaskan oleh keempat variabel fitur yang digunakan.
* **Variabel Paling Signifikan:**
  Berdasarkan ekstraksi koefisien model, **Jumlah Ulasan (`review_count`)** merupakan prediktor yang memberikan dampak positif paling besar terhadap jumlah barang yang terjual.

## Struktur Direktori

* 📁 **Dataset/**
  * 📄 `products.csv` — *(Data mentah)*
* 📁 **Notebook/**
  * 📓 `analisis_regresi.ipynb` — *(Eksplorasi Data (EDA) & Visualisasi)*
* 📁 **src/**
  * 🐍 `analisis_regresi.py` — *(Script utama Python)*
* 📄 `requirements.txt` — *(Daftar library yang dibutuhkan)*

## Panduan Penggunaan

**1. Akses & Clone Repositori** 🔗 **[Klik di sini untuk melihat Repositori GitHub](https://github.com/trayyaazzahra7777-a11y/Project-Statistika-Scikit-Learn)**

Atau, salin proyek ke komputer lokal menggunakan perintah terminal berikut:
```bash
git clone https://github.com/trayyaazzahra7777-a11y/Project-Statistika-Scikit-Learn