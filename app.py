from src.loader import cargar_documento

RUTA_PDF = "data/PDF_politicas_devoluciones_TiendaBimBamBuy.pdf"


def main():
    documentos = cargar_documento(RUTA_PDF)

    print("=" * 60)
    print("BimBamBuy AI Agent")
    print("=" * 60)

    print(f"Documento cargado correctamente")
    print(f"Páginas cargadas: {len(documentos)}")

    print("\nPrimeros 700 caracteres:\n")

    print(documentos[0].page_content[:700])


if __name__ == "__main__":
    main()