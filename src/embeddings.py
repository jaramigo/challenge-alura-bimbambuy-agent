from langchain_google_genai import GoogleGenerativeAIEmbeddings

from config import EMBEDDING_MODEL


# Crea el modelo de embeddings de Gemini
def build_embeddings():
    embeddings = GoogleGenerativeAIEmbeddings(model=EMBEDDING_MODEL)
    return embeddings