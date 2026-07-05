def format_docs(documents):
    """
    Convert retrieved LangChain documents into a single text string.
    """

    return "\n\n".join(doc.page_content for doc in documents)