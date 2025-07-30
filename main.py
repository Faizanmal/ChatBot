import requests
import streamlit as st
from datetime import datetime
from storage import save_message, load_sessions, load_session_messages
from config import API_KEY

api = API_KEY

st.title("💬 Hello, I'm Your Assistant")

if "user" not in st.session_state:
    st.session_state.user = ""
if "passw" not in st.session_state:
    st.session_state.passw = ""
if "session_id" not in st.session_state:
    st.session_state.session_id = None
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "You are a helpful assistant."}]
if "start_time" not in st.session_state:
    st.session_state.start_time = datetime.now().strftime("%H:%M")

if not st.session_state.session_id:
    st.subheader("🔒 Login Required")
    username = st.text_input("Username", value=st.session_state.user,placeholder="Any Remember for chat history")
    password = st.text_input("Password", type="password", value=st.session_state.passw,placeholder="Any not rememberable")

    if st.button("Login"):
        if username and password:
            st.session_state.user = username
            st.session_state.passw = password
            past = load_sessions(username)
            next_index = len(past) + 1
            st.session_state.session_id = f"{username.lower()}{next_index}"
            st.rerun()
        else:
            st.error("❌ Please enter both username and password.")

else:
    st.success(f"✅ Welcome {st.session_state.user}")
    st.write("🕒 Session Start Time:", st.session_state.start_time)

    st.sidebar.title("📁 Chat History")
    past_sessions = load_sessions(st.session_state.user)

    selected_session = st.sidebar.selectbox("🔍 Select a Past Session", ["Current Session"] + past_sessions)

    if selected_session:
        history = load_session_messages(st.session_state.user, selected_session)
        full_text = ""
        for h in history:
            full_text += f"""🧑 You: {h['user_input']}
🤖 Bot: {h['bot_reply']}
🕒 {h['timestamp']}

"""
            st.sidebar.markdown(f"""**You:** {h['user_input']}  
**Bot:** {h['bot_reply']}  
🕒 {h['timestamp']}""")

        st.sidebar.download_button("📥 Download Chat", full_text, file_name=f"{selected_session}.txt")

        if st.sidebar.button("🔁 Continue this Session"):
            st.session_state.session_id = selected_session
            st.session_state.messages = [{"role": "system", "content": "You are a helpful assistant."}]
            for h in history:
                st.session_state.messages.append({"role": "user", "content": h["user_input"]})
                st.session_state.messages.append({"role": "assistant", "content": h["bot_reply"]})
            st.session_state.continued = True
            st.rerun()

    model = st.selectbox("Select Model", [
        "llama3-8b-8192", "mixtral-8x7b-32768", "gemma-7b-it",
        "deepseek-r1-distill-llama-70b", "meta-llama/llama-4-scout-17b-16e-instruct"
    ])

    if "continued" in st.session_state and st.session_state.continued:
        st.subheader("🔁 Continue Session")
    else:
        st.subheader("🆕 New Chat")

    for msg in st.session_state.messages[1:]:
        st.chat_message(msg["role"]).markdown(msg["content"])

    user_input = st.chat_input("Ask Anything...")
    if user_input:
        st.chat_message("user").markdown(user_input)
        st.session_state.messages.append({"role": "user", "content": user_input})

        with st.spinner("Answering..."):
            try:
                response = requests.post(
                    "https://api.groq.com/openai/v1/chat/completions",
                    headers={"Authorization": f"Bearer {api}", "Content-Type": "application/json"},
                    json={"model": model, "messages": st.session_state.messages}
                )
                output = response.json()["choices"][0]["message"]["content"]
                st.chat_message("assistant").markdown(output)
                st.session_state.messages.append({"role": "assistant", "content": output})
                save_message(st.session_state.user, st.session_state.session_id, user_input, output)
            except Exception as e:
                st.error(f"API or Storage Error: {e}")
