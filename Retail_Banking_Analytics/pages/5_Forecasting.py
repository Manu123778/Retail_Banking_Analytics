# Import libraries

import streamlit as st

import pandas as pd

from utils.load_data import load_data

from utils.theme import apply_theme

from utils.sidebar import show_sidebar

from utils.charts import forecasting_chart


# Configure page

st.set_page_config(

    page_title="Forecasting",

    page_icon="📈",

    layout="wide"

)


# Apply theme

apply_theme()


# Display sidebar

show_sidebar()


# Load datasets

data = load_data()

transactions = data["transactions"]


# Page title

st.title("📈 Forecasting")

st.markdown("---")



# Convert date

transactions["Date"] = pd.to_datetime(transactions["Date"])

# Create Month column

transactions["Month"] = transactions["Date"].dt.to_period("M").astype(str)

# Monthly transactions

monthly = (

    transactions

    .groupby("Month", as_index=False)["amount"]

    .sum()

)


# Display Forecast Chart

future = forecasting_chart(monthly)

st.markdown("---")

# Forecast Table

st.subheader("Next 12 Months Forecast")

st.dataframe(

    future,

    use_container_width=True,

    hide_index=True

)