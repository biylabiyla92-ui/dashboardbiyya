import streamlit as st
import pandas as pd
import plotly.express as px

# load data
def load_data():
    df = pd.read_csv("dataset/covid_19_indonesia_time_series_all.csv")
    return df

# filter berdasarkan tahun
def filter_data(df, year=None):
    if year:
        df = df[df['Date'].astype(str).str.contains(str(year))]
    return df

# select tahun
def select_year():
    return st.sidebar.selectbox(
        "Pilih Tahun",
        options=[None, 2020, 2021, 2022],
        format_func=lambda x: "Semua Tahun" if x is None else str(x)
    )

# tampil data
def show_data(df):
    selected_columns = ['Location'] + list(df.loc[:, 'New Cases':'Total Recovered'].columns)
    df_selected = df[selected_columns]

    st.subheader("Data Covid-19 Indonesia 🔴⚪")
    st.dataframe(df_selected.head(10))

# total kasus
def total_case(df):
    return df['Total Cases'].max()

# total kematian
def total_death(df):
    return df['Total Deaths'].max()

# total sembuh
def total_recovery(df):
    return df['Total Recovered'].max()

# tampilan kolom metric
def kolom(df):
    kasus = total_case(df)
    kematian = total_death(df)
    sembuh = total_recovery(df)

    col1, col2, col3 = st.columns(3)

    col1.metric("🟢 Total Kasus", f"{kasus/1000:,.1f}K")
    col2.metric("⚫ Total Kematian", f"{kematian/1000:,.1f}K")
    col3.metric("🟢 Total Sembuh", f"{sembuh/1000:,.1f}K")
    
    #piechart
def pie_chart(df):
    # ambil data
    total_mati = total_death(df)
    total_sembuh = total_recovery(df)

    # buat dataframe
    data = pd.DataFrame({
        'Status': ['Mati', 'Sembuh'],
        'Jumlah': [total_mati, total_sembuh]
    })

    # buat pie chart
    fig = px.pie(
        data,
        names='Status',
        values='Jumlah',
        title='Perbandingan Total Kematian dan Total Sembuh',
        hole=0.5,
        color_discrete_sequence=['#FF6B6B', '#4ECDC4']
    )

    # tampilkan
    st.plotly_chart(fig, use_container_width=True)