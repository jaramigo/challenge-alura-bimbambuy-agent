from langchain_community.embeddings import HuggingFaceEmbeddings


# Crea el modelo de embeddings local
def build_embeddings():
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
    )
    return embeddings