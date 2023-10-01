import streamlit as st
import joblib
import pandas as pd
from sklearn.metrics import mean_squared_error
import numpy as np
# Load the saved model
loaded_model = joblib.load('local_health_model.pkl')
# Define the features for input
features = ['Hypertens', 'Anxiety', 'Asthma']
# Define the Streamlit app
st.title("Local Health Characteristics")
# Add input fields for user to enter data
Hypertens = st.slider("Hypertens", min_value=1, max_value=120, value=60)
Anxiety = st.slider("Anxiety", min_value=1, max_value=120, value=60)
Asthma = st.slider("Asthma", min_value=1, max_value=120, value=60)
# Create a DataFrame with the user input
example_data = pd.DataFrame([[Hypertens, Anxiety, Asthma]], columns=features)
# Make predictions
predicted_charges = loaded_model.predict(example_data)
# Display the prediction
st.write(f"Predicted CHD: ${predicted_CHD[0]:.0f}")
# Add calculation of Mean Squared Error (MSE) and Root Mean Squared Error (RMSE)
actual_CHD = 100 
# Replace with the actual charges if available
if actual_CHD:
    mse = mean_squared_error([actual_CHD], [predicted_CHD[0]])
    rmse = np.sqrt(mse)
    st.write(f"MSE: {mse:.2f}")
    st.write(f"RMSE: {rmse:.2f}")
else:
    st.write("Unable to calculate MSE and RMSE. Please provide CHD")