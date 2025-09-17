# clear_history.py
import streamlit as st
from store import VectorStore

def clear_chat_history():
    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.session_state.vector_store = VectorStore()  # Reinitialize to clear
        st.success("Chat history cleared!")