import pandas as pd
import os

def generate_clean_data():

    df = pd.read_csv("../data/startup_funding.csv")

    df.drop(columns=['Remarks'], inplace= True)

    df.set_index('Sr No', inplace=True)

    df.rename(columns={
        'Date dd/mm/yyyy' : 'date',
        'Startup Name' : 'startup',
        'Industry Vertical' : 'vertical',
        'SubVertical' : 'subvertical',
        'City  Location' : 'city',
        'Investors Name' : 'investors',
        'InvestmentnType' : 'round',
        'Amount in USD' : 'amount'
    }, inplace=True)

    df['amount'] = df['amount'].fillna('0')

    df['amount'] = df['amount'].str.replace(',', '')

    df['amount'] = df['amount'].str.replace('undisclosed', '0')

    df['amount'] = df['amount'].str.replace('Undisclosed', '0')

    df['amount'] = df['amount'].str.replace('unknown', '0')

    df = df[df['amount'].str.isdigit()]

    df['amount'] = df['amount'].astype(float)

    def dollar_to_inr(amount):
        return (amount * 82)/10000000

    df['amount'] = df['amount'].apply(dollar_to_inr).round(2)

    df['date'] = df['date'].str.replace('05/072018', '05/07/2018')

    df['date'] = pd.to_datetime(df['date'], errors='coerce')

    df = df.dropna(subset=['date', 'startup', 'vertical', 'city','investors', 'round', 'amount'])

    df['year'] = df['date'].dt.year
    
    df['month'] = df['date'].dt.month

    df.to_csv('../data/clean_data.csv', index=False)