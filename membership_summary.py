
import streamlit as st
import pandas as pd

def run():
    st.title("📊 Membership Summary")
    df = pd.DataFrame({
        "Status": ["Active", "Inactive", "Pending"],
        "Count": [238, 56, 14]
    })
    st.bar_chart(df.set_index("Status"))
    st.write(df)
