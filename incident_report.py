
import streamlit as st
import datetime

def run():
    st.title("🚨 Incident Report Log")
    person = st.text_input("Reported By")
    description = st.text_area("Incident Description")
    photo = st.file_uploader("Optional photo evidence")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    if st.button("Submit Report"):
        st.success(f"Incident reported by {person} on {timestamp}")
