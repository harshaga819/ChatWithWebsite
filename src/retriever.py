from src.config import (
    FETCH_K,
    LAMBDA_MULT,
    SEARCH_TYPE,
    TOP_K,
)


def get_retriever(vector_db):
    """
    Create an MMR retriever from the vector database.
    """

    retriever = vector_db.as_retriever(
        search_type=SEARCH_TYPE,
        search_kwargs={
            "k": TOP_K,
            "fetch_k": FETCH_K,
            "lambda_mult": LAMBDA_MULT,
        },
    )

    return retriever