import streamlit as st
from pipeline import ai_pipeline

# Page settings
st.set_page_config(page_title="AI Multi-Agent Chatbot", page_icon="🤖", layout="wide")

# Custom CSS
st.markdown("""
<style>

.stApp{
background: linear-gradient(135deg,#141E30,#243B55);
color:white;
font-family: 'Segoe UI', sans-serif;
}

.title{
text-align:center;
font-size:45px;
font-weight:bold;
margin-bottom:20px;
}

.chat-container{
max-height:500px;
overflow-y:auto;
padding:10px;
}

.user-bubble{
background:#4CAF50;
padding:12px;
border-radius:15px;
margin:10px;
width:fit-content;
margin-left:auto;
color:white;
}

.ai-bubble{
background:#2C2C2C;
padding:12px;
border-radius:15px;
margin:10px;
width:fit-content;
margin-right:auto;
color:white;
}

.input-box{
position:fixed;
bottom:20px;
left:25%;
width:50%;
}

</style>
""", unsafe_allow_html=True)

# Title
st.markdown("<div class='title'>🤖 Multi-AI Agent Chatbot</div>", unsafe_allow_html=True)

st.write("Your intelligent assistant powered by multiple AI agents")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Chat container
chat_container = st.container()

with chat_container:

    for sender, msg in st.session_state.messages:

        if sender == "You":
            st.markdown(f"<div class='user-bubble'>🧑 {msg}</div>", unsafe_allow_html=True)

        else:
            st.markdown(f"<div class='ai-bubble'>🤖 {msg}</div>", unsafe_allow_html=True)

# Input
st.markdown("<div class='input-box'>", unsafe_allow_html=True)

user_input = st.text_input("Type your message")

if st.button("Send"):

    if user_input:

        st.session_state.messages.append(("You", user_input))

        response = ai_pipeline(user_input)

        st.session_state.messages.append(("AI", response))

        st.rerun()

st.markdown("</div>", unsafe_allow_html=True)