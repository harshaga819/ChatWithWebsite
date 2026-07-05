from langchain_chroma import Chroma

from src.config import CHROMA_DB_PATH, embedding_model


def create_vector_store(chunks):
    """
    Create and persist a Chroma vector database.
    """

    vector_db = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=str(CHROMA_DB_PATH)
    )

    return vector_db