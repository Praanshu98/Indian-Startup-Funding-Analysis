import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/clean_data.csv")

def overall_analysis():
    st.subheader("Overall Analysis")

# General Analysis

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Investment",f"{round(df['amount'].sum(), 2)} Crores")

    with col2:
        st.metric("Average Ticket Size",f"{round(df.groupby('startup')['amount'].sum().mean(), 2)} Crores")
    
    sorted_grouped_investments = df.groupby('startup')['amount'].max().sort_values(ascending=False)
    st.metric("Maximum Investment",f"{sorted_grouped_investments.index[0]} : {sorted_grouped_investments.values[0]} Crores")

# Month on Month invested amount

    type_selected = st.selectbox('Select Type', ['Amount', 'Count'])

    if type_selected == 'Amount':
        temp_df = df.groupby(['year', 'month'])['amount'].sum().reset_index()
    else:
        temp_df = df.groupby(['year', 'month'])['amount'].count().reset_index()
    
    temp_df['x_axis'] = temp_df['year'].astype(str) + "-" + temp_df['month'].astype(str)

    fig, ax = plt.subplots()
    ax.plot(temp_df['x_axis'], temp_df['amount'])
    plt.xticks(rotation = 45)
    st.pyplot(fig)
