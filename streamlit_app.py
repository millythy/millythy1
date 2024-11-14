import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("Millythy Christy Kakisina")
st.write("22220012")

import streamlit as st
import pandas as pd

# Judul halaman
st.title("Visualisasi Dataset Brain Stroke (Numerik Saja)")

# Input untuk mengunggah dataset (file CSV)
uploaded_file = st.file_uploader("Upload file Brain Stroke CSV", type=["csv"])

# Memproses file yang diunggah
if uploaded_file is not None:
    # Membaca dataset CSV
    df = pd.read_csv(uploaded_file)
    
    # Menampilkan data yang dimuat
    st.write("Data yang dimuat:")
    st.write(df.head())

    # Filter hanya kolom numerik yang bisa dipilih
    numeric_columns = df.select_dtypes(include=['number']).columns.tolist()

    if len(numeric_columns) > 0:
        # Input multi-select untuk memilih kolom numerik yang ingin divisualisasikan
        selected_columns = st.multiselect(
            "Pilih kolom numerik untuk divisualisasikan",
            options=numeric_columns,
            default=numeric_columns  # Secara default memilih semua kolom numerik
        )

        # Loop untuk menampilkan setiap kolom yang dipilih di grafik yang berbeda
        for col in selected_columns:
            st.markdown(f"### Grafik untuk Kolom: {col}")
            st.line_chart(df[col])  # Menggunakan grafik garis sebagai contoh

    else:
        st.warning("Tidak ada kolom numerik yang ditemukan di dataset ini.")
else:
    st.write("Silakan unggah file CSV untuk memulai.")