# pages/4_Emergency_Guidance.py
import streamlit as st
import common_settings

# Apply settings and get helper functions
common_settings.apply_common_settings()
get_text = common_settings.get_text

st.title(get_text("emergency_title"))

st.subheader(get_text("doctor_contact_header"))

# --- Doctor Contact Section ---
lang = st.session_state.get("lang", "en")
doctors_list = common_settings.translations.get(lang, {}).get("doctors", [])

if doctors_list:
    # Get unique cities for the filter
    cities = sorted(list(set([doc["city"] for doc in doctors_list])))
    cities.insert(0, get_text("all_cities"))

    selected_city = st.selectbox(get_text("select_city_label"), options=cities)

    # Filter doctors based on selection
    if selected_city == get_text("all_cities"):
        filtered_doctors = doctors_list
    else:
        filtered_doctors = [doc for doc in doctors_list if doc["city"] == selected_city]

    # Display doctor cards
    for doc in filtered_doctors:
        with st.container():
            st.markdown(f"#### Dr. {doc['name']} - ({doc['specialty']})")
            st.markdown(f"📍 {doc['city']} | 📞 {doc['phone']}")
            st.caption(f"_{doc['notes']}_")
            st.divider()

else:
    st.info("Doctor information is not available.")


# --- First Aid Section ---
st.subheader(get_text("first_aid_header"))

with st.expander(get_text("heart_attack_title")):
    st.markdown(get_text("heart_attack_steps"))

with st.expander(get_text("burns_title")):
    st.markdown(get_text("burns_steps"))


# --- Original Emergency Info (Kept at the bottom) ---
st.divider()
st.header(get_text("emergency_header_1"))
st.error(get_text("emergency_disclaimer"))
st.markdown(get_text("emergency_symptoms_list"))

st.header(get_text("emergency_header_2"))
st.markdown(get_text("emergency_contacts_list"))