from langchain_community.document_loaders import PyPDFLoader


def cargar_documento(ruta_pdf: str):
    loader = PyPDFLoader(ruta_pdf)
    documentos = loader.load()

    return documentos