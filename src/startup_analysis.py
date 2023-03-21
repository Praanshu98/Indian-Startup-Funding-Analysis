import streamlit as st
import pandas as pd

df = pd.read_csv("../data/clean_data.csv")

def startup_analysis():
    st.header("Startup Analysis")
    st.sidebar.selectbox('Select Startup', list(df['Startup Name'].unique()))
