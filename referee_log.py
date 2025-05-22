
import streamlit as st

def run():
    st.title("⚽ Referee Logbook")
    ref = st.text_input("Referee Name")
    game = st.text_input("Game/Event ID")
    rating = st.slider("Rating", 1, 5, 3)
    if st.button("Log Feedback"):
        st.success(f"Logged for {ref} on game {game} with rating {rating}/5")
