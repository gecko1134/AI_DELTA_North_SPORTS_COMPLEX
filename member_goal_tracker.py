
import streamlit as st

def run():
    st.title("🎯 Member Goal Tracker")
    name = st.text_input("Name")
    goal = st.text_input("Goal (e.g. Attend 10 sessions)")
    if st.button("Submit Goal"):
        st.success(f"{name}'s goal logged: {goal}")
