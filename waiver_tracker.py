
import streamlit as st

def run():
    st.title("📝 Waiver Status Tracker")
    name = st.text_input("Participant Name")
    has_waiver = st.checkbox("Waiver Submitted")
    if st.button("Check Status"):
        if has_waiver:
            st.success(f"{name} is cleared ✅")
        else:
            st.error(f"{name} is missing a waiver ⚠️")
