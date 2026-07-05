from pathlib import Path
import joblib
import streamlit as st

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_DIR = BASE_DIR / "models"

@st.cache_data
def load_model():

    model = joblib.load(MODEL_DIR / "loan_model.pkl")
    scaler = joblib.load(MODEL_DIR / "scaler.pkl")

    return model, scaler
