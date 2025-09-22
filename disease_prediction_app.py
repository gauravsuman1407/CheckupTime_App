import streamlit as st
import sqlite3
import hashlib
import pandas as pd
from datetime import datetime

# --- Database Setup & Functions (पहले जैसा) ---
conn = sqlite3.connect('userdata.db', check_same_thread=False)
c = conn.cursor()
def create_usertable(): c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT, password TEXT)')
def create_history_table(): c.execute('CREATE TABLE IF NOT EXISTS historytable(username TEXT, search_date TEXT, disease TEXT, prediction REAL)')
def add_userdata(username, password): c.execute('INSERT INTO userstable(username, password) VALUES (?,?)', (username, password)); conn.commit()
def add_history_data(username, disease, prediction): now = datetime.now().strftime("%Y-%m-%d %H:%M:%S"); c.execute('INSERT INTO historytable(username, search_date, disease, prediction) VALUES (?,?,?,?)', (username, now, disease, prediction)); conn.commit()
def view_user_history(username): c.execute('SELECT search_date, disease, prediction FROM historytable WHERE username = ? ORDER BY search_date DESC', (username,)); return c.fetchall()
def get_user_password_hash(username): c.execute('SELECT password FROM userstable WHERE username =?', (username,)); return c.fetchone()
def make_hashes(password): return hashlib.sha256(str.encode(password)).hexdigest()
def check_hashes(password, hashed_text): return make_hashes(password) == hashed_text

# --- Data Loading (पहले जैसा) ---
@st.cache_data
def load_data(filepath):
    try: return pd.read_csv(filepath)
    except FileNotFoundError: st.error(f"Error: '{filepath}' not found."); return None

# --- Chatbot Logic (पहले जैसा) ---
def get_bot_response(user_input):
    query = user_input.lower().strip()
    if any(word in query for word in ["नमस्ते", "हेलो", "हाय"]): return "नमस्ते! मैं आपकी क्या सहायता कर सकता हूँ?"
    elif any(word in query for word in ["कैसे", "काम", "ऐप"]): return "मैं CheckupTime हूँ। आप बीमारी खोज सकते हैं, लक्षणों के बारे में सवालों के जवाब दे सकते हैं, और मैं आपको प्रतिशत में संभावना बताऊंगा।"
    # ... (बाकी चैटबॉट लॉजिक)
    else: return "माफ़ कीजिए, मैं यह सवाल समझ नहीं पाया।"

# --- Main Application ---
def main():
    # --- Session State Initialization (पहले जैसा) ---
    st.session_state.setdefault('logged_in', False)
    st.session_state.setdefault('username', '')
    st.session_state.setdefault('language', None)
    st.session_state.setdefault('view', 'main_app')
    st.session_state.setdefault('font_size', 16)
    st.session_state.setdefault('disease_selected', None)
    st.session_state.setdefault('prediction_result', None)
    st.session_state.setdefault('messages', [])

    # --- Apply Custom CSS for Font Size (पहले जैसा) ---
    st.markdown(f"<style>.main {{ font-size: {st.session_state.font_size}px; }}</style>", unsafe_allow_html=True)

    # --- Login/Signup Page (पहले जैसा) ---
    if not st.session_state.logged_in:
        st.set_page_config(page_title="Welcome to CheckupTime", layout="centered")
        st.title("CheckupTime में आपका स्वागत है / Welcome to CheckupTime")
        # ... (Login/Signup का पूरा कोड यहाँ)
        menu = ["लॉगिन (Login)", "साइन अप (Sign Up)"]
        choice = st.sidebar.selectbox("मेनू (Menu)", menu)
        if choice == "लॉगिन (Login)":
            st.sidebar.subheader("Login Section")
            username = st.sidebar.text_input("यूज़रनेम")
            password = st.sidebar.text_input("पासवर्ड", type='password')
            if st.sidebar.button("लॉगिन करें"):
                create_usertable(); create_history_table()
                db_password_hash = get_user_password_hash(username)
                if db_password_hash and check_hashes(password, db_password_hash[0]):
                    st.session_state.logged_in = True
                    st.session_state.username = username
                    st.rerun()
                else:
                    st.warning("गलत यूज़रनेम या पासवर्ड")
        elif choice == "साइन अप (Sign Up)":
            st.sidebar.subheader("नया खाता बनाएं")
            new_user = st.sidebar.text_input("नया यूज़रनेम")
            new_password = st.sidebar.text_input("नया पासवर्ड", type='password')
            if st.sidebar.button("साइन अप करें"):
                create_usertable(); add_userdata(new_user, make_hashes(new_password))
                st.success("खाता सफलतापूर्वक बन गया है!")
                st.info("अब लॉगिन करें।")

    # --- Main App Page ---
    else:
        st.set_page_config(page_title="CheckupTime Dashboard", layout="wide")
        is_hindi = st.session_state.language == "Hindi"

        # --- Sidebar Navigation and Settings ---
        st.sidebar.title(f"नमस्ते, {st.session_state.username}" if is_hindi else f"Hello, {st.session_state.username}")
        
        # Navigation Buttons
        if st.sidebar.button("मुख्य ऐप" if is_hindi else "Main App", use_container_width=True): st.session_state.view = 'main_app'; st.rerun()
        if st.sidebar.button("मेरी हिस्ट्री" if is_hindi else "My History", use_container_width=True): st.session_state.view = 'history'; st.rerun()
        if st.sidebar.button("चैट असिस्टेंट" if is_hindi else "Chat Assistant", use_container_width=True): st.session_state.view = 'chatbot'; st.rerun()
        # --- (नया) Doctor & Emergency Help Button ---
        if st.sidebar.button("डॉक्टर और इमरजेंसी हेल्प" if is_hindi else "Doctor & Emergency Help", use_container_width=True):
            st.session_state.view = 'emergency'
            st.rerun()
        if st.sidebar.button("प्राइवेसी पॉलिसी" if is_hindi else "Privacy Policy", use_container_width=True): st.session_state.view = 'privacy'; st.rerun()

        # Settings Section
        st.sidebar.divider()
        st.sidebar.header("सेटिंग्स" if is_hindi else "Settings")
        st.sidebar.toggle("डार्क मोड" if is_hindi else "Dark Mode", value=True)
        st.session_state.font_size = st.sidebar.slider("फॉन्ट साइज", 12, 24, st.session_state.font_size)
        
        st.sidebar.divider()
        if st.sidebar.button("लॉगआउट" if is_hindi else "Logout", use_container_width=True):
            for key in list(st.session_state.keys()): del st.session_state[key]
            st.rerun()

        # --- Main Content Area (View Controller) ---
        if st.session_state.view == 'emergency': # <-- (नया) Emergency View
            st.title("डॉक्टर संपर्क और इमरजेंसी गाइड" if is_hindi else "Doctor Contact & Emergency Guide")
            
            # --- Doctor Contact Section ---
            st.header("अपने क्षेत्र में डॉक्टरों से संपर्क करें" if is_hindi else "Contact Doctors in Your Area")
            doctors_df = load_data('doctors_data.csv')
            if doctors_df is not None:
                city_list_hi = ["सभी"] + doctors_df['city'].unique().tolist()
                city_list_en = ["All"] + doctors_df['city'].unique().tolist()
                
                selected_city = st.selectbox(
                    "शहर चुनें" if is_hindi else "Select City",
                    city_list_hi if is_hindi else city_list_en
                )

                if selected_city == "सभी" or selected_city == "All":
                    filtered_doctors = doctors_df
                else:
                    filtered_doctors = doctors_df[doctors_df['city'] == selected_city]
                
                for index, row in filtered_doctors.iterrows():
                    doc_name = row['doctor_name']
                    specialty = row['specialty_hi'] if is_hindi else row['specialty_en']
                    notes = row['notes_hi'] if is_hindi else row['notes_en']
                    with st.container(border=True):
                        st.subheader(f"{doc_name} - ({specialty})")
                        st.text(f"📍 {row['city']} | 📞 {row['phone']}")
                        st.caption(notes)
            else:
                st.error("डॉक्टरों का डेटा लोड नहीं हो सका।" if is_hindi else "Could not load doctors' data.")

            # --- Emergency Guide Section ---
            st.divider()
            st.header("इमरजेंसी फर्स्ट एड गाइड" if is_hindi else "Emergency First Aid Guide")
            
            # Heart Attack
            with st.expander("❤️ हार्ट अटैक (Heart Attack)"):
                st.markdown("""
                - **तुरंत एम्बुलेंस बुलाएं।**
                - व्यक्ति को आराम से बिठाएं, उनके कपड़े ढीले करें।
                - अगर डॉक्टर ने पहले से एस्पिरिन (Aspirin) लेने को कहा है, तो दें।
                - **CPR शुरू करें** अगर व्यक्ति बेहोश है और सांस नहीं ले रहा है।
                -
                - **Call an ambulance immediately.**
                - Make the person sit comfortably, loosen their clothing.
                - Give Aspirin if it has been prescribed by a doctor.
                - **Start CPR** if the person is unconscious and not breathing.
                """)
            
            # Burns
            with st.expander("🔥 जलना (Burns)"):
                st.markdown("""
                - जले हुए हिस्से को **10-15 मिनट तक ठंडे बहते पानी** के नीचे रखें।
                - किसी भी तरह का तेल, मक्खन या टूथपेस्ट न लगाएं।
                - साफ, सूखे कपड़े से ढकें।
                - गंभीर रूप से जलने पर तुरंत डॉक्टर के पास जाएं।
                -
                - Hold the burnt area under **cool running water for 10-15 minutes.**
                - Do not apply any oil, butter, or toothpaste.
                - Cover with a clean, dry cloth.
                - For severe burns, go to the doctor immediately.
                """)

        # --- Other Views (Chatbot, History, Privacy, Main App) ---
        elif st.session_state.view == 'chatbot':
            st.title("CheckupTime असिस्टेंट 🤖")
            # ... (Chatbot code from Part 6)
            
        elif st.session_state.view == 'history':
            st.title("मेरी भविष्यवाणी हिस्ट्री")
            # ... (History view code from Part 6)
            
        elif st.session_state.view == 'privacy':
            st.title("प्राइवेसी पॉलिसी")
            # ... (Privacy view code)
            
        elif st.session_state.view == 'main_app':
            # ... (Main prediction app flow from Part 6)
            pass # The code is identical to Part 6, so it's omitted for brevity

if __name__ == '__main__':
    main()