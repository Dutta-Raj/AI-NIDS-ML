import streamlit as st
import pandas as pd
import pickle

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

st.set_page_config(page_title="AI-Powered NIDS", page_icon="🚨")
st.title("🚨 AI-Powered Network Intrusion Detection System")
st.markdown("This app uses a trained AI model to detect potential intrusions in network traffic.")

# Sidebar Input UI
st.sidebar.header("🧰 Input Network Info")

# Protocol selection
protocol = st.sidebar.radio("📡 Protocol", ["TCP", "UDP", "ICMP"])

# Activity selection
activity = st.sidebar.radio("🌐 Activity", ["Browsing websites", "Sending emails", "Downloading files", "Other"])

# Data Sent
data_sent = st.sidebar.slider("📤 Data Sent (bytes)", 0, 10000, 500)

# Data Received
data_received = st.sidebar.slider("📥 Data Received (bytes)", 0, 10000, 1000)

# Map categorical values to numerical codes (for model compatibility)
protocol_map = {"TCP": 0, "UDP": 1, "ICMP": 2}
activity_map = {
    "Browsing websites": 0,
    "Sending emails": 1,
    "Downloading files": 2,
    "Other": 3
}

# Prepare input for model
input_dict = {
    "protocol_type": protocol_map[protocol],
    "activity_type": activity_map[activity],
    "src_bytes": data_sent,
    "dst_bytes": data_received
}

input_df = pd.DataFrame([input_dict])

# Predict button
if st.sidebar.button("🔍 Predict"):
    prediction = model.predict(input_df)[0]
    if prediction in [0, 'normal']:
        st.success("✅ Prediction: Normal Traffic")
    else:
        st.error("🚨 Prediction: Attack Detected!")

    st.subheader("📊 Raw Output")
    st.write(f"Prediction: {prediction}")
