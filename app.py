import os

import gradio as gr
from dotenv import load_dotenv

from config import INDEX_DIR
from config import PDF_PATH
from src.chain import answer_question
from src.chain import build_chain
from src.embeddings import build_embeddings
from src.loaders import load_pdf
from src.splitter import split_documents
from src.vectorstore import build_or_load_vectorstore


# Carga las variables de entorno
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY no está configurada")

os.environ["GOOGLE_API_KEY"] = api_key


# Inicializa el sistema RAG
def initialize_app():
    documents = load_pdf(PDF_PATH)
    chunks = split_documents(documents)
    embeddings = build_embeddings()
    vectorstore = build_or_load_vectorstore(
        chunks,
        embeddings,
        INDEX_DIR,
    )
    llm, retriever, prompt = build_chain(vectorstore)
    return llm, retriever, prompt


llm, retriever, prompt = initialize_app()


# Procesa cada mensaje del usuario
def chat_fn(message, history):
    response = answer_question(
        llm,
        retriever,
        prompt,
        message,
    )
    return response


iface = gr.ChatInterface(
    fn=chat_fn,
    title="BimBamBuy Assistant",
    description="Asistente sobre políticas de devolución y reembolso.",
)


if __name__ == "__main__":
    iface.launch(
        server_name="127.0.0.1",
        server_port=7860,
        share=True,
    )