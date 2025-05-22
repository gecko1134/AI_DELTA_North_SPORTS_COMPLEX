
import streamlit as st

def run():
    st.title("🎓 Student Rep Portal")
    name = st.text_input("Name")
    update = st.text_area("Monthly Update")
    if st.button("Submit"):
        st.success(f"Update from {name} submitted!")
