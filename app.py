import streamlit as st
from dotenv import load_dotenv
import os
from google.generativeai import configure, GenerativeModel
from store import VectorStore
from chat_history import display_chat_history
from clear_history import clear_chat_history
from private_chat import toggle_private_chat
from export_chat import export_chat_history

load_dotenv()
configure(api_key=os.getenv("GEMINI_API_KEY"))

model = GenerativeModel('gemini-1.5-flash')

# Initialize session states
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'private_mode' not in st.session_state:
    st.session_state.private_mode = False
if 'vector_store' not in st.session_state:
    st.session_state.vector_store = VectorStore()

# Inject Tailwind CSS
st.markdown("""
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
    <style>
        .chat-container { max-width: 800px; margin: auto; }
        .chat-header { background: linear-gradient(to right, #4f46e5, #7c3aed); color: white; padding: 2rem; text-align: center; border-radius: 0.5rem; }
        .chat-message-user { background-color: #e0f2fe; color: #1f2937; padding: 1rem; margin: 0.5rem 0; border-radius: 0.5rem; border: 1px solid #bfdbfe; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        .chat-message-assistant { background-color: #f3e8ff; color: #4c1d95; padding: 1rem; margin: 0.5rem 0; border-radius: 0.5rem; border: 1px solid #ddd6fe; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        .sidebar { background-color: #f9fafb; padding: 1rem; border-radius: 0.5rem; }
        .btn { background-color: #4f46e5; color: white; padding: 0.5rem 1.5rem; border-radius: 0.25rem; margin: 0.5rem; }
        .btn:hover { background-color: #4338ca; }
        .chat-input { border: 2px solid #4f46e5; border-radius: 0.25rem; padding: 0.5rem; }
        .control-bar { display: flex; justify-content: center; gap: 1rem; padding: 1rem 0; }
        .chat-history { margin-bottom: 1rem; }
    </style>
""", unsafe_allow_html=True)

# Sidebar for chat history (from Chroma DB)
with st.sidebar.container():
    st.markdown('<div class="sidebar">', unsafe_allow_html=True)
    st.markdown('<h2 class="text-lg font-bold text-gray-800">Chat History (Stored)</h2>', unsafe_allow_html=True)
    display_chat_history()
    st.markdown('</div>', unsafe_allow_html=True)

# Main UI
st.markdown('<div class="chat-container">', unsafe_allow_html=True)
st.markdown('<div class="chat-header"><h1 class="text-3xl font-bold"> Techjays </h1></div>', unsafe_allow_html=True)

# Control bar for buttons and private chat toggle
st.markdown('<div class="control-bar">', unsafe_allow_html=True)
toggle_private_chat()
clear_chat_history()
export_chat_history()
st.markdown('</div>', unsafe_allow_html=True)

# Display conversation history in main UI (without title)
st.markdown('<div class="chat-history">', unsafe_allow_html=True)
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f'<div class="chat-message-user"><strong>You:</strong> {msg["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="chat-message-assistant"><strong>AI:</strong> {msg["content"]}</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Chat input
user_input = st.chat_input("Type your message here...", key="chat_input")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Display user message
    with st.container():
        st.markdown(f'<div class="chat-message-user"><strong>You:</strong> {user_input}</div>', unsafe_allow_html=True)
    
    # Generate response
    chat = model.start_chat(history=[{"role": msg["role"], "parts": [{"text": msg["content"]}]} for msg in st.session_state.messages[:-1]])
    response = chat.send_message(user_input)
    
    # Display assistant message
    with st.container():
        st.markdown(f'<div class="chat-message-assistant"><strong>AI:</strong> {response.text}</div>', unsafe_allow_html=True)
    
    st.session_state.messages.append({"role": "assistant", "content": response.text})
    
    # Store in vector db if not private
    if not st.session_state.private_mode:
        st.session_state.vector_store.add_message(user_input, response.text)

st.markdown('</div>', unsafe_allow_html=True)