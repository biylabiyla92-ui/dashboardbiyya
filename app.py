import streamlit as st
from data import (
    load_data, filter_data,
    select_year, select_location,
    show_data, kolom, pie_chart,
    bar_chart_top_death, bar_chart_top_recovery,
    map_chart
)

# ======================
# HEADER
# ======================
def judul():
    st.title("〽️ Dashboard COVID-19 Indonesia")
    st.write("Dashboard interaktif untuk analisis data COVID-19 di Indonesia")
    st.markdown("---")

# ======================
# SIDEBAR
# ======================
st.sidebar.title("Navigasi")
menu = st.sidebar.radio("Pilih Halaman", ["Home", "Halaman Data"])

# ======================
# HALAMAN HOME
# ======================
if menu == "Home":
    judul()

    # load & filter
    df = load_data()
    year = select_year()
    location = select_location(df)

    df_filtered = filter_data(df, year, location)

    # METRIC
    kolom(df_filtered)

    # PIE CHART
    pie_chart(df_filtered)

    # ======================
    # BAR CHART
    # ======================
    st.subheader("📊 Top 5 Provinsi")

    st.plotly_chart(
        bar_chart_top_death(df_filtered),
        use_container_width=True
    )

    st.plotly_chart(
        bar_chart_top_recovery(df_filtered),
        use_container_width=True
    )

    # ======================
    # MAP
    # ======================
    st.subheader("🗺️ Sebaran Wilayah")
    map_chart(df_filtered)

# ======================
# HALAMAN DATA
# ======================
elif menu == "Halaman Data":
    judul()

    df = load_data()
    year = select_year()
    location = select_location(df)

    df_filtered = filter_data(df, year, location)

    show_data(df_filtered)
    