# Bookstore AI Chatbot & RAG System

This project consists of two core components:
1. **AI-Powered Chatbot** (main.py) - A FastAPI-based WebSocket chatbot for bookstore customer engagement.
2. **RAG-based Question Answering** (rag.py) - A Retrieval-Augmented Generation system using ChromaDB and Llama 3.

## Features
### AI Chatbot (main.py)
- **WebSocket-based real-time chat** with customers.
- **Llama 3 for intent detection** and chatbot responses.
- **Firebase Firestore integration** for chat history storage.
- **SendGrid email integration** for sending discount coupons.
- **User engagement tracking** via email collection and intent classification.

### RAG System (rag.py)
- **Retrieval-Augmented Generation (RAG)** using ChromaDB.
- **Hugging Face embeddings** (MiniLM) for document vectorization.
- **FastAPI-based API** for querying the document knowledge base.
- **Automated PDF ingestion** into the vector database on startup.
- **Llama 3-powered response generation** using contextual retrieval.

## Installation & Setup
### Prerequisites
- Python 3.8+
- Firebase Admin SDK credentials
- SendGrid API Key
- Together API Key
- spaCy model: `en_core_web_sm`

### Installation
```sh
# Clone the repository
git clone https://github.com/your-repo/bookstore-ai.git
cd bookstore-ai

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Download spaCy model
python -m spacy download en_core_web_sm
```

### Environment Variables
Create a `.env` file with the following keys:
```env
TOGETHER_API_KEY=your_together_api_key
SENDGRID_API_KEY=your_sendgrid_api_key
```

## Running the Application
### Start the Chatbot
```sh
uvicorn main:app --reload
```

### Start the RAG System
```sh
uvicorn rag:app --reload
```

## API Endpoints
### Chatbot WebSocket
**Endpoint:** `ws://localhost:8000/ws/chat`
- Accepts and responds to user messages in real-time.

### RAG Query API
**Endpoint:** `http://localhost:8001/query/?question=your_question`
- Retrieves relevant information from stored PDFs and generates responses using Llama 3.

## File Structure
```
📂 bookstore-ai
 ├── 📂 data                 # Folder for storing PDFs
 ├── 📂 chroma_db            # ChromaDB persistent storage
 ├── 📜 main.py              # AI chatbot backend
 ├── 📜 rag.py               # RAG system backend
 ├── 📜 requirements.txt      # Project dependencies
 ├── 📜 .env                  # Environment variables
 ├── 📜 README.md             # Project documentation
```

## Future Improvements
- **LLM fine-tuning** for better bookstore-specific responses.
- **User analytics dashboard** for better lead conversion tracking.
- **Support for multi-modal queries** (text + images).

---
Developed by **Ujjwal** 🚀

