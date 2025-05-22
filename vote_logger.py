
import streamlit as st

def run():
    st.title("🗳️ Vote Logger")
    motion = st.text_input("Motion Title")
    outcome = st.radio("Outcome", ["Passed", "Failed", "Deferred"])
    if st.button("Log Vote"):
        st.success(f"Motion '{motion}' recorded as: {outcome}")
