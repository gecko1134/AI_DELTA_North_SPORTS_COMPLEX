
import streamlit as st
import datetime

def run():
    st.title("📅 Board Report Scheduler")
    next_due = st.date_input("Next Report Due", datetime.date.today())
    st.success(f"Next board packet due: {next_due}")
