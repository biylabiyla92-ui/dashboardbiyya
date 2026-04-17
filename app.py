import streamlit as st
from data import show_data


def judul():
    st.title("〽️Dashboard COVID-19")
    st.write("Selamat datang di dashboard Covid-19! disini anda dapat melihat data")
    st.markdown("---")
    st.write("© 2026 dzihni argahnan nabila - ")
    
    
st.sidebar.title("Navigasi")
menu = st.sidebar.radio("Pilih Halaman", ["Home", "Halaman Data"])
if menu == "Home":
    judul()
elif menu == "Halaman Data":
    judul()
    show_data()

