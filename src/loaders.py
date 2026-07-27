from langchain_community.document_loaders import PyPDFLoader


# Carga el PDF con la política de BimBamBuy
def load_pdf(pdf_path):
    loader = PyPDFLoader(str(pdf_path))
    documents = loader.load()
    return documents