# app.py
import streamlit as st
import pandas as pd
from collections import defaultdict
import common_settings

# Apply settings and get helper functions from the common file
common_settings.apply_common_settings()
get_text = common_settings.get_text
get_translated_dataframe = common_settings.get_translated_dataframe

# --- Helper Function for Single Disease Prediction ---
def predict_single_disease_probability(df, selected_disease, selected_symptoms):
    """
    Calculates the probability for a single selected disease based on chosen symptoms.
    """
    if not selected_symptoms:
        return 0

    # Get the symptoms for the selected disease
    disease_info = df[df['Disease'] == selected_disease].iloc[0]
    total_symptoms_for_disease = disease_info['Symptoms']
    
    # Calculate the score
    matched_symptoms_count = len(set(selected_symptoms) & set(total_symptoms_for_disease))
    total_symptoms_count = len(total_symptoms_for_disease)
    
    score = (matched_symptoms_count / total_symptoms_count) * 100 if total_symptoms_count > 0 else 0
    
    return round(score, 2)

# --- Login / Signup UI ---
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'users_db' not in st.session_state:
    st.session_state['users_db'] = {'user': '123'} # Example user

if not st.session_state['logged_in']:
    st.title(get_text("login_title"))
    choice = st.radio("Choose Action", ('Login', 'Signup'))
    username = st.text_input(get_text("username"))
    password = st.text_input(get_text("password"), type="password")
    if choice == 'Login':
        if st.button(get_text("login_btn")):
            if username in st.session_state.users_db and st.session_state.users_db[username] == password:
                st.session_state['logged_in'] = True
                st.rerun()
            else:
                st.error(get_text("login_error"))
    elif choice == 'Signup':
        if st.button(get_text("signup_btn")):
            if username in st.session_state.users_db:
                st.error(get_text("signup_error"))
            else:
                st.session_state.users_db[username] = password
                st.success(get_text("signup_success"))
                st.info("Please go to the Login tab to log in.")
else:
    # --- Main Application UI ---
    st.title("Welcome to Check Up Time") # Changed Title

    # Get data in the correct language
    df = get_translated_dataframe()
    all_diseases = sorted(df['Disease'].unique().tolist())

    # 1. User selects a disease
    selected_disease = st.selectbox(
        "Search your disease", # New Label
        options=all_diseases,
        index=None, # Makes it so nothing is selected initially
        placeholder="Choose a disease to check"
    )

    # 2. If a disease is selected, show its symptoms
    if selected_disease:
        disease_info = df[df['Disease'] == selected_disease].iloc[0]
        symptoms_for_disease = disease_info['Symptoms']

        st.subheader(f"Select the symptoms you are experiencing for: {selected_disease}")
        
        selected_symptoms = st.multiselect(
            "Your Symptoms:",
            options=symptoms_for_disease
        )

        # 3. Predict button
        if st.button("Calculate Probability"):
            if selected_symptoms:
                probability = predict_single_disease_probability(df, selected_disease, selected_symptoms)
                
                st.header("Prediction Result")
                st.metric(label=f"Probability of having {selected_disease}", value=f"{probability}%")

                # 4. Doctor consultation advice
                st.warning("This is a preliminary prediction based on symptoms. Please consult a doctor for an accurate diagnosis.")
                
                # Optional: Save to history
                if 'history' not in st.session_state:
                    st.session_state.history = []
                st.session_state.history.append({
                    "disease": selected_disease,
                    "selected_symptoms": selected_symptoms,
                    "probability": probability
                })
            else:
                st.warning("Please select at least one symptom to calculate the probability.")