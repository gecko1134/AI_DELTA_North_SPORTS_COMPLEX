
import streamlit as st
import datetime

def run():
    st.title("📅 Event Calendar")
    date = st.date_input("Select a date", datetime.date.today())
    st.write(f"Events on {date}:")
    st.write("- Youth League Finals")
    st.write("- Vendor Load-in")
