import streamlit as st
import pandas as pd
import plotly.express as px

# ======================
# LOAD DATA
# ======================
def load_data():
    df = pd.read_csv("dataset/covid_19_indonesia_time_series_all.csv")
    return df

# ======================
# FILTER DATA (UPDATED)
# ======================
def filter_data(df, year=None, location=None):
    if year:
        df = df[df['Date'].astype(str).str.contains(str(year))]

    if location:
        df = df[df['Location'].isin(location)]

    return df

# ======================
# SELECT BOX
# ======================
def select_year():
    return st.sidebar.selectbox(
        "Pilih Tahun",
        options=[None, 2020, 2021, 2022],
        format_func=lambda x: "Semua Tahun" if x is None else str(x)
    )

# 🔥 MULTI LOCATION
def select_location(df):
    locations = sorted(df['Location'].unique())
    return st.sidebar.multiselect(
        "Pilih Provinsi",
        options=locations,
        default=locations
    )

# ======================
# DATA TABLE
# ======================
def show_data(df):
    selected_columns = ['Location'] + list(df.loc[:, 'New Cases':'Total Recovered'].columns)
    st.subheader("Data Covid-19 Indonesia 🔴⚪")
    st.dataframe(df[selected_columns].head(10))

# ======================
# AMBIL DATA TERAKHIR
# ======================
def get_last_data(df):
    return df.sort_values('Date').groupby('Location', as_index=False).last()

# ======================
# TOTAL
# ======================
def total_case(df):
    return get_last_data(df)['Total Cases'].sum()

def total_death(df):
    return get_last_data(df)['Total Deaths'].sum()

def total_recovery(df):
    return get_last_data(df)['Total Recovered'].sum()

# ======================
# METRIC
# ======================
def kolom(df):
    col1, col2, col3 = st.columns(3)

    col1.metric("🟢 Total Kasus", f"{total_case(df)/1000:,.1f}K")
    col2.metric("⚫ Total Kematian", f"{total_death(df)/1000:,.1f}K")
    col3.metric("🟢 Total Sembuh", f"{total_recovery(df)/1000:,.1f}K")

# ======================
# PIE CHART
# ======================
def pie_chart(df):
    data = pd.DataFrame({
        'Status': ['Mati', 'Sembuh'],
        'Jumlah': [total_death(df), total_recovery(df)]
    })

    fig = px.pie(
        data,
        names='Status',
        values='Jumlah',
        title='Perbandingan Total Kematian dan Total Sembuh',
        hole=0.5
    )

    st.plotly_chart(fig, use_container_width=True)

# ======================
# BAR CHART KEMATIAN
# ======================
def bar_chart_top_death(df):
    df_last = get_last_data(df)
    df_top5 = df_last.sort_values(by='Total Deaths', ascending=False).head(5)

    fig = px.bar(
        df_top5,
        x='Location',
        y='Total Deaths',
        title='Top 5 Provinsi dengan Kematian Tertinggi',
        text='Total Deaths'
    )

    return fig

# ======================
# BAR CHART SEMBUH
# ======================
def bar_chart_top_recovery(df):
    df_last = get_last_data(df)
    df_top5 = df_last.sort_values(by='Total Recovered', ascending=False).head(5)

    fig = px.bar(
        df_top5,
        x='Location',
        y='Total Recovered',
        title='Top 5 Provinsi dengan Kesembuhan Tertinggi',
        text='Total Recovered'
    )

    return fig

# ======================
# MAP CHART
# ======================
def map_chart(df):
    if df.empty:
        st.warning("Data tidak tersedia")
        return

    df_last = get_last_data(df)

    fig = px.scatter_mapbox(
        df_last,
        lat="Latitude",
        lon="Longitude",
        size="Total Cases",
        color="Total Cases",
        hover_name="Location",
        zoom=4,
        title="Sebaran COVID-19 di Indonesia"
    )

    fig.update_layout(mapbox_style="open-street-map")

    st.plotly_chart(fig, use_container_width=True)