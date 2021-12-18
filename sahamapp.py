import yfinance as yf
import streamlit as st

st.write("""
# INI CARA MENAMPILKAN DATA SAHAM MENGGUNAKAN STREAMLIT
Shown are the stock closing price and volume of Google!

1. First item
2. Second item
3. Third item
""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
tickerSymbol = 'ASII.JK'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2000-11-30', end='2021-11-30')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)