# Supply-Chain-AI-Assistant-using-RAG
Answers questions with precision using Retrieval-Augmented Generation (RAG).

Technology
- LangChain	- Handles document processing, chunking, embedding, and retrieval.
- ChromaDB - Stores vector embeddings of PDF text for fast semantic search.
- OpenAI GPT - Generates responses based on retrieved document context.
- Streamlit - Creates a simple UI for users to upload PDFs and ask questions.
- GCP Cloud Run - Deploys the Streamlit app in a serverless environment.
- PyMuPDF / pdfminer - Extracts text from PDFs for processing.
