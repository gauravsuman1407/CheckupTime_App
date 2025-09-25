import streamlit as st
import pandas as pd  # <-- यही लाइन मिसिंग थी
import common_settings

# Apply settings and get helper functions
common_settings.apply_common_settings()
get_text = common_settings.get_text
get_translated_dataframe = common_settings.get_translated_dataframe

st.title(get_text("disease_info_title"))

# Get data in the correct language
df = get_translated_dataframe()

# Check if the DataFrame and columns exist
if not df.empty and 'Disease' in df.columns:
    selected_disease = st.selectbox(
        get_text("disease_selector_label"),
        df['Disease'].unique().tolist()
    )

    if selected_disease:
        # Filter the DataFrame for the selected disease
        disease_info = df[df['Disease'] == selected_disease].iloc[0]

        st.header(disease_info['Disease'])

        # Display Description
        if 'Description' in disease_info and pd.notna(disease_info['Description']):
            st.subheader(get_text("description_subheader"))
            st.write(disease_info['Description'])

        # Display Symptoms
        if 'Symptoms' in disease_info and disease_info['Symptoms']:
            st.subheader(get_text("symptoms_subheader"))
            for symptom in disease_info['Symptoms']:
                st.markdown(f"- {symptom}")

        # Display Video Link
        if 'Video_Links' in disease_info and pd.notna(disease_info['Video_Links']):
            st.subheader(get_text("video_info_subheader"))
            st.video(disease_info['Video_Links'])
else:
    st.error("Disease data could not be loaded.")