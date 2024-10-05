import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load Data
day_df = pd.read_csv('day.csv')
hour_df = pd.read_csv('/content/drive/MyDrive/Bike-sharing-dataset/hour.csv')

# Clean Data (implement your cleaning steps here)

# Question 1 Visualization
st.subheader("Relationship Between Temperature and Bike Rentals")
correlation = day_df['temp'].corr(day_df['cnt'])
st.write(f'Correlation: {correlation:.2f}')

fig1, ax1 = plt.subplots()
sns.scatterplot(x='temp', y='cnt', data=day_df, ax=ax1)
ax1.set_title('Hubungan Suhu dan Jumlah Peminjaman Sepeda')
ax1.set_xlabel('Suhu')
ax1.set_ylabel('Jumlah Peminjaman Sepeda')
st.pyplot(fig1)

# Question 2 Visualization
st.subheader("Hourly Bike Rental Patterns")
fig2, ax2 = plt.subplots()
sns.lineplot(data=hour_df, x='hr', y='cnt', ci=None, ax=ax2)
ax2.set_title('Pola Peminjaman Sepeda Berdasarkan Jam dalam Sehari')
ax2.set_xlabel('Jam (0-23)')
ax2.set_ylabel('Jumlah Peminjaman Sepeda')
st.pyplot(fig2)

# Additional Analysis for Question 2
st.subheader("Hourly Patterns Based on Weekdays")
fig3, ax3 = plt.subplots()
sns.lineplot(data=hour_df, x='hr', y='cnt', hue='weekday', palette='tab10', ax=ax3)
ax3.set_title('Pola Peminjaman Sepeda Berdasarkan Jam dan Hari Kerja')
ax3.set_xlabel('Jam (0-23)')
ax3.set_ylabel('Jumlah Peminjaman Sepeda')
st.pyplot(fig3)
