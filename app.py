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