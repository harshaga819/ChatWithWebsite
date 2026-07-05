from langchain_core.prompts import ChatPromptTemplate


prompt = ChatPromptTemplate.from_template(
    """
You are an AI assistant that answers questions based only on the provided website content.

Instructions:
- Read the complete context carefully.
- Answer only using the provided context.
- If multiple context chunks contain relevant information, combine them into a clear and natural answer.
- Do not use outside knowledge.
- If the answer is not available in the context, reply:
  "I couldn't find the answer on the provided website."

Context:
{context}

Question:
{question}

Answer:
"""
)