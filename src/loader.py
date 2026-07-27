from langchain_community.document_loaders import PyPDFLoader


def load_pdf(pdf_path):
    return PyPDFLoader(str(pdf_path)).load()