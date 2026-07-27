# Recupera el contexto más relevante
def retrieve_context(retriever, question):
    docs = retriever.get_relevant_documents(question)
    context_parts = []
    for doc in docs:
        context_parts.append(doc.page_content)
    context = "\n\n".join(context_parts)
    return context