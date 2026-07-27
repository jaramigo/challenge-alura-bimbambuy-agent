from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
VECTORSTORE_DIR = BASE_DIR / "vectorstore"
PDF_PATH = DATA_DIR / "PDF_politicas_devoluciones_TiendaBimBamBuy.pdf"
INDEX_DIR = VECTORSTORE_DIR / "faiss_index"
MODEL_NAME = "gemini-flash-latest"
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 150
TOP_K = 4