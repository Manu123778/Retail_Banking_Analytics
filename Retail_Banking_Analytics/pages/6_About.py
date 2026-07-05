# Import library

import streamlit as st

from utils.theme import apply_theme

from utils.sidebar import show_sidebar


# Configure page

st.set_page_config(

    page_title="About Project",

    page_icon="ℹ️",

    layout="wide"

)


# Apply application theme

apply_theme()


# Display sidebar

show_sidebar()


# Page Title

st.title("ℹ️ About Retail Banking Analytics Project")

st.markdown("---")


# Project Overview

st.header("📌 Project Overview")

st.write("""

The Retail Banking Analytics Project is an end-to-end Data Analytics and Machine Learning application developed using real-world banking data.

The project focuses on analyzing customer behavior, loan performance, banking transactions, customer segmentation, and loan risk prediction.

""")


st.markdown("---")


# Business Objectives

st.header("🎯 Business Objectives")

st.markdown("""

- Analyze customer banking behavior

- Identify loan risk

- Segment customers

- Forecast future transactions

- Build an interactive analytics dashboard

""")


st.markdown("---")


# Technologies

st.header("🛠 Technologies Used")

col1, col2 = st.columns(2)

with col1:

    st.markdown("""

    ✅ Python

    ✅ Pandas

    ✅ NumPy

    ✅ Plotly

    ✅ Scikit-Learn

    """)

with col2:

    st.markdown("""

    ✅ Streamlit

    ✅ SQL Server

    ✅ Power BI

    ✅ VS Code

    """)


st.markdown("---")


# Project Modules

st.header("📂 Project Modules")

st.markdown("""

- Executive Dashboard

- Customer Segmentation

- Loan Risk Analysis

- Loan Prediction

- Forecasting

""")


st.markdown("---")


# Machine Learning

st.header("🤖 Machine Learning")

st.write("""

Model Used : Logistic Regression

Problem Type : Multi-Class Classification

Target Variable : Loan Status

""")


st.markdown("---")


# Developer

st.header("👨‍💻 Developer")

st.write("""

Name : Manu Yadav

Role : Data Analyst

Skills :

• Python

• SQL

• Power BI

• Excel

• Machine Learning

• Streamlit

""")