
import streamlit as st

def run():
    st.title("📝 Meeting Attendance Log")
    meeting = st.text_input("Meeting Date")
    attendees = st.text_area("Attendees (comma-separated)")
    if st.button("Log Attendance"):
        st.success(f"{len(attendees.split(','))} attendees logged for {meeting}")
