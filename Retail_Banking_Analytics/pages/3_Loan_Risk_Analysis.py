# Import libraries

import streamlit as st

from utils.load_data import load_data
from utils.theme import apply_theme
from utils.sidebar import show_sidebar

from utils.kpi_cards import show_loan_kpis

from utils.charts import (

    loan_status_chart_risk,

    loan_amount_status_chart,

    loan_duration_chart,

    top_loan_chart

)
# Configure page

st.set_page_config(

    page_title="Loan Risk Analysis",

    page_icon="⚠️",

    layout="wide"

)

# Apply theme

apply_theme()

# Display sidebar

show_sidebar()

# Load datasets

data = load_data()

loan = data["loan"]

client = data["client"]

account = data["account"]

transactions = data["transactions"]

# Page title

st.title("⚠️ Loan Risk Analysis")

st.markdown("---")

# Create Loan Status

loan["Loan_Status"] = loan["status"].replace({

    "A": "Active",

    "B": "Closed",

    "C": "Default",

    "D": "High Risk"

})

# Calculate default rate

default_rate = (

    (loan["Loan_Status"] == "Default").sum()

    / len(loan)

) * 100

# Display KPI Cards

show_loan_kpis(

    total_loans=loan.shape[0],

    total_amount=loan["amount"].sum(),

    average_amount=loan["amount"].mean(),

    default_rate=default_rate

)

st.markdown("---")


col1, col2 = st.columns(2)

with col1:

    loan_status_chart_risk(loan)

with col2:

    loan_amount_status_chart(loan)
    
    
st.markdown("---")

col3, col4 = st.columns(2)

with col3:

    loan_duration_chart(loan)

with col4:

    top_loan_chart(loan)