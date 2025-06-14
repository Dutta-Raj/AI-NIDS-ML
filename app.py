import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the trained model
model = pickle.load(open("model.pkl", "rb"))

st.title("🚨 AI-Powered Network Intrusion Detection System (NIDS)")

st.write("Enter network connection features below to predict if it's an attack or normal.")

# Sample numeric inputs (adjust as per your dataset)
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

# Create user input form
user_input = {}
with st.form("nids_form"):
    for feature in feature_names:
        user_input[feature] = st.number_input(f"{feature}", value=0.0)
    submitted = st.form_submit_button("Predict")

if submitted:
    # Convert input to DataFrame
    input_df = pd.DataFrame([user_input])
    prediction = model.predict(input_df)[0]
    label = "✅ Normal" if prediction == "normal" or prediction == 0 else "🚨 Attack"
    st.success(f"Prediction: **{label}**")
