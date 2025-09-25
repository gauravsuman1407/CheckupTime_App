# pages/2_Chatbot.py
import streamlit as st
import common_settings

common_settings.apply_common_settings()
get_text = common_settings.get_text

st.title(get_text("chatbot_title"))

st.info(get_text("chatbot_info"))

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

def get_bot_response(user_input):
    user_input = user_input.lower()
    if "cold" in user_input or "सर्दी" in user_input:
        return get_text("chatbot_resp_cold")
    elif "covid" in user_input or "कोविड" in user_input:
        return get_text("chatbot_resp_covid")
    elif "flu" in user_input or "इन्फ्लूएंजा" in user_input:
        return get_text("chatbot_resp_flu")
    elif "emergency" in user_input or "आपातकाल" in user_input:
        return get_text("chatbot_resp_emergency")
    elif "hello" in user_input or "hi" in user_input or "नमस्ते" in user_input:
        return get_text("chatbot_resp_hello")
    else:
        return get_text("chatbot_resp_default")

if prompt := st.chat_input(get_text("chatbot_prompt")):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    response = get_bot_response(prompt)
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})