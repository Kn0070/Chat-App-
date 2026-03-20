import streamlit as st
import google.generativeai as genai

st.title("Khushal's Gemini AI App")
api_key = st.sidebar.text_input("AIzaSyBFywiKHodFb1NEFh-IF9Uw8t12l31xDwY", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    user_input = st.text_input("Ask me anything:")
    if user_input:
        response = model.generate_content(user_input)
        st.write(response.text)