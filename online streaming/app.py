import streamlit as st
import pandas as pd
import time
from data_generator import generate_transaction_event
from model import OnlineRiskModel

st.set_page_config(page_title="Real-Time Transaction Risk Scoring", layout="wide")
st.title("📊 Live Transaction Risk Monitoring")

st.caption(
    "This dashboard simulates real-time transaction ingestion and "
    "incremental risk scoring using an online learning model."
)

model = OnlineRiskModel()

if "events" not in st.session_state:
    st.session_state.events = []

start_stream = st.button("Start Stream")

table_placeholder = st.empty()
chart_placeholder = st.empty()

if start_stream:
    for _ in range(100):
        event = generate_transaction_event()
        risk = model.score_and_update(event["amount"], event["velocity"])

        event["risk_score"] = risk
        st.session_state.events.append(event)

        df = pd.DataFrame(st.session_state.events)

        table_placeholder.dataframe(df.tail(10))
        chart_placeholder.line_chart(df[["amount", "risk_score"]])

        time.sleep(1)
