import joblib
import streamlit as st


@st.cache_resource
def load_model():

    model = joblib.load("models/loan_model.pkl")

    scaler = joblib.load("models/scaler.pkl")

    return model, scaler