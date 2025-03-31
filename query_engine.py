from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

def ask_question(vector_store, query):
    """Retrieve relevant context and generate an answer using GPT."""
    llm = ChatOpenAI(model_name="gpt-3")
    retriever = vector_store.as_retriever()
    rag_chain = RetrievalQA(llm=llm, retriever=retriever)
    return rag_chain.run(query)