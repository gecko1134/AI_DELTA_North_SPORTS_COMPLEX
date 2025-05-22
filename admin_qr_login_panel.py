
import streamlit as st

def run():
    st.title("🔐 QR Login Portal")
    st.markdown("Secure login for board and admin via QR.")
    st.image("assets/qr_login_sample.png", caption="Scan to login", width=250)
