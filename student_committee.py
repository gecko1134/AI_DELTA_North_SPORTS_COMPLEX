
import streamlit as st

def run():
    st.title("🧑‍🎓 Student Committee Tracker")
    rep = st.text_input("Student Rep")
    topic = st.text_input("Feedback Topic")
    if st.button("Log Feedback"):
        st.success(f"Feedback from {rep} on '{topic}' logged.")
