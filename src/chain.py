from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

from config import MODEL_NAME
from config import TOP_K
from src.prompts import SYSTEM_PROMPT


# Crea la cadena RAG
def build_chain(vectorstore):
    llm = ChatGoogleGenerativeAI(
        model=MODEL_NAME,
        temperature=0.2,
    )
    retriever = vectorstore.as_retriever(
        search_kwargs={"k": TOP_K},
    )
    prompt = ChatPromptTemplate.from_messages([
        ("system", SYSTEM_PROMPT),
        ("human", "Contexto:\n{context}\n\nPregunta:\n{question}"),
    ])
    return llm, retriever, prompt


# Responde una pregunta usando el contexto recuperado
def answer_question(llm, retriever, prompt, question):
    docs = retriever.get_relevant_documents(question)
    context = "\n\n".join(doc.page_content for doc in docs)
    messages = prompt.format_messages(
        context=context,
        question=question,
    )
    response = llm.invoke(messages)
    return response.content