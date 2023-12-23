import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt

st.title("S&P500 APP")
st.markdown("""
    This app recives the list of the S&P500(from wikipedia) and it's corresponding **closing price** (year to date)

    * **Python Libraries:** Pandas, Streamlit, base64, matplotlib
    * **Data Source:** [Wikipedia](https://en.wikipedia.org/wiki/List_of_S%26P_500_companies).

    ***      
""")

#loading data
@st.cache_data
def load_data():
    url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    html = pd.read_html(url,header=0)
    df = html[0]
    return df

df =  load_data()

