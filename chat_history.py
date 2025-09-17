# chat_history.py
import streamlit as st
from store import VectorStore

def display_chat_history():
    vector_store = st.session_state.get('vector_store', VectorStore())
    history = vector_store.get_all_messages()
    for msg in history:
        st.write(f"**User:** {msg['user']}")
        st.write(f"**Assistant:** {msg['assistant']}")
        st.write("---")