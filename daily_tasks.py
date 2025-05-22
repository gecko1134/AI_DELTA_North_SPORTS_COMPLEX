
import streamlit as st

def run():
    st.title("📋 Daily Task Tracker")
    tasks = st.session_state.get("tasks", [])

    new_task = st.text_input("Add a task")
    if st.button("Add") and new_task:
        tasks.append(new_task)
        st.session_state["tasks"] = tasks

    for i, t in enumerate(tasks):
        if st.checkbox(t, key=f"task_{i}"):
            tasks.pop(i)
            st.session_state["tasks"] = tasks
            st.experimental_rerun()
