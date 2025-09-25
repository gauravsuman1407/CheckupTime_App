# pages/History.py
import streamlit as st
import common_settings

# Apply settings and get helper functions
common_settings.apply_common_settings()
get_text = common_settings.get_text

st.title(get_text("history_title")) # Assuming "history_title" is in your language file

if 'history' not in st.session_state or not st.session_state.history:
    st.info("No prediction history found.")
else:
    st.header("Your Past Predictions")
    
    # Iterate over the history list in reverse to show the latest first
    for i, entry in enumerate(reversed(st.session_state.history)):
        # Each entry is now a dictionary with 'disease', 'selected_symptoms', and 'probability'
        
        disease = entry.get("disease", "N/A")
        probability = entry.get("probability", "N/A")
        selected_symptoms = entry.get("selected_symptoms", [])
        
        # Use an expander for each history entry
        with st.expander(f"Prediction #{len(st.session_state.history) - i}: {disease} ({probability}%)"):
            st.write(f"**Disease Checked:** {disease}")
            st.write(f"**Probability:** {probability}%")
            
            st.write("**Selected Symptoms:**")
            # Display symptoms as a list
            if selected_symptoms:
                for symptom in selected_symptoms:
                    st.markdown(f"- {symptom}")
            else:
                st.write("None")