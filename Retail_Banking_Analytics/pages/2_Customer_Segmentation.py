# Import libraries

import streamlit as st

from utils.load_data import load_data

from utils.theme import apply_theme

from utils.sidebar import show_sidebar

from utils.kpi_cards import show_customer_kpis

from utils.charts import (

    age_distribution_chart,

    gender_distribution_chart,

    balance_by_age_chart

)

# Configure page

st.set_page_config(

    page_title="Customer Segmentation",

    page_icon="👥",

    layout="wide"

)


# Apply application theme

apply_theme()


# Display sidebar

show_sidebar()


# Load datasets

data = load_data()

client = data["client"]

account = data["account"]

transactions = data["transactions"]

loan = data["loan"]


# Create customer master table

customer = (
    client
    .merge(account, on="district_id", how="left")
    .merge(transactions.groupby("account_id", as_index=False)["balance"].mean(), on="account_id", how="left")
    .merge(loan.groupby("account_id", as_index=False)["amount"].sum(), on="account_id", how="left")
)

# Create age column

# Birth year (first 2 digits)
customer["Birth_Year"] = customer["birth_number"] // 10000

# Convert to 4-digit year
customer["Birth_Year"] = customer["Birth_Year"].apply(
    lambda x: 1900 + x if x > 25 else 2000 + x
)

# Age
customer["Age"] = 2026 - customer["Birth_Year"]

# Gender (month > 50 means Female)
customer["Gender"] = (
    ((customer["birth_number"] // 100) % 100 > 50)
    .astype(int)
)

# Replace missing values

customer["balance"] = customer["balance"].fillna(0)

customer["amount"] = customer["amount"].fillna(0)

# Page title

st.title("👥 Customer Segmentation")

st.markdown("---")

# Display customer KPI cards

show_customer_kpis(

    total_customers=customer["client_id"].nunique(),

    average_age=customer["Age"].mean(),

    average_balance=customer["balance"].mean(),

    total_loan_amount=customer["amount"].sum()

)

st.markdown("---")



# Display customer charts

col1, col2 = st.columns(2)

with col1:
    age_distribution_chart(customer)

with col2:
    gender_distribution_chart(customer)

st.markdown("---")

balance_by_age_chart(customer)