import streamlit as st
import pandas as pd

st.write("""
	## GWU SCC
	Data Analysis
	""")

df = pd.read_csv("btc-usd.csv")

# st.write(df)

st.line_chart(df, x="Date", y="Close")
st.bar_chart(df, x="Date", y="Close")

st.snow()
st.balloons()