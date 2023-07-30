import yfinance as yf
import streamlit as st

st.write("""
# Stock-Man 
       
Shown are the stock **closing price** and **volume** of Google!

""")

#defining ticker symbol
tickerSymbol = 'GOOGL'
#getting data
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume Price
""")
st.line_chart(tickerDf.Volume)

st.write(""" 
###### Vaibhav Sharma
""")