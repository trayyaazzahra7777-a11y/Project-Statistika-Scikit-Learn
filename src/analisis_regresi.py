# ==============================================================================
# ANALISIS FAKTOR-FAKTOR YANG MEMPENGARUHI JUMLAH PENJUALAN PRODUK TOKOPEDIA
# MENGGUNAKAN REGRESI LINEAR BERGANDA (SCIKIT-LEARN)
# ==============================================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from matplotlib.widgets import Button

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

# ==============================================================================
# PENGATURAN TAMPILAN
# ==============================================================================

sns.set_theme(style="whitegrid")

plt.rcParams["figure.figsize"] = (11, 7)
plt.rcParams["font.size"] = 11

# ==============================================================================
# MEMBACA DATASET
# ==============================================================================

print("Memuat dataset...")

df = pd.read_csv("Dataset/products.csv")

print("\nDataset berhasil dimuat")
print(f"Jumlah Data : {len(df)}")

# ==============================================================================
# MEMBERSIHKAN DATA
# ==============================================================================

df["discount_percent"] = (
    df["discount_percent"]
    .fillna("0%")
    .astype(str)
    .str.replace("%", "", regex=False)
    .astype(float)
)

df = df.dropna(subset=[
    "price",
    "discount_percent",
    "review_count",
    "rating",
    "sold_count"
])

# ==============================================================================
# FITUR DAN TARGET
# ==============================================================================

features = [
    "price",
    "discount_percent",
    "review_count",
    "rating"
]

target = "sold_count"

X = df[features]
y = df[target]

# ==============================================================================
# SPLIT DATA
# ==============================================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ==============================================================================
# MEMBANGUN MODEL REGRESI
# ==============================================================================

model = LinearRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

# ==============================================================================
# EVALUASI MODEL
# ==============================================================================

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("\n==============================")
print("HASIL REGRESI")
print("==============================")
print(f"Jumlah Data      : {len(df)}")
print(f"Jumlah Parameter : {len(features)}")
print(f"MAE  : {mae:.4f}")
print(f"RMSE : {rmse:.4f}")
print(f"R²   : {r2:.4f}")

# ==============================================================================
# KOEFISIEN REGRESI
# ==============================================================================

coef_df = pd.DataFrame({
    "Faktor": features,
    "Koefisien": model.coef_
})

coef_df = coef_df.sort_values(
    by="Koefisien",
    ascending=False
)

pd.set_option(
    "display.float_format",
    "{:.12f}".format
)

print("\nKoefisien Regresi")
print(coef_df)

# ==============================================================================
# KORELASI
# ==============================================================================

corr_matrix = df[
    features + [target]
].corr()

# ==============================================================================
# RESIDUAL
# ==============================================================================

residual = y_test - y_pred

# ==============================================================================
# VISUALISASI INTERAKTIF
# ==============================================================================

current_plot = [0]

fig, ax = plt.subplots()

plt.subplots_adjust(bottom=0.22)

# ==============================================================================
# FUNGSI GAMBAR
# ==============================================================================

def draw_plot(index):

    ax.clear()

    # --------------------------------------------------------------------------
    # GRAFIK 1 : HEATMAP KORELASI
    # --------------------------------------------------------------------------

    if index == 0:

        sns.heatmap(
            corr_matrix,
            annot=True,
            cmap="coolwarm",
            fmt=".2f",
            ax=ax
        )

        ax.set_title(
            "Grafik 1 dari 4\nHeatmap Korelasi Antar Variabel",
            fontsize=15,
            fontweight="bold"
        )

    # --------------------------------------------------------------------------
    # GRAFIK 2 : KOEFISIEN REGRESI
    # --------------------------------------------------------------------------

    elif index == 1:

        bars = ax.barh(
            coef_df["Faktor"],
            coef_df["Koefisien"]
        )

        for bar in bars:

            width = bar.get_width()

            ax.text(
                width,
                bar.get_y() + bar.get_height()/2,
                f"{width:.3f}",
                va="center"
            )

        ax.set_title(
            "Grafik 2 dari 4\nPengaruh Faktor Terhadap Penjualan",
            fontsize=15,
            fontweight="bold"
        )

        ax.set_xlabel("Nilai Koefisien")

    # --------------------------------------------------------------------------
    # GRAFIK 3 : AKTUAL VS PREDIKSI
    # --------------------------------------------------------------------------

    elif index == 2:

        ax.scatter(
            y_test,
            y_pred,
            alpha=0.7
        )

        min_val = min(
            y_test.min(),
            y_pred.min()
        )

        max_val = max(
            y_test.max(),
            y_pred.max()
        )

        ax.plot(
            [min_val, max_val],
            [min_val, max_val],
            "r--",
            linewidth=2
        )

        ax.text(
            0.05,
            0.95,
            f"R² = {r2:.4f}",
            transform=ax.transAxes,
            fontsize=12,
            bbox=dict(facecolor="white")
        )

        ax.set_title(
            "Grafik 3 dari 4\nPenjualan Aktual vs Prediksi",
            fontsize=15,
            fontweight="bold"
        )

        ax.set_xlabel("Penjualan Aktual")
        ax.set_ylabel("Penjualan Prediksi")

    # --------------------------------------------------------------------------
    # GRAFIK 4 : DISTRIBUSI RESIDUAL
    # --------------------------------------------------------------------------

    elif index == 3:

        sns.histplot(
            residual,
            bins=30,
            kde=True,
            ax=ax
        )

        ax.axvline(
            0,
            color="red",
            linestyle="--",
            linewidth=2
        )

        ax.set_title(
            "Grafik 4 dari 4\nDistribusi Error (Residual)",
            fontsize=15,
            fontweight="bold"
        )

        ax.set_xlabel("Error")
        ax.set_ylabel("Frekuensi")

    fig.canvas.draw_idle()

# ==============================================================================
# TOMBOL NAVIGASI
# ==============================================================================

def next_plot(event):

    current_plot[0] = (current_plot[0] + 1) % 4

    draw_plot(current_plot[0])

def prev_plot(event):

    current_plot[0] = (current_plot[0] - 1) % 4

    draw_plot(current_plot[0])

# Tombol Sebelumnya

ax_prev = plt.axes([0.25, 0.05, 0.2, 0.08])

btn_prev = Button(
    ax_prev,
    "< Sebelumnya"
)

# Tombol Selanjutnya

ax_next = plt.axes([0.55, 0.05, 0.2, 0.08])

btn_next = Button(
    ax_next,
    "Selanjutnya >"
)

btn_prev.on_clicked(prev_plot)
btn_next.on_clicked(next_plot)

# Tampilkan grafik pertama

draw_plot(0)

plt.show()