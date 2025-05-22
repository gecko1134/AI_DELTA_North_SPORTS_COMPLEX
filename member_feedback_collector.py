
import streamlit as st

def run():
    st.title("🗣️ Feedback Collector")
    member = st.text_input("Member")
    tier = st.selectbox("Tier", ["Bronze", "Silver", "Gold"])
    feedback = st.text_area("Feedback")
    if st.button("Submit"):
        st.success(f"Feedback from {member} ({tier}) recorded.")
