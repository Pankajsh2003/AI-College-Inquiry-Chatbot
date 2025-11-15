import streamlit as st
from chatbot import CollegeChatbot

st.set_page_config(page_title="AI College Chatbot", layout="centered")

# Stylish UI
st.markdown("""
    <h1 style='text-align:center; color:#4CAF50;'>🤖 AI College Inquiry Chatbot</h1>
    <p style='font-size:18px; text-align:center;'>
        Ask anything about courses, fees, admission, or contact details!
    </p>
    <hr>
""", unsafe_allow_html=True)

bot = CollegeChatbot()

# Input box
user_input = st.text_input("💬 Type your question here:")

if st.button("Ask"):
    if user_input.strip() == "":
        st.warning("⚠ Please enter a question.")
    else:
        response = bot.get_response(user_input)
        st.markdown(f"""
            <div style='padding:15px; border-radius:10px; background:#E8F5E9; font-size:18px;'>
                <b>Chatbot:</b> {response}
            </div>
        """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Made with ❤️ in Streamlit</p>", unsafe_allow_html=True)
