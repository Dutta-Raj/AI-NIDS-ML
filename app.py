import streamlit as st
import pandas as pd
import pickle

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

st.set_page_config(page_title="Is This Network Safe?", page_icon="🛡️")
st.title("🛡️ Is This Network Safe?")
st.markdown("Let AI detect if your current internet activity is **safe** or **suspicious**.")

# --- User-friendly inputs ---
protocol = st.radio("Which protocol is being used?", ["TCP", "UDP", "ICMP"])
activity = st.radio("What are you doing online?", ["Browsing websites", "Sending emails", "Downloading files", "Other"])
data_sent = st.slider("Data sent (in KB)", 0, 10000, 500)
data_received = st.slider("Data received (in KB)", 0, 10000, 1000)

# --- Map activity to service value ---
service_map = {
    "Browsing websites": "http",
    "Sending emails": "smtp",
    "Downloading files": "ftp",
    "Other": "other"
}

# --- Build input data (6 features only) ---
input_data = {
    'duration': 5,  # fixed short session duration
    'protocol_type': protocol.lower(),
    'service': service_map[activity],
    'flag': 'SF',  # standard connection flag
    'src_bytes': data_sent,
    'dst_bytes': data_received
}

# --- Predict ---
if st.button("🔍 Check Now"):
    input_df = pd.DataFrame([input_data])
    prediction = model.predict(input_df)[0]

    if prediction in [0, 'normal']:
        st.success("✅ You're Safe! No threats detected.")
    else:
        st.error("🚨 Suspicious activity detected! Be cautious.")

    st.caption("Prediction made using AI trained on network data (NSL-KDD).")
