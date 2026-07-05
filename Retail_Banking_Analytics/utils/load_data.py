# Import libraries

import pandas as pd
import streamlit as st


# Load all datasets

@st.cache_data
def load_data():

    account = pd.read_csv("data/account.csv")

    client = pd.read_csv("data/client.csv")

    district = pd.read_csv("data/district.csv")

    disposition = pd.read_csv("data/disposition.csv")

    card = pd.read_csv("data/card.csv")

    loan = pd.read_csv("data/loan.csv")

    orders = pd.read_csv("data/orders.csv")

    transactions = pd.read_csv("data/transactions.csv")

    return {

        "account": account,

        "client": client,

        "district": district,

        "disposition": disposition,

        "card": card,

        "loan": loan,

        "orders": orders,

        "transactions": transactions

    }