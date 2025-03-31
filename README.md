# Supply-Chain-AI-Assistant-using-RAG
Answers questions with precision using Retrieval-Augmented Generation (RAG).

System Architecture
PDF Ingestion: User uploads supply chain-related PDFs.

Text Processing: Extract text and split into smaller chunks.

Vector Storage: Embed text using OpenAI and store in ChromaDB.

Query Processing: User asks a question; the system retrieves relevant text.

AI Response Generation: OpenAI GPT generates a contextual response.

Deployment: The Streamlit UI is deployed on GCP Cloud Run.

Technology
- LangChain	- Handles document processing, chunking, embedding, and retrieval.
- ChromaDB - Stores vector embeddings of PDF text for fast semantic search.
- OpenAI GPT - Generates responses based on retrieved document context.
- Streamlit - Creates a simple UI for users to upload PDFs and ask questions.
- GCP Cloud Run - Deploys the Streamlit app in a serverless environment.
- PyMuPDF / pdfminer - Extracts text from PDFs for processing.
