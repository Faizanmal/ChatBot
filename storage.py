import os
import json
from datetime import datetime

BASE_DIR = "chat_data"
os.makedirs(BASE_DIR, exist_ok=True)

def get_session_file(username, session_id):
    return os.path.join(BASE_DIR, f"{username}_{session_id}.json")

def save_message(username, session_id, user_input, bot_reply):
    filepath = get_session_file(username, session_id)
    chat = []
    if os.path.exists(filepath):
        with open(filepath, "r") as f:
            chat = json.load(f)

    chat.append({
        "user_input": user_input,
        "bot_reply": bot_reply,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

    with open(filepath, "w") as f:
        json.dump(chat, f, indent=2)

def load_sessions(username):
    files = os.listdir(BASE_DIR)
    return [f.replace(f"{username}_", "").replace(".json", "") for f in files if f.startswith(username)]

def load_session_messages(username, session_id):
    filepath = get_session_file(username, session_id)
    if os.path.exists(filepath):
        with open(filepath, "r") as f:
            return json.load(f)
    return []
