# Import libraries

import streamlit as st

from utils.load_data import load_data

from utils.theme import apply_theme

from utils.sidebar import show_sidebar

from utils.model_loader import load_model

# Configure page

st.set_page_config(

    page_title="Loan Prediction",

    page_icon="🤖",

    layout="wide"

)


# Apply theme

apply_theme()


# Display sidebar

show_sidebar()


# Load dataset

data = load_data()

model, scaler = load_model()

st.success("✅ Model Loaded Successfully")

loan = data["loan"]


# Page title

st.title("🤖 Loan Prediction")

st.markdown("---")


# User Inputs

st.subheader("Enter Customer Details")

col1, col2 = st.columns(2)

with col1:

    age = st.number_input("Age", 18, 100, 45)

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    account_type = st.selectbox(
        "Account Type",
        ["OWNER", "DISPONENT"]
    )

    total_transactions = st.number_input(
        "Total Transactions",
        min_value=0,
        value=350
    )

    total_transaction_amount = st.number_input(
        "Total Transaction Amount",
        min_value=0.0,
        value=150000.0
    )

with col2:

    average_transaction_amount = st.number_input(
        "Average Transaction Amount",
        min_value=0.0,
        value=4500.0
    )

    average_balance = st.number_input(
        "Average Balance",
        min_value=0.0,
        value=60000.0
    )

    loan_amount = st.number_input(
        "Loan Amount",
        min_value=0.0,
        value=120000.0
    )

    loan_duration = st.number_input(
        "Loan Duration (Months)",
        min_value=1,
        value=36
    )

    monthly_payment = st.number_input(
        "Monthly Payment",
        min_value=0.0,
        value=4200.0
    )
    
    
if st.button("Predict Loan Risk"):

    # Encode categorical values
    gender_value = 1 if gender == "Female" else 0
    account_type_value = 1 if account_type == "OWNER" else 0

    # Create input data
    input_data = [[
        age,
        gender_value,
        account_type_value,
        total_transactions,
        total_transaction_amount,
        average_transaction_amount,
        average_balance,
        loan_amount,
        loan_duration,
        monthly_payment
    ]]

    # Scale input
    input_scaled = scaler.transform(input_data)

    # Predict
    prediction = model.predict(input_scaled)[0]

    # Decode prediction
    loan_status = {
        0: "Loan Completed Successfully",
        1: "Loan Completed with Issues",
        2: "Active Loan",
        3: "Active Loan with Outstanding Debt"
    }

    st.markdown("---")
    st.subheader("Prediction Result")

    if prediction == 0:
        st.success("🟢 " + loan_status[prediction])

    elif prediction == 1:
        st.warning("🟡 " + loan_status[prediction])

    elif prediction == 2:
        st.info("🔵 " + loan_status[prediction])

    else:
        st.error("🔴 " + loan_status[prediction])