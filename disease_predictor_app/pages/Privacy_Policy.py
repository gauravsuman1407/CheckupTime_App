# pages/5_Privacy_Policy.py
import streamlit as st
import common_settings

common_settings.apply_common_settings()
get_text = common_settings.get_text

st.title(get_text("privacy_title"))

st.markdown(get_text("privacy_policy_content"))