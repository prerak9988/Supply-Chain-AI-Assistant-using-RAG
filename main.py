import streamlit as st
import tempfile
from pdf_processing import extract_text_from_pdf, chunk_text
from vector_store import store_in_chroma
from query_engine import ask_question

st.title("📦 Supply Chain AI Assistant")

uploaded_file = st.file_uploader("📄 Upload a PDF", type="pdf")

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(uploaded_file.read())
        pdf_text = extract_text_from_pdf(temp_file.name)
        text_chunks = chunk_text(pdf_text)
        vector_store = store_in_chroma(text_chunks)
        st.success("✅ PDF processed successfully!")

        query = st.text_input("🔍 Ask a question about the document:")
        if query:
            response = ask_question(vector_store, query)
            st.write("💡 Answer:", response)
