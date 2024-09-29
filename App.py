import numpy as np
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

@st.cache_data
def load_data():
    data = pd.read_csv('Cleaned.csv')
    return data

data = load_data()

cities = data['Location'].unique()  

# User selects a city from dropdown menu
city = st.selectbox("Select a city", cities)

city_data = data[data['Location'] == city]

city_data_by_year = city_data.groupby('year', as_index=False).sum()

st.subheader(f"Rainfall over the Years in {city} ")
fig1, ax1 = plt.subplots(figsize=(8, 6))
ax1.plot(city_data_by_year['year'], city_data_by_year['Rainfall'], marker='o', color='blue')
ax1.set_xlabel('Year')
ax1.set_ylabel('Rainfall (mm)')
ax1.set_title(f"Rainfall Trend Over the Years in {city} ")
st.pyplot(fig1)

sorted_city_data = city_data_by_year.sort_values(by='Rainfall', ascending=False)
st.subheader(f"Years with the Highest Rainfall in {city} ")
fig2, ax2 = plt.subplots(figsize=(8, 6))
top_10_years = sorted_city_data.head(10)
ax2.bar(top_10_years['year'], top_10_years['Rainfall'], color='green')
plt.xticks(np.arange(2009, 2018, 1))
ax2.set_xlabel('Year')
ax2.set_ylabel('Rainfall (mm)')
ax2.set_title(f"Top 10 Years with the Highest Rainfall in {city} ")
st.pyplot(fig2)

# Visualization 3: Histogram of Rainfall Distribution
st.subheader(f"Histogram of Rainfall in {city} ")
fig3, ax3 = plt.subplots(figsize=(8, 6))
ax3.hist(city_data['Rainfall'], color='purple')  
ax3.set_xlabel('Rainfall (mm)')
ax3.set_ylabel('Frequency')
ax3.set_title(f"Rainfall Distribution in {city} ")
st.pyplot(fig3)

st.subheader(f"Proportion of Rainy vs Dry Days in {city} ")
rainy_days = city_data[city_data['Rainfall'] > 0].shape[0]
dry_days = city_data[city_data['Rainfall'] == 0].shape[0]
labels = ['Rainy Days', 'Dry Days']
sizes = [rainy_days, dry_days]
fig4, ax4 = plt.subplots(figsize=(6, 6))
ax4.pie(sizes, labels=labels, autopct='%1.1f%%', colors=['skyblue', 'lightgrey'], startangle=90)
ax4.axis('equal') 
ax4.set_title(f"Proportion of Rainy vs Dry Days in {city} ")
st.pyplot(fig4)
