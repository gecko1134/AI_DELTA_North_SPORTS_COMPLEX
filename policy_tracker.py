
import streamlit as st

def run():
    st.title("📋 Policy Tracker")
    policy = st.text_input("Policy Title")
    status = st.selectbox("Status", ["Draft", "Pending Approval", "Approved"])
    if st.button("Log Policy"):
        st.success(f"{policy} - Status: {status}")
