# Import library

import streamlit as st


# Display dashboard KPI cards

def show_dashboard_kpis(
    total_customers,
    total_accounts,
    total_loans,
    total_transactions
):

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            label="👥 Total Customers",
            value=f"{total_customers:,}"
        )

    with col2:

        st.metric(
            label="🏦 Total Accounts",
            value=f"{total_accounts:,}"
        )

    with col3:

        st.metric(
            label="💰 Total Loans",
            value=f"{total_loans:,}"
        )

    with col4:

        st.metric(
            label="💳 Total Transactions",
            value=f"{total_transactions:,}"
        )
        

# Display customer segmentation KPI cards

def show_customer_kpis(

    total_customers,

    average_age,

    average_balance,

    total_loan_amount

):

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(

            "👥 Total Customers",

            f"{total_customers:,}"

        )

    with col2:

        st.metric(

            "🎂 Average Age",

            f"{average_age:.0f} Years"

        )

    with col3:

        st.metric(

            "💰 Average Balance",

            f"₹ {average_balance:,.0f}"

        )

    with col4:

        st.metric(

            "🏦 Total Loan Amount",

            f"₹ {total_loan_amount:,.0f}"

        )
        
# Loan Risk KPI Cards

def show_loan_kpis(

    total_loans,

    total_amount,

    average_amount,

    default_rate

):

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("🏦 Total Loans", f"{total_loans:,}")

    with col2:
        st.metric("💰 Total Loan Amount", f"₹ {total_amount:,.0f}")

    with col3:
        st.metric("📊 Average Loan", f"₹ {average_amount:,.0f}")

    with col4:
        st.metric("⚠️ Default Rate", f"{default_rate:.1f}%")