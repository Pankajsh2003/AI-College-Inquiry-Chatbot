import streamlit as st
from chatbot import CollegeChatbot

st.set_page_config(page_title="GITAM AI Chatbot", layout="centered")

# Styles
st.markdown("""
    <style>
        .response-box {
            background-color: #303F9F;
            padding: 15px;
            border-radius: 10px;
            color: white;
            font-size: 18px;
        }
        .title {
            text-align:center;
            color:#FFEB3B;
            font-size: 40px;
        }
        .subtitle {
            text-align:center;
            font-size: 18px;
            color:#BDBDBD;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='title'>🎓 GITAM AI Inquiry Chatbot</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Ask about Courses • Fees • Admission • Placements • Hostel • Facilities • Contact</p>", unsafe_allow_html=True)

bot = CollegeChatbot()

user_input = st.text_input("💬 Type your question:")

if st.button("Ask"):
    if user_input.strip() == "":
        st.warning("⚠ Please enter a question.")
    else:
        response = bot.get_response(user_input)
        st.markdown(f"<div class='response-box'>{response}</div>", unsafe_allow_html=True)

st.markdown("<br><center>Made with ❤️ for GITAM</center>", unsafe_allow_html=True)
