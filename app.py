import streamlit as st
from data import kolom, show_data, load_data, filter_data, select_year, pie_chart

def judul():
    st.title("〽️Dashboard COVID-19")
    st.write("Selamat datang di dashboard Covid-19! disini anda dapat melihat data")
    st.markdown("---")
    st.write("© 2026 dzihni argahnan nabila")

# sidebar
st.sidebar.title("Navigasi")
menu = st.sidebar.radio("Pilih Halaman", ["Home", "Halaman Data"])

# HALAMAN HOME
if menu == "Home":
    judul()
    year = select_year()
    df = load_data()
    df_filtered = filter_data(df, year)
    kolom(df_filtered)
    pie_chart(df_filtered)
    
# HALAMAN DATA
elif menu == "Halaman Data":
    judul()
    year = select_year()
    df = load_data()
    df_filtered = filter_data(df, year)
    show_data(df_filtered)