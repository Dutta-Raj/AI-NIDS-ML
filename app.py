import streamlit as st
import pandas as pd
import pickle

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

st.set_page_config(page_title="AI-Powered NIDS", page_icon="🚨")
st.title("🚨 AI-Powered Network Intrusion Detection System (NIDS)")
st.markdown("This app predicts whether a network connection is **normal** or an **attack** based on input features from the NSL-KDD dataset.")

# Feature names based on NSL-KDD dataset
feature_names = [
    'duration', 'protocol_type', 'service', 'flag', 'src_bytes', 'dst_bytes',
    'land', 'wrong_fragment', 'urgent', 'hot', 'num_failed_logins', 'logged_in',
    'num_compromised', 'root_shell', 'su_attempted', 'num_root', 'num_file_creations',
    'num_shells', 'num_access_files', 'num_outbound_cmds', 'is_host_login',
    'is_guest_login', 'count', 'srv_count', 'serror_rate', 'srv_serror_rate',
    'rerror_rate', 'srv_rerror_rate', 'same_srv_rate', 'diff_srv_rate',
    'srv_diff_host_rate', 'dst_host_count', 'dst_host_srv_count', 'dst_host_same_srv_rate',
    'dst_host_diff_srv_rate', 'dst_host_same_src_port_rate', 'dst_host_srv_diff_host_rate',
    'dst_host_serror_rate', 'dst_host_srv_serror_rate', 'dst_host_rerror_rate',
    'dst_host_srv_rerror_rate'
]

# User input form
st.sidebar.header("🛠️ Input Network Features")
input_data = {}
for feature in feature_names:
    input_data[feature] = st.sidebar.number_input(f"{feature}", value=0.0)

# Predict button
if st.sidebar.button("🔍 Predict"):
    input_df = pd.DataFrame([input_data])
    prediction = model.predict(input_df)[0]

    if prediction in [0, 'normal']:
        st.success("✅ Prediction: Normal Traffic")
    else:
        st.error("🚨 Prediction: Attack Detected!")

    st.subheader("🔢 Raw Model Output")
    st.write(f"Prediction Value: {prediction}")
