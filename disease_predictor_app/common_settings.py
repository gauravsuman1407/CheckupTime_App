# common_settings.py
import streamlit as st
import pandas as pd

# --- All Text and Data is Now Centralized Here ---
translations = {
    "en": {
        # ... (other text remains the same) ...
        "app_title": "Disease Prediction",
        "chatbot_title": "FAQ Chatbot",
        "disease_info_title": "Disease Information",
        "emergency_title": "Doctor Contact & Emergency Guide",
        "history_title": "Prediction History",
        "privacy_title": "Privacy Policy",
        "main_app_title": "Disease Prediction From Symptoms",
        
        # New UI Text for Emergency Page (CORRECTED FORMATTING)
        "doctor_contact_header": "Contact Doctors in Your Area",
        "select_city_label": "Select City",
        "all_cities": "All",
        "first_aid_header": "Emergency First Aid Guide",
        "heart_attack_title": "❤️ Heart Attack",
        "burns_title": "🔥 Burns",
        "heart_attack_steps": """
- **1. Call emergency services immediately.**
- **2. Have the person sit down and rest:** Make them sit on the floor, leaning against a wall or chair. This reduces strain on the heart.
- **3. Loosen tight clothing:** Loosen any tight clothing around the neck, chest, and waist.
- **4. Give Aspirin (if available):** If the person is not allergic to aspirin, ask them to chew one tablet (300mg) slowly. It helps to thin the blood.
- **5. Stay calm and wait for help:** Stay with the person and try to keep them calm until the ambulance arrives.
        """,
        "burns_steps": """
- **1. Cool the burn under cool running water:** Hold the affected area under cool (not ice-cold) running water for at least 10-20 minutes.
- **2. Remove jewelry and clothing:** Gently remove rings, watches, or tight clothing from the burned area before it starts to swell.
- **3. Do not apply any oils or creams:** Avoid applying butter, oil, or any creams, as this can cause infection.
- **4. Cover with a clean dressing:** Lightly cover the burn with a clean, non-stick bandage or a clean cloth.
- **5. Do not break blisters:** If blisters form, do not break them as it increases the risk of infection.
        """,
        
        # Doctor Data
        "doctors": [
            {"name": "A. K. Sharma", "specialty": "General Physician", "city": "Kota", "phone": "9876543210", "notes": "Available 24/7 for emergencies."},
            {"name": "Sunita Verma", "specialty": "Cardiologist", "city": "Jaipur", "phone": "9871234567", "notes": "Specializes in heart-related issues."},
            {"name": "R. Singh", "specialty": "Pediatrician", "city": "Kota", "phone": "9988776655", "notes": "Expert in child health."},
            {"name": "Priya Gupta", "specialty": "Dermatologist", "city": "Udaipur", "phone": "9123456789", "notes": "For skin and hair problems."},
            {"name": "Mohan Lal", "specialty": "General Physician", "city": "Jaipur", "phone": "9555666777", "notes": "Morning and evening clinic hours."}
        ],
        # ... (rest of the text keys) ...
        "login_title": "Login / Signup",
        "username": "Username",
        "password": "Password",
        "login_btn": "Login",
        "signup_btn": "Signup",
        "login_success": "Logged in successfully!",
        "login_error": "Invalid username or password.",
        "signup_success": "Signup successful! Please login.",
        "signup_error": "Username already exists.",
        "logout_btn": "Logout",
        "sidebar_header": "Settings",
        "language": "Language",
        "font_size": "Font Size",
        "main_header": "Symptom Checker",
        "symptom_selector_label": "Select your symptoms:",
        "predict_btn": "Predict Disease",
        "prediction_header": "Prediction Results",
        "no_symptoms_msg": "Please select symptoms to see a prediction.",
        "disease_col": "Disease",
        "probability_col": "Match Percentage",
        "history_disclaimer": "Your history is saved for this session only.",
        "disease_selector_label": "Select a disease to learn more:",
        "description_subheader": "Description",
        "symptoms_subheader": "Common Symptoms",
        "video_info_subheader": "Informational Video",
        "chatbot_info": "This is a simple chatbot. Ask questions like 'What are the symptoms of a cold?'.",
        "chatbot_prompt": "Ask a question...",
        "chatbot_resp_cold": "Common cold symptoms include a runny nose, sneezing, and a sore throat.",
        "chatbot_resp_covid": "COVID-19 is a respiratory illness with symptoms like fever, cough, and loss of taste or smell.",
        "chatbot_resp_flu": "Influenza (Flu) symptoms include fever, body aches, fatigue, and cough.",
        "chatbot_resp_emergency": "For emergencies, please call your local emergency number immediately.",
        "chatbot_resp_hello": "Hello! How can I help you today?",
        "chatbot_resp_default": "I'm sorry, I don't have information on that. Please consult a doctor.",
        "history_no_predictions": "You have not made any predictions in this session yet.",
        "history_prediction_expander": "Prediction",
        "history_selected_symptoms": "**Symptoms You Selected:**",
        "history_prediction_results": "**Prediction Results:**",
        "emergency_header_1": "When to Seek Immediate Medical Attention",
        "emergency_disclaimer": "Disclaimer: This application is not a substitute for professional medical advice. If you are experiencing a medical emergency, please call your local emergency number immediately.",
        "emergency_symptoms_list": "- **Difficulty breathing or shortness of breath**\n- **Persistent pain or pressure in the chest**\n- **New confusion or inability to arouse**\n- **Bluish lips or face**\n- **Severe abdominal pain**\n- **Uncontrolled bleeding**",
        "emergency_header_2": "Contact Information",
        "emergency_contacts_list": "- **National Emergency Number (India):** 112\n- **Ambulance:** 102 or 108\n- **Police:** 100\n- **Fire:** 101",
        "emergency_info": "It is always best to have the contact information for your local hospital and personal doctor readily available.",
        "privacy_policy_content": """
Last updated: September 23, 2025
This Privacy Policy describes Our policies and procedures on the collection, use and disclosure of Your information when You use the Service.
### **Information We Collect**
- **Account Information:** When you sign up, we store your username to create and manage your account.
- **Symptom Data:** The symptoms you select are used solely for the purpose of providing disease prediction results.
### **How We Use Your Information**
- **To Provide and Maintain our Service:** Including logging you into your account and providing the core prediction functionality.
- **To Manage Your Account:** To manage your registration as a user of the Service.
### **Contact Us**
If you have any questions about this Privacy Policy, you can contact us.
""",
        # Data with Video Links
        "disease_data": {
            'Disease': ['Common Cold', 'Influenza (Flu)', 'Allergies', 'COVID-19', 'Gastroenteritis', 'Migraine'],
            'Symptoms': [
                'Runny Nose, Sneezing, Sore Throat, Cough',
                'Fever, Body Aches, Fatigue, Cough, Sore Throat',
                'Sneezing, Itchy Eyes, Runny Nose, Rash',
                'Fever, Cough, Loss of Taste or Smell, Fatigue, Shortness of Breath',
                'Nausea, Vomiting, Diarrhea, Stomach Cramps',
                'Headache, Nausea, Sensitivity to Light, Aura'
            ],
            'Description': [
                'A common viral infection of the nose and throat.',
                'A viral infection that attacks your respiratory system.',
                'A condition in which the immune system reacts abnormally to a foreign substance.',
                'An infectious disease caused by the SARS-CoV-2 virus.',
                'An intestinal infection marked by watery diarrhea, abdominal cramps, nausea or vomiting.',
                'A headache of varying intensity, often accompanied by nausea and sensitivity to light and sound.'
            ],
            'Video_Links': [
                'https://youtu.be/q2rUZaLnkO8?si=fdevLMKIzBHFdMma', 
                'https://youtu.be/jzKoObDl8lM?si=G78_lON_-3VvAnfB', 
                'https://youtu.be/ludNeoqDo-c?si=JoiOb1re69kbjQNX', 
                'https://youtu.be/lJ5L-M1aD4o?si=o0Rvbg9q56aLgEKv', 
                'https://youtu.be/82xHq4Od-CY?si=5hteT7Ya90FU529g', 
                'https://youtu.be/OZtTAVtZ2qY?si=RZMxqvI1XEQJ8IjT'
            ]
        }
    },
    "hi": {
        # ... (other text remains the same) ...
        "app_title": "रोग भविष्यवाणी",
        "chatbot_title": "सहायता चैटबॉट",
        "disease_info_title": "रोग की जानकारी",
        "emergency_title": "डॉक्टर संपर्क और आपातकालीन गाइड", 
        "history_title": "भविष्यवाणी का इतिहास",
        "privacy_title": "गोपनीयता नीति",
        "main_app_title": "लक्षणों से रोग की भविष्यवाणी",
        # New UI Text for Emergency Page (CORRECTED FORMATTING)
        "doctor_contact_header": "अपने क्षेत्र में डॉक्टरों से संपर्क करें",
        "select_city_label": "शहर चुनें",
        "all_cities": "सभी",
        "first_aid_header": "आपातकालीन प्राथमिक चिकित्सा गाइड",
        "heart_attack_title": "❤️ हार्ट अटैक (Heart Attack)",
        "burns_title": "🔥 जलना (Burns)",
        "heart_attack_steps": """
- **1. तुरंत इमरजेंसी नंबर पर कॉल करें।**
- **2. व्यक्ति को आराम से बिठाएं:** उन्हें ज़मीन पर बिठा दें और किसी दीवार या कुर्सी का सहारा दें। इससे दिल पर तनाव कम होगा।
- **3. तंग कपड़े ढीले करें:** गर्दन, छाती और कमर के पास के किसी भी तंग कपड़े को ढीला कर दें।
- **4. एस्पिरिन दें (यदि उपलब्ध हो):** अगर व्यक्ति को एस्पिरिन से एलर्जी नहीं है, तो उन्हें एक टैबलेट (300mg) धीरे-धीरे चबाने के लिए कहें। यह खून को पतला करने में मदद करता है।
- **5. शांत रहें और मदद का इंतज़ार करें:** एम्बुलेंस आने तक व्यक्ति के साथ रहें और उन्हें शांत रखने की कोशिश करें।
        """,
        "burns_steps": """
- **1. जले हुए हिस्से को ठंडे पानी के नीचे रखें:** कम से कम 10-20 मिनट के लिए बहते हुए ठंडे (बर्फीले नहीं) पानी के नीचे रखें।
- **2. गहने और कपड़े हटाएं:** जले हुए हिस्से के आसपास से अंगूठी, घड़ी या तंग कपड़े धीरे से हटा दें, इससे पहले कि सूजन शुरू हो।
- **3. किसी भी तरह का तेल या क्रीम न लगाएं:** मक्खन, तेल या कोई क्रीम लगाने से बचें, इससे इन्फेक्शन हो सकता है।
- **4. साफ पट्टी से ढकें:** जले हुए हिस्से को एक साफ, नॉन-स्टिक पट्टी या साफ कपड़े से हल्के से ढकें।
- **5. फफोले न फोड़ें:** अगर फफोले बन गए हैं, तो उन्हें फोड़ें नहीं क्योंकि इससे इन्फेक्शन का खतरा बढ़ जाता है।
        """,
        # Doctor Data
        "doctors": [
            {"name": "ए. के. शर्मा", "specialty": "सामान्य चिकित्सक", "city": "Kota", "phone": "9876543210", "notes": "आपात स्थिति के लिए 24/7 उपलब्ध।"},
            {"name": "सुनीता वर्मा", "specialty": "हृदय रोग विशेषज्ञ", "city": "Jaipur", "phone": "9871234567", "notes": "हृदय संबंधी मामलों में विशेषज्ञ।"},
            {"name": "आर. सिंह", "specialty": "बाल रोग विशेषज्ञ", "city": "Kota", "phone": "9988776655", "notes": "बच्चों के स्वास्थ्य में विशेषज्ञ।"},
            {"name": "प्रिया गुप्ता", "specialty": "त्वचा रोग विशेषज्ञ", "city": "Udaipur", "phone": "9123456789", "notes": "त्वचा और बालों की समस्याओं के लिए।"},
            {"name": "मोहन लाल", "specialty": "सामान्य चिकित्सक", "city": "Jaipur", "phone": "9555666777", "notes": "सुबह और शाम क्लिनिक के घंटे।"}
        ],
        # ... (rest of the text keys) ...
        "login_title": "लॉगिन / साइनअप",
        "username": "उपयोगकर्ता नाम",
        "password": "पासवर्ड",
        "login_btn": "लॉगिन करें",
        "signup_btn": "साइन अप करें",
        "login_success": "सफलतापूर्वक लॉग इन किया!",
        "login_error": "अमान्य उपयोगकर्ता नाम या पासवर्ड।",
        "signup_success": "साइन अप सफल! कृपया लॉगिन करें।",
        "signup_error": "उपयोगकर्ता नाम पहले से मौजूद है।",
        "logout_btn": "लॉग आउट",
        "sidebar_header": "सेटिंग्स",
        "language": "भाषा",
        "font_size": "फ़ॉन्ट आकार",
        "main_header": "लक्षण परीक्षक",
        "symptom_selector_label": "अपने लक्षण चुनें:",
        "predict_btn": "रोग की भविष्यवाणी करें",
        "prediction_header": "भविष्यवाणी के परिणाम",
        "no_symptoms_msg": "भविष्यवाणी देखने के लिए कृपया लक्षण चुनें।",
        "disease_col": "रोग",
        "probability_col": "मिलान प्रतिशत",
        "history_disclaimer": "आपका इतिहास केवल इस सत्र के लिए सहेजा गया है।",
        "disease_selector_label": "अधिक जानने के लिए एक रोग चुनें:",
        "description_subheader": "विवरण",
        "symptoms_subheader": "आम लक्षण",
        "video_info_subheader": "जानकारीपूर्ण वीडियो",
        "chatbot_info": "यह एक सरल चैटबॉट है। 'सर्दी के लक्षण क्या हैं?' जैसे प्रश्न पूछें।",
        "chatbot_prompt": "एक प्रश्न पूछें...",
        "chatbot_resp_cold": "सर्दी के सामान्य लक्षणों में नाक बहना, छींक आना और गले में खराश शामिल हैं।",
        "chatbot_resp_covid": "COVID-19 एक श्वसन संबंधी बीमारी है जिसके लक्षण बुखार, खांसी और स्वाद या गंध का न आना है।",
        "chatbot_resp_flu": "इन्फ्लूएंजा (फ्लू) के लक्षणों में बुखार, शरीर में दर्द, थकान और खांसी शामिल हैं।",
        "chatbot_resp_emergency": "आपात स्थिति के लिए, कृपया तुरंत अपने स्थानीय आपातकालीन नंबर पर कॉल करें।",
        "chatbot_resp_hello": "नमस्ते! मैं आपकी कैसे मदद कर सकता हूँ?",
        "chatbot_resp_default": "मुझे खेद है, मेरे पास इस पर जानकारी नहीं है। कृपया डॉक्टर से सलाह लें।",
        "history_no_predictions": "आपने इस सत्र में अभी तक कोई भविष्यवाणी नहीं की है।",
        "history_prediction_expander": "भविष्यवाणी",
        "history_selected_symptoms": "**आपके द्वारा चुने गए लक्षण:**",
        "history_prediction_results": "**भविष्यवाणी के परिणाम:**",
        "emergency_header_1": "तत्काल चिकित्सा सहायता कब लेनी है",
        "emergency_disclaimer": "अस्वीकरण: यह एप्लिकेशन पेशेवर चिकित्सा सलाह का विकल्प नहीं है। यदि आप एक चिकित्सा आपातकाल का सामना कर रहे हैं, तो कृपया तुरंत अपने स्थानीय आपातकालीन नंबर पर कॉल करें।",
        "emergency_symptoms_list": "- **सांस लेने में कठिनाई या सांस की तकलीफ**\n- **सीने में लगातार दर्द या दबाव**\n- **नया भ्रम या जागने में असमर्थता**\n- **नीले होंठ या चेहरा**\n- **पेट में गंभीर दर्द**\n- **अनियंत्रित रक्तस्राव**",
        "emergency_header_2": "संपर्क जानकारी",
        "emergency_contacts_list": "- **राष्ट्रीय आपातकालीन नंबर (भारत):** 112\n- **एम्बुलेंस:** 102 या 108\n- **पुलिस:** 100\n- **फायर:** 101",
        "emergency_info": "अपने स्थानीय अस्पताल और व्यक्तिगत डॉक्टर की संपर्क जानकारी हमेशा उपलब्ध रखना सबसे अच्छा है।",
        "privacy_policy_content": """
अंतिम अपडेट: 23 सितंबर, 2025
यह गोपनीयता नीति सेवा का उपयोग करने पर आपकी जानकारी के संग्रह, उपयोग और प्रकटीकरण पर हमारी नीतियों और प्रक्रियाओं का वर्णन करती है।
### **हम जो जानकारी एकत्र करते हैं**
- **खाता जानकारी:** जब आप साइन अप करते हैं, तो हम आपका खाता बनाने और प्रबंधित करने के लिए आपका उपयोगकर्ता नाम संग्रहीत करते।
- **लक्षण डेटा:** आपके द्वारा चुने गए लक्षणों का उपयोग केवल रोग भविष्यवाणी के परिणाम प्रदान करने के उद्देश्य से किया जाता है।
### **हम आपकी जानकारी का उपयोग कैसे करते हैं**
- **हमारी सेवा प्रदान करने और बनाए रखने के लिए:** जिसमें आपको अपने खाते में लॉग इन करना और मुख्य भविष्यवाणी कार्यक्षमता प्रदान करना शामिल है।
- **आपका खाता प्रबंधित करने के लिए:** सेवा के उपयोगकर्ता के रूप में आपके पंजीकरण का प्रबंधन करने के लिए।
### **संपर्क करें**
यदि इस गोपनीयता नीति के बारे में आपके कोई प्रश्न हैं, तो आप हमसे संपर्क कर सकते हैं।
""",
        # Data with Video Links
        "disease_data": {
            'Disease': ['सामान्य सर्दी', 'इन्फ्लूएंजा (फ्लू)', 'एलर्जी', 'कोविड-19', 'आंत्रशोथ', 'माइग्रेन'],
            'Symptoms': [
                'बहती नाक, छींकना, गले में खराश, खांसी',
                'बुखार, शरीर में दर्द, थकान, खांसी, गले में खराश',
                'छींकना, आंखों में खुजली, बहती नाक, दाने',
                'बुखार, खांसी, स्वाद या गंध का न आना, थकान, सांस की तकलीफ',
                'मतली, उल्टी, दस्त, पेट में ऐंठन',
                'सिरदर्द, मतली, प्रकाश के प्रति संवेदनशीलता, आभा'
            ],
            'Description': [
                'नाक और गले का एक आम वायरल संक्रमण।',
                'एक वायरल संक्रमण जो आपके श्वसन तंत्र पर हमला करता है।',
                'एक ऐसी स्थिति जिसमें प्रतिरक्षा प्रणाली किसी बाहरी पदार्थ पर असामान्य रूप से प्रतिक्रिया करती है।',
                'सार्स-कोव-2 वायरस के कारण होने वाला एक संक्रामक रोग।',
                'एक आंतों का संक्रमण जिसमें पानी वाले दस्त, पेट में ऐंठन, मतली या उल्टी होती है।',
                'विभिन्न तीव्रता का सिरदर्द, जो अक्सर मतली और प्रकाश तथा ध्वनि के प्रति संवेदनशीलता के साथ होता है।'
            ],
            'Video_Links': [
                'https://youtu.be/q2rUZaLnkO8?si=fdevLMKIzBHFdMma', 
                'https://youtu.be/jzKoObDl8lM?si=G78_lON_-3VvAnfB', 
                'https://youtu.be/ludNeoqDo-c?si=JoiOb1re69kbjQNX', 
                'https://youtu.be/lJ5L-M1aD4o?si=o0Rvbg9q56aLgEKv', 
                'https://youtu.be/82xHq4Od-CY?si=5hteT7Ya90FU529g', 
                'https://youtu.be/OZtTAVtZ2qY?si=RZMxqvI1XEQJ8IjT'
            ]
        }
    }
}


# Functions remain the same
def get_text(key):
    return translations.get(st.session_state.lang, translations["en"]).get(key, key)

def get_translated_dataframe():
    lang = st.session_state.get("lang", "en")
    data = translations.get(lang, translations["en"]).get("disease_data", {})
    df = pd.DataFrame(data)
    if 'Symptoms' in df.columns and isinstance(df['Symptoms'].iloc[0], str):
         df['Symptoms'] = df['Symptoms'].apply(lambda x: [s.strip() for s in x.split(',')])
    return df

def apply_common_settings():
    if 'lang' not in st.session_state:
        st.session_state['lang'] = 'en'
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False
    if 'font_size' not in st.session_state:
        st.session_state['font_size'] = 16
    if 'history' not in st.session_state:
        st.session_state['history'] = []
    if 'users_db' not in st.session_state:
        st.session_state['users_db'] = {"user1": "pass1", "user2": "pass2"}

    st.markdown(f"""
        <style>
        html, body, [class*="st-"], .main .block-container {{
            font-size: {st.session_state.font_size}px;
        }}
        </style>
    """, unsafe_allow_html=True)
    
    if st.session_state.get('logged_in', False):
        with st.sidebar:
            st.header(get_text("sidebar_header"))
            
            selected_lang = st.selectbox(
                get_text("language"),
                options=['en', 'hi'],
                index=0 if st.session_state.lang == 'en' else 1,
                format_func=lambda x: "English" if x == 'en' else "हिंदी"
            )
            if selected_lang != st.session_state.lang:
                st.session_state.lang = selected_lang
                st.rerun()

            def update_font_size():
                st.session_state.font_size = st.session_state.font_slider

            st.slider(
                get_text("font_size"),
                min_value=12,
                max_value=24,
                key='font_slider',
                value=st.session_state.font_size,
                on_change=update_font_size
            )
            
            if st.button(get_text("logout_btn")):
                st.session_state['logged_in'] = False
                st.rerun()