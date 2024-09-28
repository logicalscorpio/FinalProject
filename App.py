import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
import pickle

# Load the trained model
with open('D:/IBM Data Scientist/FinalProject/saved_models/xgb_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Define a function to process user input
def process_input(user_data):
    # Convert user data to a DataFrame
    df = pd.DataFrame([user_data])
    
    # Apply LabelEncoder for categorical variables
    label_encoder = LabelEncoder()
    
    # Example mapping of categorical features (this needs to be consistent with your training data)
    df['WindGustDir'] = label_encoder.fit_transform(df['WindGustDir'])
    df['WindDir9am'] = label_encoder.fit_transform(df['WindDir9am'])
    df['WindDir3pm'] = label_encoder.fit_transform(df['WindDir3pm'])
    df['RainToday'] = label_encoder.fit_transform(df['RainToday'])
    
    # Apply StandardScaler to numerical variables
    scaler = StandardScaler()
    
    # Numerical columns that need scaling (consistent with your model's training process)
    scaled_columns = ['MinTemp', 'MaxTemp', 'Rainfall', 'Evaporation', 'Sunshine', 'WindGustSpeed', 
                      'WindSpeed9am', 'WindSpeed3pm', 'Humidity9am', 'Humidity3pm', 'Pressure9am', 
                      'Cloud9am', 'Cloud3pm']
    
    df[scaled_columns] = scaler.fit_transform(df[scaled_columns])
    
    return df

# Example of user input data (to be replaced by actual user input)
user_input = {
    'Location': 1,
    'MinTemp': 12.5,
    'MaxTemp': 25.3,
    'Rainfall': 0.0,
    'Evaporation': 5.0,
    'Sunshine': 8.0,
    'WindGustDir': 'N',  # Needs to be converted to numerical encoding
    'WindGustSpeed': 40.0,
    'WindDir9am': 'NW',  # Needs to be converted to numerical encoding
    'WindDir3pm': 'SE',  # Needs to be converted to numerical encoding
    'WindSpeed9am': 15.0,
    'WindSpeed3pm': 20.0,
    'Humidity9am': 70,
    'Humidity3pm': 50,
    'Pressure9am': 1015.0,
    'Cloud9am': 4,
    'Cloud3pm': 3,
    'RainToday': 'No',  # Needs to be converted to numerical encoding
    'day': 28,
    'month': 9,
    'year': 2024
}

# Process the input data
processed_input = process_input(user_input)

# Make the prediction
prediction = model.predict(processed_input)

# Output the result
if prediction == 1:
    print("It will rain tomorrow.")
else:
    print("It will not rain tomorrow.")
