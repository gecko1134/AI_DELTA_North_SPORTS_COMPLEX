
import streamlit as st

def run():
    st.title("🎟️ Ticket Tracker")
    member = st.text_input("Member ID")
    scans = st.number_input("Tickets Scanned", min_value=0)
    if st.button("Log"):
        st.success(f"{member} logged with {scans} scans.")
