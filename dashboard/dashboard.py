import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='dark')

day_df = pd.read_csv("main_data.csv")

def plot_holiday_data(df):
    pivot_table_holiday = df.pivot_table(index='holiday', values='cnt', aggfunc='sum')
    pivot_table_holiday.index = pivot_table_holiday.index.map({0: 'Hari Kerja', 1: 'Hari Libur'})

    st.subheader("Pertanyaan 1: Apakah ada perbedaan signifikan dalam jumlah penyewaan sepeda dalam satu hari tergantung pada apakah hari tersebut adalah hari libur atau bukan?")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(pivot_table_holiday.index, pivot_table_holiday['cnt'], color='skyblue')
    ax.set_title('Jumlah Penyewaan Sepeda Berdasarkan Hari Libur')
    ax.set_xlabel('Keterangan Hari')
    ax.set_ylabel('Jumlah Tersewa')
    ax.set_xticklabels(pivot_table_holiday.index, rotation=45)
    st.pyplot(fig)
    st.caption("Dalam grafik di atas, kita bisa melihat bahwa jumlah penyewaan sepeda cenderung lebih tinggi pada hari kerja dibandingkan hari libur.")

def plot_weather_data(df):
    pivot_table_weathersit = df.pivot_table(index='weathersit', values='cnt', aggfunc='sum')
    weathersit_labels = {
        1: 'Cerah',
        2: 'Berkabut',
        3: 'Cuaca Ringan',
        4: 'Cuaca Ekstrem'
    }
    pivot_table_weathersit.index = pivot_table_weathersit.index.map(weathersit_labels)

    st.subheader("Pertanyaan 2: Bagaimana kondisi cuaca (weathersit) mempengaruhi jumlah penyewaan sepeda?")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(pivot_table_weathersit.index, pivot_table_weathersit['cnt'], color='skyblue')
    ax.set_title('Jumlah Penyewaan Sepeda Berdasarkan Kondisi Cuaca')
    ax.set_xlabel('Kondisi Cuaca')
    ax.set_ylabel('Jumlah Tersewa')
    ax.set_xticklabels(pivot_table_weathersit.index, rotation=45)
    st.pyplot(fig)
    st.caption("Grafik ini menunjukkan bagaimana kondisi cuaca mempengaruhi jumlah penyewaan sepeda, dengan penyewaan cenderung lebih tinggi pada hari cerah.")

st.header("Analisis Bike Sharing Dataset")

with st.sidebar:
    st.header('Bike Sharing')
    st.caption('Tetap peduli dengan kesehatan dan lingkungan.')
    
plot_holiday_data(day_df)
plot_weather_data(day_df)

st.caption('Copyright © AdonisZK 2024')