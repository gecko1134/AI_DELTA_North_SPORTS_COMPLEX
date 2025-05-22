
import streamlit as st

def run():
    st.title("🗂️ Member CRM")
    name = st.text_input("Member Name")
    tier = st.selectbox("Membership Tier", ["Bronze", "Silver", "Gold"])
    if st.button("Log Entry"):
        st.success(f"{name} logged as {tier}")
