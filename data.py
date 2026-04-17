import streamlit as st
import pandas as pd


def load_data():
     df = pd.read_csv("dataset\covid_19_indonesia_time_series_all.csv")
     return df
    
def show_data():
    df = load_data()
    st.header("🦠 Data Kasus Covid-19 DI 🔴⚪")

    # Menampilkan kolom tertentu saja
    df_filtered = df.loc[:, "Location":"Total Recovered"]
    st.dataframe(df_filtered.head(10))
    
    # Menampilkan total kasus keseluruhan
    total_kasus = df["Total Cases"].sum()
    st.subheader("Total Kasus Keseluruhan")
    st.write(total_kasus)
    
    # menampilkan statistik deskriptif dataset
    st.subheader("statistik deksriptif dataset")
    st.write(df.describe())

    # Copyright
    st.markdown("---")
    st.write("© 2026 dzihni argahnan nabila - 184240002")