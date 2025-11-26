
#------------------------------------------------------------------------------ #
# GitHub commands to push changes:
# git init
# git add .
# git commit -m "Initial commit of resume analyzer app"
# git remote add origin https://github.com/ml-newbie/resume-analyzer.git
# git branch -M main
# git push -u origin main
# All future pushes can be done with: git push
#------------------------------------------------------------------------------ #

import streamlit as st
from tutor_bot import ask_python_tutor
import re

st.set_page_config(page_title="Python Tutor Chatbot", layout="wide")

st.markdown("<h1 style='text-align:center'>🐍 Python Tutor Chatbot</h1>", unsafe_allow_html=True)
st.markdown(
    '<p style="font-size:10px; color:gray; text-align:center;">© 2025 John Merwin. All rights reserved.</p>',
    unsafe_allow_html=True
)

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Input text area right under title
user_input = st.text_area("Ask a Python question here:", height=100)

if st.button("💬 Ask Tutor") and user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    
    with st.spinner("🤖 Tutor is thinking..."):
        response = ask_python_tutor(user_input, chat_history=st.session_state.chat_history[:-1])
    
    st.session_state.chat_history.append({"role": "assistant", "content": response})

# Render chat
for msg in st.session_state.chat_history:
    st.markdown(f"**{msg['role'].capitalize()}:** {msg['content']}")

# Chat container
chat_container = st.container()

for msg in st.session_state.chat_history:
    if msg["role"] == "user":
        chat_container.markdown(
            f"<div style='background-color:#cce5ff;padding:10px;border-radius:5px;margin:5px 0;'><b>You:</b> {msg['content']}</div>",
            unsafe_allow_html=True
        )
    else:
        # Detect code blocks and render nicely
        code_blocks = re.findall(r"```(python)?\n(.*?)```", msg["content"], re.DOTALL)
        if code_blocks:
            text_only = re.sub(r"```(python)?\n(.*?)```", "", msg["content"], flags=re.DOTALL)
            if text_only.strip():
                chat_container.markdown(
                    f"<div style='background-color:#d4edda;padding:10px;border-radius:5px;margin:5px 0;'><b>Tutor:</b> {text_only.strip()}</div>",
                    unsafe_allow_html=True
                )
            for _, code in code_blocks:
                chat_container.code(code, language="python")
        else:
            chat_container.markdown(
                f"<div style='background-color:#d4edda;padding:10px;border-radius:5px;margin:5px 0;'><b>Tutor:</b> {msg['content']}</div>",
                unsafe_allow_html=True
            )
