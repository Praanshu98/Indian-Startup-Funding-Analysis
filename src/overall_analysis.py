import streamlit as st
import pandas as pd

df = pd.read_csv("../data/clean_data.csv")

def overall_analysis():
    st.header("Overall Analysis")