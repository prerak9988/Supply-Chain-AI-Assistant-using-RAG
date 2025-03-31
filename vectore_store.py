import chromadb
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from config import CHROMA_DB_PATH

def store_in_chroma(text_chunks):
    """Store text chunks as embeddings in ChromaDB."""
    embeddings = OpenAIEmbeddings()
    chroma_client = chromadb.PersistentClient(path=CHROMA_DB_PATH)
    vector_store = Chroma.from_texts(text_chunks, embedding=embeddings, client=chroma_client)
    return vector_store