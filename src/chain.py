from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

from config import MODEL_NAME, TOP_K
from src.prompts import SYSTEM_PROMPT


def build_chain(vectorstore):
    # Inicializa Gemini con el stack moderno compatible con Pydantic v2.
    llm = ChatGoogleGenerativeAI(
        model=MODEL_NAME,
        temperature=0.2,
    )

    # Crea el retriever para buscar contexto relevante dentro del vector store.
    retriever = vectorstore.as_retriever(
        search_kwargs={"k": TOP_K},
    )

    # Define el prompt de sistema y la entrada del usuario.
    prompt = ChatPromptTemplate.from_messages([
        ("system", SYSTEM_PROMPT),
        ("human", "Contexto:\n{context}\n\nPregunta:\n{question}"),
    ])

    return llm, retriever, prompt


def answer_question(llm, retriever, prompt, question):
    # Recupera los documentos más relevantes usando la API moderna.
    docs = retriever.invoke(question)

    # Une el contenido recuperado para pasarlo al modelo.
    context = "\n\n".join(doc.page_content for doc in docs)

    # Construye los mensajes finales para Gemini.
    messages = prompt.format_messages(
        context=context,
        question=question,
    )

    # Genera la respuesta final.
    response = llm.invoke(messages)
    return response.content