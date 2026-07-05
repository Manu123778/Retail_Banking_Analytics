# Import libraries

import pandas as pd

import plotly.express as px

import streamlit as st


# Display monthly transaction trend

def monthly_transaction_chart(transactions):

    # Convert transaction date to datetime

    transactions["Date"] = pd.to_datetime(transactions["Date"])

    # Create month column

    transactions["Month"] = transactions["Date"].dt.to_period("M").astype(str)

    # Calculate monthly transaction amount

    monthly_transaction = (
        transactions
        .groupby("Month", as_index=False)["amount"]
        .sum()
    )

    # Create interactive line chart

    fig = px.line(

        monthly_transaction,

        x="Month",

        y="amount",

        markers=True,

        title="Monthly Transaction Trend"

    )

    fig.update_layout(

        template="plotly_white",

        height=500,

        title_x=0.5,

        xaxis_title="Month",

        yaxis_title="Transaction Amount",

        hovermode="x unified"

    )

    st.plotly_chart(fig, use_container_width=True)
    
    
    # Display loan status distribution

def loan_status_chart(loan):

    # Count loan status

    loan_status = (
        loan["status"]
        .value_counts()
        .reset_index()
    )

    loan_status.columns = ["Loan Status", "Count"]

    # Create interactive donut chart

    fig = px.pie(

        loan_status,

        names="Loan Status",

        values="Count",

        hole=0.55,

        title="Loan Status Distribution"

    )

    fig.update_layout(

        template="plotly_white",

        height=500,

        title_x=0.5

    )

    st.plotly_chart(fig, use_container_width=True)
    
    
    # Display account type distribution

def account_type_chart(account):

    # Count account types

    account_type = (
        account["Account_type"]
        .value_counts()
        .reset_index()
    )

    account_type.columns = ["Account Type", "Count"]

    # Create interactive bar chart

    fig = px.bar(

        account_type,

        x="Account Type",

        y="Count",

        color="Account Type",

        text_auto=True,

        title="Account Type Distribution"

    )

    fig.update_layout(

        template="plotly_white",

        height=450,

        title_x=0.5,

        showlegend=False,

        xaxis_title="Account Type",

        yaxis_title="Number of Accounts"

    )

    st.plotly_chart(fig, use_container_width=True)
    
    
    # Display transaction type distribution

def transaction_type_chart(transactions):

    transaction_type = (
        transactions["Type"]
        .value_counts()
        .reset_index()
    )

    transaction_type.columns = ["Transaction Type", "Count"]

    fig = px.bar(

        transaction_type,

        x="Transaction Type",

        y="Count",

        color="Transaction Type",

        text_auto=True,

        title="Transaction Type Distribution"

    )

    fig.update_layout(

        template="plotly_white",

        height=400,

        title_x=0.5,

        showlegend=False,

        xaxis_title="Transaction Type",

        yaxis_title="Number of Transactions"

    )

    st.plotly_chart(fig, use_container_width=True)
    
    # Display customer age distribution

def age_distribution_chart(customer):

    # Create interactive histogram

    fig = px.histogram(

        customer,

        x="Age",

        nbins=20,

        title="Customer Age Distribution"

    )

    fig.update_layout(

        template="plotly_white",

        height=400,

        title_x=0.5,

        xaxis_title="Age",

        yaxis_title="Number of Customers"

    )

    st.plotly_chart(fig, use_container_width=True)
    
    
    # Display customer gender distribution

def gender_distribution_chart(customer):

    # Convert gender values

    gender = customer.copy()

    gender["Gender"] = gender["Gender"].replace({

        0: "Female",

        1: "Male"

    })

    # Count gender

    gender_count = (

        gender["Gender"]

        .value_counts()

        .reset_index()

    )

    gender_count.columns = ["Gender", "Count"]

    # Create interactive donut chart

    fig = px.pie(

        gender_count,

        names="Gender",

        values="Count",

        hole=0.55,

        title="Customer Gender Distribution"

    )

    fig.update_layout(

        template="plotly_white",

        height=400,

        title_x=0.5

    )

    st.plotly_chart(fig, use_container_width=True)
    
    
    
    # Display average balance by age group

def balance_by_age_chart(customer):

    # Create age groups
    customer = customer.copy()

    customer["Age Group"] = pd.cut(

        customer["Age"],

        bins=[0, 30, 40, 50, 60, 70, 100],

        labels=[
            "18-30",
            "31-40",
            "41-50",
            "51-60",
            "61-70",
            "70+"
        ]
    )

    balance = (
        customer
        .groupby("Age Group", as_index=False)["balance"]
        .mean()
    )

    fig = px.bar(

        balance,

        x="Age Group",

        y="balance",

        color="Age Group",

        text_auto=".0f",

        title="Average Balance by Age Group"

    )

    fig.update_layout(

        template="plotly_white",

        height=400,

        title_x=0.5,

        showlegend=False,

        xaxis_title="Age Group",

        yaxis_title="Average Balance"

    )

    st.plotly_chart(fig, use_container_width=True)
    
    
    
# Loan Status Distribution

def loan_status_chart_risk(loan):

    status = (
        loan["Loan_Status"]
        .value_counts()
        .reset_index()
    )

    status.columns = ["Loan Status", "Count"]

    fig = px.pie(

        status,

        names="Loan Status",

        values="Count",

        hole=0.55,

        title="Loan Status Distribution"

    )

    fig.update_layout(

        template="plotly_white",

        height=400,

        title_x=0.5

    )

    st.plotly_chart(fig, use_container_width=True)
    
    
# Loan Amount by Status

def loan_amount_status_chart(loan):

    amount = (

        loan

        .groupby("Loan_Status", as_index=False)["amount"]

        .sum()

    )

    fig = px.bar(

        amount,

        x="Loan_Status",

        y="amount",

        color="Loan_Status",

        text_auto=True,

        title="Loan Amount by Status"

    )

    fig.update_layout(

        template="plotly_white",

        height=400,

        title_x=0.5,

        showlegend=False,

        xaxis_title="Loan Status",

        yaxis_title="Loan Amount"

    )

    st.plotly_chart(fig, use_container_width=True)
    
    
# Loan Duration Distribution

def loan_duration_chart(loan):

    fig = px.histogram(

        loan,

        x="duration",

        nbins=10,

        title="Loan Duration Distribution"

    )

    fig.update_layout(

        template="plotly_white",

        height=400,

        title_x=0.5,

        xaxis_title="Loan Duration (Months)",

        yaxis_title="Number of Loans"

    )

    st.plotly_chart(fig, use_container_width=True)
    
# Top 10 Loans by Amount

def top_loan_chart(loan):

    top_loan = (

        loan

        .sort_values("amount", ascending=False)

        .head(10)

    )

    fig = px.bar(

        top_loan,

        x="loan_id",

        y="amount",

        color="amount",

        text_auto=True,

        title="Top 10 Loans by Amount"

    )

    fig.update_layout(

        template="plotly_white",

        height=400,

        title_x=0.5,

        showlegend=False,

        xaxis_title="Loan ID",

        yaxis_title="Loan Amount"

    )

    st.plotly_chart(fig, use_container_width=True)
    
    
    
# Display transaction forecasting

def forecasting_chart(monthly):

    import pandas as pd

    import plotly.graph_objects as go

    # Copy data

    forecast = monthly.copy()

    # Forecast next 12 months using average monthly growth

    growth = forecast["amount"].pct_change().mean()

    last_value = forecast["amount"].iloc[-1]

    last_month = pd.Period(forecast["Month"].iloc[-1], freq="M")

    future = []

    for i in range(1,13):

        last_month = last_month + 1

        last_value = last_value * (1 + growth)

        future.append({

            "Month":str(last_month),

            "amount":last_value

        })

    future = pd.DataFrame(future)

    # Create chart

    fig = go.Figure()

    fig.add_trace(

        go.Scatter(

            x=forecast["Month"],

            y=forecast["amount"],

            mode="lines+markers",

            name="Historical"

        )

    )

    fig.add_trace(

        go.Scatter(

            x=future["Month"],

            y=future["amount"],

            mode="lines+markers",

            name="Forecast"

        )

    )

    fig.update_layout(

        title="Transaction Forecast (Next 12 Months)",

        template="plotly_white",

        height=450,

        title_x=0.5,

        xaxis_title="Month",

        yaxis_title="Transaction Amount"

    )

    st.plotly_chart(fig,use_container_width=True)

    return future