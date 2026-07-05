# Import libraries

import streamlit as st

from utils.load_data import load_data

from utils.theme import apply_theme 

from utils.sidebar import show_sidebar

from utils.kpi_cards import show_dashboard_kpis
# Configure Streamlit page

st.set_page_config(

    page_title="Retail Banking Analytics",

    page_icon="🏦",

    layout="wide"

)

apply_theme()

show_sidebar()
# Load all datasets

data = load_data()

account = data["account"]

client = data["client"]

district = data["district"]

disposition = data["disposition"]

card = data["card"]

loan = data["loan"]

orders = data["orders"]

transactions = data["transactions"]


# Main title

st.title("🏦 Retail Banking Analytics Portal")

st.markdown("---")


# Welcome section

st.header("Welcome")

st.write("""

Welcome to the **Retail Banking Analytics Portal**.

This application provides interactive dashboards, customer analytics, loan risk analysis, predictive modeling, and forecasting for retail banking data.

Use the navigation menu on the left to explore the project.

""")


st.markdown("---")


# Project modules

st.subheader("Project Modules")


col1, col2, col3 = st.columns(3)

with col1:

    st.info("📊 Executive Dashboard")

with col2:

    st.info("👥 Customer Segmentation")

with col3:

    st.info("⚠️ Loan Risk Analysis")


col4, col5, col6 = st.columns(3)

with col4:

    st.info("🤖 Loan Prediction")

with col5:

    st.info("📈 Forecasting")

with col6:

    st.info("ℹ️ About Project")


st.markdown("---")


# Dataset information

# Display KPI cards

show_dashboard_kpis(

    total_customers=len(client),

    total_accounts=len(account),

    total_loans=len(loan),

    total_transactions=len(transactions)

)


st.markdown("---")


# Technologies

st.subheader("Technologies Used")

st.write("""

- SQL Server

- Python

- Pandas

- Plotly

- Scikit-learn

- Streamlit

- Power BI

""")


st.markdown("---")


st.success("Use the sidebar to open the analytics pages.")