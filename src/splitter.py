from langchain.text_splitter import RecursiveCharacterTextSplitter

from config import CHUNK_OVERLAP
from config import CHUNK_SIZE


# Divide los documentos en fragmentos pequeños
def split_documents(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
    )
    chunks = text_splitter.split_documents(documents)
    return chunks