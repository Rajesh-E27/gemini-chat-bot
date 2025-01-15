import streamlit as st
import google.generativeai as genai


st.title("welcome to gemini chat")

genai.configure(api_key="AIzaSyDpjZ8VqFpIInANBTDXOLg6YhXrndDLIqk")  

text = st.text_input("enter your question")

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])


if st.button("Generate"):
    response = chat.send_message(text)
    st.write(response.text)
