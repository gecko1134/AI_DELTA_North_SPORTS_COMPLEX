
import streamlit as st

def run():
    st.title("🧽 Cleaning Schedule")
    zones = ["Court A", "Court B", "Turf 1", "Turf 2"]
    for zone in zones:
        shift = st.selectbox(f"Assign cleaning shift for {zone}", ["Morning", "Afternoon", "Evening"])
        st.write(f"{zone} assigned to {shift} shift.")
