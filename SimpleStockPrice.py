import streamlit as st
import yfinance as yf

st.write("""
#Simple Stock Price App

Shown are the stock closing price and volume of NVIDIA!!

""")

#define the ticker symbol
tickerSymbol = 'NVDA'
#get data on this tracker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDF = tickerData.history(period = '1d', start = '2008-1-31', end = '2023-8-31')

st.write("""
## Closing Price
""")
st.line_chart(tickerDF.Close)
st.write("""
## Volume Price
""")
st.line_chart(tickerDF.Volume)