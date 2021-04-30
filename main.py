import streamlit as st
import pandas as pd


st.title("Dow j close price")
df = pd.read_csv('DJI.csv')
st.write(df)
st.line_chart(df.Close)
