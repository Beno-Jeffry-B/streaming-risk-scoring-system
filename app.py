import streamlit as st
import pandas as pd
import time
from data_generator import generate_data
from model import train_and_predict

st.set_page_config(page_title="Live Streaming Risk ML App", layout="wide")
st.title("📊 Real-Time Transaction Risk Dashboard")

data_placeholder = st.empty()
chart_placeholder = st.empty()

if "data" not in st.session_state:
    st.session_state.data = []

start = st.button("Start Streaming")

if start:
    for _ in range(100):
        event = generate_data()

        prediction = train_and_predict(
            event["transaction_amount"], event["transaction_velocity"]
        )

        event["risk_score"] = prediction
        st.session_state.data.append(event)

        df = pd.DataFrame(st.session_state.data)

        data_placeholder.dataframe(df.tail(10))
        chart_placeholder.line_chart(df[["transaction_amount", "risk_score"]])

        time.sleep(1)
