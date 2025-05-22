
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def run():
    st.title("📊 Facility Dashboard")

    data = pd.DataFrame({
        "Zone": ["Court A", "Court B", "Turf 1", "Turf 2"],
        "Usage Hours": [82, 73, 91, 64],
        "Revenue ($)": [4100, 3650, 6300, 3700]
    })

    st.subheader("Surface Usage")
    st.dataframe(data)

    st.subheader("Usage Chart")
    fig1, ax1 = plt.subplots()
    ax1.bar(data["Zone"], data["Usage Hours"])
    ax1.set_ylabel("Hours")
    st.pyplot(fig1)

    st.subheader("Revenue Chart")
    fig2, ax2 = plt.subplots()
    ax2.bar(data["Zone"], data["Revenue ($)"], color="green")
    ax2.set_ylabel("Revenue ($)")
    st.pyplot(fig2)
