import os
import chromadb
import httpx
import asyncio
from fastapi import FastAPI, HTTPException
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")
TOGETHER_API_URL = "https://api.together.xyz/v1/chat/completions"

if not TOGETHER_API_KEY:
    raise ValueError("API Key not found! Check your .env file.")

# Initialize FastAPI app
app = FastAPI()

# Set up ChromaDB
chroma_client = chromadb.PersistentClient(path="./chroma_db")
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vector_store = Chroma(persist_directory="./chroma_db", embedding_function=embedding_model)

# Function to load and store PDF in vector database
@app.post("/upload_pdf/")
def load_and_store_pdf(pdf_path: str):
    try:
        loader = PyPDFLoader(pdf_path)
        documents = loader.load()
        
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        chunks = text_splitter.split_documents(documents)
        
        texts = [chunk.page_content for chunk in chunks]
        metadata = [{"source": chunk.metadata.get("page")} for chunk in chunks]

        vector_store.add_texts(texts, metadatas=metadata)
        vector_store.persist()
        return {"message": f"✅ PDF {pdf_path} loaded into ChromaDB."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Query function using Llama 3 via Together API
async def query_rag(question: str):
    retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 3})
    docs = retriever.get_relevant_documents(question)

    context = "\n\n".join([doc.page_content for doc in docs])

    system_prompt = "You are an AI assistant using a RAG system. Answer questions based on the given context."
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"Context: {context}\n\nQuestion: {question}"}
    ]

    payload = {
        "model": "meta-llama/Llama-3.3-70B-Instruct-Turbo",
        "messages": messages,
        "max_tokens": 300
    }
    headers = {"Authorization": f"Bearer {TOGETHER_API_KEY}"}

    async with httpx.AsyncClient() as client:
        response = await client.post(TOGETHER_API_URL, json=payload, headers=headers)
        return response.json()["choices"][0]["message"]["content"]

@app.get("/query/")
async def query_api(question: str):
    try:
        response = await query_rag(question)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

