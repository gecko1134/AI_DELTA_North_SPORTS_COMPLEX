
import streamlit as st

def run():
    st.title("👥 Shift Assigner")
    staff = st.multiselect("Select Staff", ["Alex", "Taylor", "Morgan", "Jamie"])
    zone = st.selectbox("Assign to Zone", ["Court A", "Turf 1", "Main Entrance"])
    if st.button("Assign Shift"):
        st.success(f"Assigned {', '.join(staff)} to {zone}")
