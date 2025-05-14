import streamlit as st
import joblib
import numpy as np

st.title("Crop Yield Prediction")
model = joblib.load("models/trained_model.pkl")

ndvi = st.slider("NDVI", 0.1, 1.0, 0.5)
rainfall = st.number_input("Rainfall (mm)", value=100)
temperature = st.number_input("Avg Temperature (°C)", value=25)

features = np.array([[ndvi, rainfall, temperature]])
if st.button("Predict Yield"):
    yield_prediction = model.predict(features)
    st.success(f"Predicted Yield: {yield_prediction[0]:.2f} tons/hectare")
