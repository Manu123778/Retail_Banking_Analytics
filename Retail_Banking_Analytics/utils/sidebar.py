# Import library

import streamlit as st


# Display sidebar

def show_sidebar():

    # Display logo

    # st.sidebar.image("assets/bank_icon.png", use_container_width=True)

    st.sidebar.markdown("---")

    # Project title
    st.sidebar.title("🏦 Retail Banking")

    

    st.sidebar.write("Retail Banking Analytics Portal")

    st.sidebar.markdown("---")

    # Dataset information

    st.sidebar.subheader("Dataset")

    st.sidebar.write("✔ Customers")

    st.sidebar.write("✔ Accounts")

    st.sidebar.write("✔ Transactions")

    st.sidebar.write("✔ Loans")

    st.sidebar.markdown("---")

    # Developer information

    st.sidebar.subheader("Developer")

    st.sidebar.write("Manu Yadav")

    st.sidebar.markdown("---")

    st.sidebar.success("Data Analytics Project")
    
   