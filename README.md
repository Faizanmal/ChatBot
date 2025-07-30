# 🧠 AI Chat Assistant with Streamlit + Groq API

This is a conversational AI assistant built using **Streamlit** and integrated with **Groq's LLM API**. It includes user login, session tracking, persistent chat history, and support for multiple open-source LLMs like LLaMA and Mixtral.

---

## 🚀 Features

- 🔐 **User Login** (non-authenticated but session-based)
- 💬 **Chat Interface** with markdown support
- 📁 **Chat History** per user, with download option
- ♻️ **Resume Past Sessions** anytime
- 🧠 **Multiple LLMs** (LLaMA, Mixtral, Gemma, etc.)
- 🧾 **Session Storage** using local JSON files
- ⚡ **Backend API Integration** via Groq’s Chat API

---

## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/)
- Python 3
- [Groq API](https://console.groq.com/)
- JSON file storage for chat history
- Modular code structure (`main.py`, `storage.py`, `config.py`)

---

## 📂 Project Structure

```

├── main.py              # Streamlit app
├── storage.py           # Save/load user messages
├── config.py            # Contains API Key
├── chat\_data/           # Stored user chats as JSON
├── README.md            # You're here!

````

---

## 📦 Setup Instructions

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
````

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

(Manually install if `requirements.txt` is missing: `pip install streamlit requests`)

3. **Set your API Key:**

Create a file named `config.py` and add:

```python
API_KEY = "your_groq_api_key_here"
```

4. **Run the app:**

```bash
streamlit run main.py
```

---

## 🧠 Supported LLMs

You can choose from:

* `llama3-8b-8192`
* `mixtral-8x7b-32768`
* `gemma-7b-it`
* `deepseek-r1-distill-llama-70b`
* `meta-llama/llama-4-scout-17b-16e-instruct`

---

## 💾 Chat Persistence

Chats are stored in the `chat_data/` folder as JSON files, with filenames like:

```
chat_data/username_sessionID.json
```

Each entry includes:

* `user_input`
* `bot_reply`
* `timestamp`

---

## 📋 To Do / Ideas

* 🔑 Replace basic login with secure authentication
* ☁️ Migrate chat history to a database or cloud storage
* 🎨 Enhance UI with custom Streamlit components
* 📊 Add usage analytics or session metrics
* 🧪 Add unit tests for `storage.py`

---

## 📄 License

This project is open-source and free to use under the [MIT License](LICENSE).

---

## 🙋‍♂️ Author

Built by Malik Faizan
Feel free to connect on [LinkedIn](https://linkedin.com/in/faizanmalikdelhi) or contribute via PRs!
