# Import library

import streamlit as st


# Apply application theme

def apply_theme():

    st.markdown(
        """
        <style>

        .main{

            padding-top:20px;

        }

        h1{

            color:#0F62FE;

            text-align:center;

            font-weight:bold;

        }

        h2{

            color:#1F2937;

            font-weight:bold;

        }

        h3{

            color:#2563EB;

        }

        div[data-testid="metric-container"]{

            background-color:#F8FAFC;

            border:1px solid #E5E7EB;

            padding:15px;

            border-radius:10px;

            box-shadow:2px 2px 8px rgba(0,0,0,0.1);

        }

        </style>
        """,
        unsafe_allow_html=True
    )