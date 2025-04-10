
# 📚 Bookstore AI Chatbot

A Dockerized FastAPI + WebSocket chatbot for bookstore customer engagement, powered by Llama 3, Firebase, and SendGrid.

## 🚀 Features

- 🧠 Intent detection using Llama 3 (Together API)
- 💬 Real-time chat via WebSocket
- 🔥 Firebase Firestore for chat history & email storage
- ✉️ SendGrid integration for email discount coupons
- 🤖 Personalized, quirky AI responses (custom system prompt)

## 🛠️ Setup

### 1. Clone & Install

```bash
git clone https://github.com/UjjwalPardeshi/Rag_Application.git
cd chatbot
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

### 2. Environment Variables

Create a `.env` file:

```env
TOGETHER_API_KEY=your_together_api_key
SENDGRID_API_KEY=your_sendgrid_api_key
FIREBASE_CREDENTIALS_PATH=path_to_firebase_credentials.json
```

### 3. Run the App

```bash
uvicorn main:app --reload
```

## 🧪 WebSocket Endpoint

```ws
ws://localhost:8000/ws/chat
```

## 📦 Docker

```bash
docker build -t bookstore-chatbot .
docker run -p 8000:8000 --env-file .env bookstore-chatbot
```

## 🗂️ Project Structure

```
📁 bookstore-chatbot
├── main.py           # Chatbot backend
├── requirements.txt
├── .env
├── Dockerfile
```

---

Let me know if you want the RAG part or advanced usage added too.
