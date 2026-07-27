from pathlib import Path

from langchain_community.vectorstores import FAISS


# Guarda o carga el índice vectorial
def build_or_load_vectorstore(chunks, embeddings, index_dir: Path):
    if index_dir.exists():
        vectorstore = FAISS.load_local(
            str(index_dir),
            embeddings,
            allow_dangerous_deserialization=True,
        )
        return vectorstore

    index_dir.mkdir(parents=True, exist_ok=True)
    vectorstore = FAISS.from_documents(chunks, embeddings)
    vectorstore.save_local(str(index_dir))
    return vectorstore