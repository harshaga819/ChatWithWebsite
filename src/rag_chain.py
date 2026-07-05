from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

from src.config import llm
from src.prompt import prompt
from src.utils import format_docs


def create_rag_chain(retriever):
    """
    Create the complete RAG pipeline.
    """

    rag_chain = (
        {
            "context": retriever | format_docs,
            "question": RunnablePassthrough(),
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    return rag_chain