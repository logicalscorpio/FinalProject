import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler, LabelEncoder

model_path = 'D:/IBM Data Scientist/FinalProject/saved_models/xgb_model.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)

st.title("Tomorrow's Rain Prediction")

st.sidebar.header("Enter Feature Values:")
location = st.sidebar.selectbox("Location", [
    'Cobar', 'CoffsHarbour', 'Moree', 'NorfolkIsland', 'Sydney', 'SydneyAirport',
    'WaggaWagga', 'Williamtown', 'Canberra', 'Sale', 'MelbourneAirport',
    'Melbourne', 'Mildura', 'Portland', 'Watsonia', 'Brisbane', 'Cairns',
    'Townsville', 'MountGambier', 'Nuriootpa', 'Woomera', 'PerthAirport',
    'Perth', 'Hobart', 'AliceSprings', 'Darwin'
])
min_temp = st.sidebar.number_input("MinTemp", value=20.0)
max_temp = st.sidebar.number_input("MaxTemp", value=30.0)
rainfall = st.sidebar.number_input("Rainfall", min_value=0.0, max_value=500.0, value=0.0)
evaporation = st.sidebar.number_input("Evaporation", value=5.0)
sunshine = st.sidebar.number_input("Sunshine", value=8.0)
wind_gust_dir = st.sidebar.selectbox("WindGustDir", ['SSW', 'S', 'NNE', 'WNW', 'N', 'SE', 'ENE', 'NE', 'E', 'SW', 'W', 'WSW', 'NNW', 'ESE', 'SSE', 'NW'])
wind_gust_speed = st.sidebar.number_input("WindGustSpeed", min_value=0.0, max_value=200.0, value=30.0)
wind_dir_9am = st.sidebar.selectbox("WindDir9am", ['ENE', 'SSE', 'NNE', 'WNW', 'NW', 'N', 'S', 'SE', 'NE', 'W', 'SSW', 'E', 'NNW', 'ESE', 'WSW', 'SW'])
wind_dir_3pm = st.sidebar.selectbox("WindDir3pm", ['SW', 'SSE', 'NNW', 'WSW', 'WNW', 'S', 'ENE', 'N', 'SE', 'NNE', 'NW', 'E', 'ESE', 'NE', 'SSW', 'W'])
wind_speed_9am = st.sidebar.number_input("WindSpeed9am", min_value=0.0, max_value=150.0, value=10.0)
wind_speed_3pm = st.sidebar.number_input("WindSpeed3pm", min_value=0.0, max_value=150.0, value=15.0)
humidity_9am = st.sidebar.number_input("Humidity9am", min_value=0.0, max_value=100.0, value=50.0)
humidity_3pm = st.sidebar.number_input("Humidity3pm", min_value=0.0, max_value=100.0, value=50.0)
pressure_9am = st.sidebar.number_input("Pressure9am", min_value=900.0, max_value=1100.0, value=1010.0)
cloud_9am = st.sidebar.number_input("Cloud9am", min_value=0.0, max_value=9.0, value=5.0)
cloud_3pm = st.sidebar.number_input("Cloud3pm", min_value=0.0, max_value=9.0, value=5.0)
rain_today = st.sidebar.selectbox("RainToday", ['No', 'Yes'])
day = st.sidebar.number_input("Day", min_value=1, max_value=31, value=1)
month = st.sidebar.number_input("Month", min_value=1, max_value=12, value=1)
year = st.sidebar.number_input("Year", min_value=2000, max_value=2024, value=2024)

input_data = pd.DataFrame({
    'Location': [location],
    'MinTemp': [min_temp],
    'MaxTemp': [max_temp],
    'Rainfall': [rainfall],
    'Evaporation': [evaporation],
    'Sunshine': [sunshine],
    'WindGustDir': [wind_gust_dir],
    'WindGustSpeed': [wind_gust_speed],
    'WindDir9am': [wind_dir_9am],
    'WindDir3pm': [wind_dir_3pm],
    'WindSpeed9am': [wind_speed_9am],
    'WindSpeed3pm': [wind_speed_3pm],
    'Humidity9am': [humidity_9am],
    'Humidity3pm': [humidity_3pm],
    'Pressure9am': [pressure_9am],
    'Cloud9am': [cloud_9am],
    'Cloud3pm': [cloud_3pm],
    'RainToday': [rain_today],
    'day': [day],
    'month': [month],
    'year': [year]
})

le = LabelEncoder()

for col in ['Location', 'WindGustDir', 'WindDir9am', 'WindDir3pm', 'RainToday']:
    input_data[col] = le.fit_transform(input_data[col])

sc = StandardScaler()
scaled_cols = ['MinTemp', 'MaxTemp', 'Evaporation', 'Sunshine', 'WindGustSpeed', 'WindSpeed9am', 'WindSpeed3pm', 'Humidity9am', 'Humidity3pm', 'Pressure9am']
input_data[scaled_cols] = sc.fit_transform(input_data[scaled_cols])

prediction = model.predict(input_data)

st.subheader("Will it rain tomorrow?")
st.write("Yes" if prediction[0] == 1 else "No")  # Default value is "No"
