import streamlit as st
import pandas as pd

df = pd.read_csv('C:\Pycharm_workspace\GitHub\July_25_Web_APP\cars24-car-price.csv')

st.dataframe(df)