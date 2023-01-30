import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App
 
 shown are the stock **closing price** and ***volume*** of Google!
 
 """)

tickerSymbol = 'GOOGL'        #AAPL-Apple
tickerData = yf.Ticker(tickerSymbol)
tickerdf = tickerData.history(period='id', start='2018-6-26', end='2022-6-26')

st.write("""
## Closing Price
""")
st.line_chart(tickerdf.Close)
st.write("""
## Volume Price
""")
st.line_chart(tickerdf.Volume)