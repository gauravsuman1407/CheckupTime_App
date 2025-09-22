import streamlit as st
import sqlite3
import pandas as pd

# डेटाबेस कनेक्शन बनाना
conn = sqlite3.connect('users.db')
c = conn.cursor()

# यूज़र टेबल बनाना अगर वह मौजूद नहीं है
c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        password TEXT
    )
''')
conn.commit()

# साइन-अप फंक्शन
def signup_page():
    st.subheader("साइन-अप करें")
    new_user = st.text_input("यूज़रनेम", key="new_user_input")
    new_password = st.text_input("पासवर्ड", type="password", key="new_pass_input")
    if st.button("साइन-अप"):
        try:
            c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (new_user, new_password))
            conn.commit()
            st.success("अकाउंट बन गया! कृपया लॉगिन करें।")
        except sqlite3.IntegrityError:
            st.error("यह यूज़रनेम पहले से मौजूद है।")

# लॉगिन फंक्शन
def login_page():
    st.subheader("लॉगिन करें")
    user = st.text_input("यूज़रनेम", key="user_input")
    password = st.text_input("पासवर्ड", type="password", key="pass_input")
    if st.button("लॉगिन"):
        c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (user, password))
        data = c.fetchall()
        if data:
            st.session_state['logged_in'] = True
            st.session_state['username'] = user
            st.rerun() # st.experimental_rerun() is deprecated
        else:
            st.error("गलत यूज़रनेम या पासवर्ड।")

# मुख्य ऐप
def main_app():
    st.title("CheckupTime")
    
    # यहाँ पर हम भाषा का चयन जोड़ेंगे
    language = st.selectbox("भाषा चुनें / Select Language", ["हिंदी", "English"])

    # CSV फ़ाइल से डेटा लोड करें
    try:
        df = pd.read_csv('diseases_data.csv')
    except FileNotFoundError:
        st.error("डेटाबेस फ़ाइल 'diseases_data.csv' नहीं मिली। सुनिश्चित करें कि यह उसी फ़ोल्डर में है जहाँ आपकी ऐप फ़ाइल है।")
        return
        
    if language == "हिंदी":
        df_lang = df[df['language'] == 'हिंदी']
    else:
        df_lang = df[df['language'] == 'English']
        
    diseases = df_lang['disease'].tolist()

    # सर्च बॉक्स
    search_label = "बीमारी का नाम खोजें:" if language == "हिंदी" else "Search for a disease:"
    symptom_label = "अपने लक्षण चुनें:" if language == "हिंदी" else "Select your symptoms:"
    button_label = "भविष्यवाणी करें" if language == "हिंदी" else "Predict"
    
    selected_disease = st.selectbox(search_label, [""] + diseases)
    
    if selected_disease:
        st.subheader(symptom_label)
        
        selected_symptoms = []
        
        # चुने गए रोग के अनुसार लक्षण दिखाएँ
        symptoms_row = df_lang[df_lang['disease'] == selected_disease].iloc[0]
        
        symptoms_list = [symptoms_row['symptom1'], symptoms_row['symptom2'], symptoms_row['symptom3'], symptoms_row['symptom4'], symptoms_row['symptom5']]
        
        for symptom in symptoms_list:
            if pd.isna(symptom): # अगर कोई लक्षण खाली हो तो
                continue
            if st.checkbox(symptom):
                selected_symptoms.append(symptom)

        if st.button(button_label):
            # यहाँ पर भविष्यवाणी का लॉजिक आएगा
            match_count = sum(1 for symptom in selected_symptoms if symptom in symptoms_list)
            if len(symptoms_list) > 0:
                percentage = (match_count / len(symptoms_list)) * 100
                st.success(f"{selected_disease} होने की {percentage:.0f}% संभावना है।")
            else:
                st.info("कोई भविष्यवाणी उपलब्ध नहीं।")