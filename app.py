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


# Carga las variables de entorno del archivo .env.
load_dotenv()

# Valida que exista la API key de Google Gemini.
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY no está configurada")

# Expone la API key en el entorno para el SDK de Gemini.
os.environ["GOOGLE_API_KEY"] = api_key


# Inicializa el flujo RAG una sola vez al arrancar la app.
def initialize_app():
    # Carga el PDF con las políticas.
    documents = load_pdf(PDF_PATH)
    # Divide el contenido en fragmentos recuperables.
    chunks = split_documents(documents)
    # Crea los embeddings locales.
    embeddings = build_embeddings()
    # Construye o carga el índice vectorial desde disco.
    vectorstore = build_or_load_vectorstore(
        chunks,
        embeddings,
        INDEX_DIR,
    )
    # Prepara la cadena RAG con LLM, retriever y prompt.
    llm, retriever, prompt = build_chain(vectorstore)
    return llm, retriever, prompt


# Se inicializan los componentes una sola vez.
llm, retriever, prompt = initialize_app()


# Procesa cada mensaje del usuario y devuelve la respuesta del bot.
def chat_fn(message, history):
    response = answer_question(
        llm,
        retriever,
        prompt,
        message,
    )
    return response


# Define la interfaz de conversación con Gradio.
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