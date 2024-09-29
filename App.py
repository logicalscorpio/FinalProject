import numpy as np
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

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

# Plotly Visualization 1: Rainfall over the Years in the selected city
st.subheader(f"Rainfall over the Years in {city}")
fig1 = px.line(city_data_by_year, x='year', y='Rainfall', markers=True,
               title=f"Rainfall Trend Over the Years in {city}")
fig1.update_layout(xaxis_title='Year', yaxis_title='Rainfall (mm)')
st.plotly_chart(fig1)

# Plotly Visualization 2: Bar chart of Top 10 Years with Highest Rainfall
sorted_city_data = city_data_by_year.sort_values(by='Rainfall', ascending=False)
top_10_years = sorted_city_data.head(10)

st.subheader(f"Years with the Highest Rainfall in {city}")
fig2 = px.bar(top_10_years, x='year', y='Rainfall', title=f"Top 10 Years with the Highest Rainfall in {city}",
              labels={'year': 'Year', 'Rainfall': 'Rainfall (mm)'}, color='Rainfall')
fig2.update_layout(xaxis_title='Year', yaxis_title='Rainfall (mm)', xaxis=dict(tickmode='linear'))
st.plotly_chart(fig2)

# Plotly Visualization 3: Histogram of Rainfall Distribution
st.subheader(f"Histogram of Rainfall in {city}")
fig3 = px.histogram(city_data, x='Rainfall', nbins=30, title=f"Rainfall Distribution in {city}",
                    labels={'Rainfall': 'Rainfall (mm)'})
fig3.update_layout(xaxis_title='Rainfall (mm)', yaxis_title='Frequency')
st.plotly_chart(fig3)

# Plotly Visualization 4: Proportion of Rainy vs Dry Days
st.subheader(f"Proportion of Rainy vs Dry Days in {city}")
rainy_days = city_data[city_data['Rainfall'] > 0].shape[0]
dry_days = city_data[city_data['Rainfall'] == 0].shape[0]
labels = ['Rainy Days', 'Dry Days']
sizes = [rainy_days, dry_days]

fig4 = go.Figure(data=[go.Pie(labels=labels, values=sizes, hole=.3)])
fig4.update_traces(hoverinfo='label+percent', textinfo='value', marker=dict(colors=['skyblue', 'lightgrey']))
fig4.update_layout(title=f"Proportion of Rainy vs Dry Days in {city}")
st.plotly_chart(fig4)
