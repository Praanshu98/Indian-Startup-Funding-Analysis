import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from data_preprocessing import generate_clean_data

generate_clean_data()

df = pd.read_csv("../data/clean_data.csv")

def investor_analysis():
    st.subheader("Investor Analysis")
    selected_investor = st.sidebar.selectbox('Select Startup', sorted(set(df['investors'].str.split(',').sum())))
    button = st.sidebar.button("Find Investor Details")
    if button:
        load_investor_details(selected_investor)


def load_investor_details(investor):
    st.markdown(f"#### {investor}")
    # 5 Latest investment by selected investor
    latest_5_investments = df[df['investors'].str.contains(f'{investor}')].head(5)[['date', 'startup', 'vertical', 
                                                                                    'city', 'round', 'amount']]
    st.subheader("Most recent Investments")
    st.dataframe(latest_5_investments)

    # Top 5 biggest investments by selected Investors

    st.subheader("Biggest Investments (Top 5)")
    col1, col2 =  st.columns(2)
    biggest_investments = df[df['investors'].str.contains(f'{investor}')].groupby('startup')['amount'].sum().sort_values(ascending=False).head(5)

    with col1:    
        st.dataframe(biggest_investments)
    
    with col2:
        fig, ax = plt.subplots()
        ax.bar(biggest_investments.index, biggest_investments.values) # type: ignore

        st.pyplot(fig)
    

    # Sectors invested in by the selected investor


    st.subheader("Sector Invested In (Top 5)")
    col1, col2 =  st.columns(2)
    sector_investments = df[df['investors'].str.contains(f'{investor}')].groupby('vertical')['amount'].sum().sort_values(ascending=False).head(5)
    

    with col1:    
        st.dataframe(sector_investments)
    
    with col2:
        fig, ax = plt.subplots()
        ax.pie(sector_investments, labels=sector_investments.index, autopct="%0.01f%%") # type: ignore

        st.pyplot(fig)

## Investment Stage Inverstors invests in.

    st.subheader("Investment Stage")
    col1, col2 =  st.columns(2)
    stage_investments = df[df['investors'].str.contains(f'{investor}')].groupby('round')['amount'].sum().sort_values(ascending=False)
    

    with col1:    
        st.dataframe(stage_investments)
    
    with col2:
        fig, ax = plt.subplots()
        ax.pie(stage_investments, labels=stage_investments.index, autopct="%0.01f%%") # type: ignore

        st.pyplot(fig)

## Investment City

    st.subheader("Investment City (Top 5)")
    col1, col2 =  st.columns(2)
    city_investments = df[df['investors'].str.contains(f'{investor}')].groupby('city')['amount'].sum().sort_values(ascending=False).head(5)
    

    with col1:    
        st.dataframe(city_investments)
    
    with col2:
        fig, ax = plt.subplots()
        ax.pie(city_investments, labels=city_investments.index, autopct="%0.01f%%") # type: ignore

        st.pyplot(fig)

## Investmennt Year

    st.subheader("Year on Year Investment")
    col1, col2 =  st.columns(2)
    year_investments = df[df['investors'].str.contains(f'{investor}')].groupby('year')['amount'].sum()
    

    with col1:    
        st.dataframe(year_investments)
    
    with col2:
        fig, ax = plt.subplots()
        ax.plot(year_investments.index, year_investments.values)

        st.pyplot(fig)