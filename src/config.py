from pathlib import Path

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings

# Load Environment Variables

load_dotenv()

# Project Paths

BASE_DIR = Path(__file__).resolve().parent.parent

CHROMA_DB_PATH = BASE_DIR / "data" / "chroma_db"

# Model Configuration

LLM_MODEL = "llama-3.3-70b-versatile"

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

TEMPERATURE = 0.2

# Text Splitting Configuration

CHUNK_SIZE = 1000

CHUNK_OVERLAP = 200

# Retriever Configuration

SEARCH_TYPE = "mmr"

TOP_K = 8

FETCH_K = 20

LAMBDA_MULT = 0.5

# Embedding Model

embedding_model = HuggingFaceEmbeddings(
    model_name=EMBEDDING_MODEL
)

# LLM

llm = ChatGroq(
    model=LLM_MODEL,
    temperature=TEMPERATURE
)