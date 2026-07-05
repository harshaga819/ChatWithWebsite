import streamlit as st

from src.loader import load_website
from src.splitter import split_documents
from src.vector_store import create_vector_store
from src.retriever import get_retriever
from src.rag_chain import create_rag_chain

# ==========================================================
# Page Configuration
# ==========================================================

st.set_page_config(
    page_title="Website Chatbot using RAG",
    page_icon="🌐",
    layout="wide"
)

# ==========================================================
# Session State
# ==========================================================

if "rag_chain" not in st.session_state:
    st.session_state.rag_chain = None

if "processed_url" not in st.session_state:
    st.session_state.processed_url = None

# ==========================================================
# Title
# ==========================================================

st.title("🌐 Website Chatbot using RAG")

st.write(
    "Ask questions about any website using Retrieval-Augmented Generation (RAG)."
)

st.divider()

# ==========================================================
# Website URL
# ==========================================================

website_url = st.text_input(
    "Enter Website URL",
    placeholder="https://example.com"
)

# ==========================================================
# Process Website
# ==========================================================

if st.button("Process Website", use_container_width=True):

    if not website_url.strip():
        st.warning("Please enter a website URL.")
        st.stop()

    with st.spinner("Processing website..."):

        documents = load_website(website_url)

        chunks = split_documents(documents)

        vector_db = create_vector_store(chunks)

        retriever = get_retriever(vector_db)

        rag_chain = create_rag_chain(retriever)

        st.session_state.rag_chain = rag_chain
        st.session_state.processed_url = website_url

    st.success("Website processed successfully!")

st.divider()

# ==========================================================
# Ask Question
# ==========================================================

question = st.text_input(
    "Ask a Question",
    placeholder="What is this website about?"
)

if st.button("Ask", use_container_width=True):

    if st.session_state.rag_chain is None:
        st.warning("Please process a website first.")
        st.stop()

    if not question.strip():
        st.warning("Please enter a question.")
        st.stop()

    with st.spinner("Generating answer..."):

        answer = st.session_state.rag_chain.invoke(question)

    st.subheader("Answer")

    st.write(answer)