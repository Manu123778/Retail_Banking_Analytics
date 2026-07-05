from pathlib import Path
import pandas as pd
import streamlit as st

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"


@st.cache_data
def load_data():

    account = pd.read_csv(DATA_DIR / "account.csv")
    client = pd.read_csv(DATA_DIR / "client.csv")
    district = pd.read_csv(DATA_DIR / "district.csv")
    disposition = pd.read_csv(DATA_DIR / "disposition.csv")
    card = pd.read_csv(DATA_DIR / "card.csv")
    loan = pd.read_csv(DATA_DIR / "loan.csv")
    orders = pd.read_csv(DATA_DIR / "orders.csv")
    transactions = pd.read_csv(DATA_DIR / "transactions.csv")

    return {
        "account": account,
        "client": client,
        "district": district,
        "disposition": disposition,
        "card": card,
        "loan": loan,
        "orders": orders,
        "transactions": transactions,
    }
