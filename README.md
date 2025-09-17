## Task-1_Chat-Application

A Streamlit-based chat application powered by Google's Gemini (via `google-generativeai`) with optional private mode, persistent vector storage of chat history using ChromaDB, and utilities to clear and export conversations.

### Features
- **Gemini-powered chat**: Uses `gemini-1.5-flash` for fast responses.
- **Private mode**: Toggle to keep messages out of persistent storage.
- **Persistent history**: Stores chat turns in a ChromaDB collection for later viewing.
- **Sidebar history**: Renders previously stored user/assistant message pairs.
- **Export**: Download current session messages as JSON.
- **Clear**: Clear in-memory session and reset stored history.
- **Modern UI**: TailwindCSS-styled components for a clean look.

### Project Structure
- `app.py`: Main Streamlit app and UI; handles chat flow and calls Gemini API.
- `store.py`: `VectorStore` wrapper around ChromaDB for storing/retrieving messages.
- `chat_history.py`: Sidebar history rendering from vector store.
- `private_chat.py`: Private mode toggle.
- `clear_history.py`: Clear in-memory session and reinitialize vector store.
- `export_chat.py`: Export current session messages as a download.
- `requirements.txt`: Python dependencies.

### Prerequisites
- Python 3.9+ recommended
- A Google Generative AI API key (Gemini). You can obtain one from Google's AI Studio.

### Environment Variables
Create a `.env` file in the project root (`Task-1_Chat-Application`) with:

```
GEMINI_API_KEY=your_api_key_here
```

The app loads this key via `python-dotenv` and configures `google.generativeai` accordingly.

### Installation
From the project directory (`Task-1_Chat-Application`):

1) (Optional, recommended) Create and activate a virtual environment
```
python -m venv .venv
.\.venv\Scripts\activate
```

2) Install dependencies
```
pip install -r requirements.txt
```

### Run the App
From within the project directory with your environment activated and `.env` set:

```
streamlit run app.py
```

This will launch a local server and open the app in your default browser.

### Usage
- Type a message in the chat input and press Enter.
- The app displays your message and the AI response in the main pane.
- Use the controls above the chat:
  - **Private Chat (not stored in memory)**: When checked, subsequent exchanges are not saved to ChromaDB.
  - **Clear Chat History**: Clears the in-memory session and resets the vector store.
  - **Export Chat**: After clicking, a Download button appears to save current session messages as `chat_history.json`.
- The left sidebar shows previously stored user/assistant pairs from ChromaDB.

### Data Storage Details
- The `VectorStore` (in `store.py`) uses ChromaDB's default client (in-memory by default unless configured otherwise) and a default embedding function.
- When private mode is OFF, each user/assistant turn is embedded and stored with minimal metadata.
- When private mode is ON, messages remain only in the current `st.session_state` and are not written to ChromaDB.

### Configuration Notes
- Model: `gemini-1.5-flash` (configured in `app.py`). You can change the model name if needed.
- TailwindCSS is included via CDN in `app.py` purely for styling.

### Troubleshooting
- **No API key / auth errors**: Ensure `.env` exists and `GEMINI_API_KEY` is set; restart the app after changes.
- **Import errors**: Re-run `pip install -r requirements.txt` in the active virtual environment.
- **ChromaDB issues**: If persistence is desired, configure ChromaDB with a persistent directory or server; by default, it may be in-memory.
- **Blank page or UI issues**: Check the terminal for Streamlit errors; ensure internet access for the Tailwind CDN.

### Security & Privacy
- Private mode prevents storing messages in the vector store, but in-session messages are still visible until you clear them.
- Do not commit `.env` or any secrets to version control.

### License
This project is provided as-is for educational and demonstration purposes. Add a license file if you intend to distribute.

### Acknowledgments
- Built with `Streamlit`, `google-generativeai`, `ChromaDB`, and `python-dotenv`.



<h1>OUTPUT</h1>
<img width="1073" height="795" alt="image" src="https://github.com/user-attachments/assets/ba864380-a86d-489d-84e8-c84bc744f18d" />
<img width="1040" height="828" alt="image" src="https://github.com/user-attachments/assets/362d2ae7-1019-42d5-8d5a-7ce20fb6786d" />
<img width="1918" height="917" alt="image" src="https://github.com/user-attachments/assets/8d325ae1-3349-40b7-bb84-dfad4ed6da02" />

