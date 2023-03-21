import streamlit as st
import pandas as pd
from data_preprocessing import generate_clean_data
from investor_analysis import investor_analysis
from overall_analysis import overall_analysis
from startup_analysis import startup_analysis


st.set_page_config(
    page_title="IND Startup Analysis",
    page_icon="📊",
    layout="centered",
    # initial_sidebar_state="collapsed",
)

st.write("[Page Under Construction]")

st.header("Welcome to Indian Startup Funding Analysis Dashboard 🙋🏻")

option = st.sidebar.selectbox('Select analysis type', ['Overall Analysis', 'Investor Analysis', 'Startup Analysis'])

if option == 'Overall Analysis':
    overall_analysis()
elif option == 'Investor Analysis':
    investor_analysis()
elif option == 'Startup Analysis':
    startup_analysis()


