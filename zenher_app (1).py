
import streamlit as st
import requests

st.set_page_config(page_title="Zenher Assistant", layout="centered")
st.title("🤖 Zenher: Women's Health AI Assistant")

st.markdown("_Empowering menstrual and reproductive wellness with intelligent, respectful, and informative support._")

user_input = st.text_input("Ask your question 👇")

def ask_zenher(prompt):
    headers = {
        "Authorization": "Bearer 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"
    }
    url = "https://api-inference.huggingface.co/models/microsoft/Phi-3-mini"
    payload = {
        "inputs": f"You are Zenher, a friendly and respectful women's health assistant. Do not give medical diagnoses. Be supportive and informative.\n\nUser: {prompt}\nZenher:"
    }
    response = requests.post(url, headers=headers, json=payload)
    try:
        return response.json()[0]["generated_text"]
    except:
        return "Sorry, something went wrong. Please try again later."

if user_input:
    with st.spinner("Thinking..."):
        answer = ask_zenher(user_input)
        st.success(answer)
