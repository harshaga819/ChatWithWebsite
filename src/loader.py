from langchain_community.document_loaders import WebBaseLoader


def load_website(url: str):
    """
    Load website content and return LangChain documents.
    """

    try:
        loader = WebBaseLoader(url)
        documents = loader.load()

        if not documents:
            raise ValueError("No content could be extracted from the website.")

        return documents

    except Exception as e:
        raise RuntimeError(f"Failed to load website: {e}")