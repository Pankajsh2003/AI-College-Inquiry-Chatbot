import streamlit as st
from chatbot import CollegeChatbot

st.set_page_config(page_title="College Inquiry Chatbot", layout="centered")

bot = CollegeChatbot()

st.title("🎓 AI College Inquiry Chatbot")
st.write("Ask me anything about the college — courses, fees, admission, contact!")

user_input = st.text_input("Type your question:")

if st.button("Ask"):
    if user_input.strip() == "":
        st.warning("Please enter a question.")
    else:
        response = bot.get_response(user_input)
        st.success(response)
