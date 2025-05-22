
import streamlit as st

def run():
    st.title("📆 Board Terms Manager")
    name = st.text_input("Board Member Name")
    term_years = st.number_input("Term Length (Years)", 1, 6)
    if st.button("Add Term"):
        st.success(f"{name} term logged for {term_years} years")
