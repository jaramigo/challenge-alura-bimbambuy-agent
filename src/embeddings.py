import os

# Evita warnings de paralelismo de tokenizers al usar Gradio.
os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")

from langchain_huggingface import HuggingFaceEmbeddings


def build_embeddings():
    # Crea embeddings locales con un modelo liviano y estable.
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        encode_kwargs={"normalize_embeddings": True},
    )