import streamlit as st
import pandas as pd
import numpy as np
import time 


def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://img.freepik.com/free-photo/laboratory-glassware-with-pink-background_23-2149731526.jpg?semt=ais_hybrid&w=740&q=80");
             background-attachment: fixed;
             background-size: cover;
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()

# Title and Intro
st.title("🧪 My PhD Science Journey")
st.header("""
📊 PhD Progres Progress, not Perfection.
""")

col1, col2, col3,col4  = st.columns(4)
col1.metric("Papers Published", "0", "-1")
col2.metric("Coffee Consumed (L)", "1000000", "20")
col3.metric("Current Sanity Level", "25%", "-5%")
col4.metric("Current Chapter1", "Draft 0.01", "0.01%")


journey_data = pd.DataFrame({
    "Milestone": ["Registration", "Literature Review", "Ethics Approval", 
                  "Data Collection", "Data Analysis", "Writing", "Allowance"],
    "Momentum (%)": [90, 30, 0, 0, 0, -2, 100]
})

st.line_chart(journey_data, x="Milestone", y="Momentum (%)")






