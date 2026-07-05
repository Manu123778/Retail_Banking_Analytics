# Import libraries

import streamlit as st

from utils.load_data import load_data

from utils.theme import apply_theme

from utils.sidebar import show_sidebar

from utils.kpi_cards import show_dashboard_kpis

from utils.charts import (
    monthly_transaction_chart,
    loan_status_chart,
    account_type_chart,
    transaction_type_chart
)


# Configure page

st.set_page_config(

    page_title="Executive Dashboard",

    page_icon="📊",

    layout="wide"

)


# Apply application theme

apply_theme()


# Display sidebar

show_sidebar()


# Load all datasets

data = load_data()

account = data["account"]

client = data["client"]

loan = data["loan"]

transactions = data["transactions"]


# Dashboard title

st.title("📊 Executive Dashboard")

st.markdown("---")


# Display KPI cards

show_dashboard_kpis(

    total_customers=len(client),

    total_accounts=len(account),

    total_loans=len(loan),

    total_transactions=len(transactions)

)


st.markdown("---")


# Display dashboard charts

col1, col2 = st.columns(2)

with col1:

    monthly_transaction_chart(transactions)

with col2:

    loan_status_chart(loan)
    
st.markdown("---")

# Display second row of charts

col3, col4 = st.columns(2)

with col3:
    account_type_chart(account)

with col4:
    transaction_type_chart(transactions)

