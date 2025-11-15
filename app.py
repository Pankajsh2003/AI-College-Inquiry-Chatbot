import streamlit as st
from chatbot import CollegeChatbot

st.set_page_config(page_title="AI College Chatbot", layout="centered")

# Better Colors for Dark Mode
st.markdown("""
    <style>
        .response-box {
            background-color: #2E7D32; 
            padding: 15px;
            border-radius: 10px;
            color: white;
            font-size: 18px;
        }
        .title {
            text-align:center; 
            color:#4CAF50;
            font-size: 40px;
            margin-bottom: 10px;
        }
        .subtitle {
            text-align:center;
            font-size: 18px;
            color:#BBBBBB;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='title'>🤖 AI College Chatbot</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Ask about courses, fees, admission, placements, or contact</p>", unsafe_allow_html=True)

bot = CollegeChatbot()

user_input = st.text_input("💬 Type your question here:")

if st.button("Ask"):
    if user_input.strip() == "":
        st.warning("⚠ Please enter a question.")
    else:
        response = bot.get_response(user_input)
        st.markdown(f"<div class='response-box'>{response}</div>", unsafe_allow_html=True)

st.markdown("<br><center>Made with ❤️ in Streamlit</center>", unsafe_allow_html=True)
