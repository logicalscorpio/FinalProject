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

city = st.selectbox("Select a city", cities)

city_data = data[data['Location'] == city]

city_data_by_year = city_data.groupby('year', as_index=False).sum()

st.subheader(f"Rainfall over the Years in {city}")
fig1 = px.line(city_data_by_year, x='year', y='Rainfall', markers=True,
               title=f"Rainfall Trend Over the Years in {city}")
fig1.update_layout(xaxis_title='Year', yaxis_title='Rainfall (mm)')
st.plotly_chart(fig1)

selected_var = st.radio("Select the variable to compare with Rainfall:", 
                         ("Minimum Temperature (MinTemp)", "Maximum Temperature (MaxTemp)"))

y_variable = 'MinTemp' if selected_var == "Minimum Temperature (MinTemp)" else 'MaxTemp'

st.subheader(f"Rainfall vs {selected_var} in {city}")
fig2 = px.scatter(city_data, x=y_variable, y='Rainfall', 
                   title=f"Rainfall vs {selected_var} in {city}",
                   labels={y_variable: selected_var, 'Rainfall': 'Rainfall (mm)'})
fig2.update_layout(xaxis_title=selected_var, yaxis_title='Rainfall (mm)')
st.plotly_chart(fig2)

st.subheader(f"Histogram of Rainfall in {city}")
fig4 = px.histogram(city_data, x='Rainfall', nbins=30, title=f"Rainfall Distribution in {city}",
                    labels={'Rainfall': 'Rainfall (mm)'})
fig4.update_layout(xaxis_title='Rainfall (mm)', yaxis_title='Frequency')
st.plotly_chart(fig4)

st.subheader(f"Proportion of Rainy vs Dry Days in {city}")
rainy_days = city_data[city_data['Rainfall'] > 0].shape[0]
dry_days = city_data[city_data['Rainfall'] == 0].shape[0]
labels = ['Rainy Days', 'Dry Days']
sizes = [rainy_days, dry_days]

fig5 = go.Figure(data=[go.Pie(labels=labels, values=sizes, hole=.3)])
fig5.update_traces(hoverinfo='label+percent', textinfo='value', marker=dict(colors=['skyblue', 'lightgrey']))
fig5.update_layout(title=f"Proportion of Rainy vs Dry Days in {city}")
st.plotly_chart(fig5)
