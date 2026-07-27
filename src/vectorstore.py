from pathlib import Path

from langchain_community.vectorstores import FAISS


# Guarda o carga el índice vectorial.
def build_or_load_vectorstore(chunks, embeddings, index_dir: Path):
    # Si ya existe un índice guardado, lo carga desde disco.
    if index_dir.exists():
        vectorstore = FAISS.load_local(
            str(index_dir),
            embeddings,
            allow_dangerous_deserialization=True,
        )
        return vectorstore

    # Si no existe, crea el directorio y construye el índice desde cero.
    index_dir.mkdir(parents=True, exist_ok=True)
    vectorstore = FAISS.from_documents(chunks, embeddings)
    vectorstore.save_local(str(index_dir))
    return vectorstore