import yfinance as yf
import streamlit as st
import datetime

#https://ranaroussi.github.io/yfinance/
st.header("Stock market Analyser")
st.subheader("This webapp shows information about different stocks!")
stock_name = st.text_input("Enter Stock Name or Symbol", "AAPL")
ticker_data = yf.Ticker(stock_name)
col1, col2 = st.columns(2)

with col1:
    start_date = st.date_input("Enter Start Date", datetime.date(2019,1,1))
with col2:
    end_date = st.date_input("Enter End Date", datetime.date(2022,12,31))
#ticker_df = ticker_data.history(start='2019-01-01', end="2022-12-31")
ticker_df = ticker_data.history(start=start_date, end=end_date)

st.dataframe(ticker_df)

st.write("Closing Price Chart")
st.line_chart(ticker_df['Close'])