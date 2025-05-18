import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from dotenv import load_dotenv
load_dotenv()
from src.rag import cargar_documento, dividir_documentos, crear_vectores, cargar_vectores
from langchain.chat_models import ChatOllama
from langchain.vectorstores.base import VectorStoreRetriever
from langchain.prompts import PromptTemplate
from langchain.chains.question_answering import load_qa_chain
from langsmith import traceable
from langchain.callbacks.tracers.langchain import LangChainTracer


st.set_page_config(page_title="Chat con tu PDF", page_icon="📄")
st.title("Chatbot con RAG ")

uploaded_file = st.file_uploader("Sube tu PDF", type=["pdf"])

if uploaded_file:
    pdf_path = f"./data/{uploaded_file.name}"
    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.read())

    with st.spinner("Procesando documento..."):
        docs = cargar_documento(pdf_path)
        chunks = dividir_documentos(docs)
        db = crear_vectores(chunks)

    st.success("Documento cargado y procesado correctamente.")

    query = st.text_input("Haz tu pregunta sobre el documento:")
    if query:
        with st.spinner("Pensando... generando respuesta"):
            # Inicializar modelo y prompt
            model = ChatOllama(model="qwen:7b-chat", temperature=0.4, top_p=0.9)

            custom_prompt = PromptTemplate(
                input_variables=["context", "question"],
                template="""
Responde en español de manera clara y detallada usando únicamente el siguiente contexto. Si no puedes responder con base en el contexto, di que no sabes.

Contexto:
{context}

Pregunta: {question}
Respuesta:
"""
            )

            tracer = LangChainTracer(project_name=os.getenv("LANGCHAIN_PROJECT"))

            retriever = db.as_retriever(search_type="mmr", search_kwargs={"k": 10, "lambda_mult": 0.7})
            documentos_relevantes = retriever.get_relevant_documents(query)
            # Eliminar duplicados exactos
            documentos_relevantes = list({doc.page_content: doc for doc in documentos_relevantes}.values())

            # Mostrar en consola el contexto usado
            for i, doc in enumerate(documentos_relevantes):
                print(f"\n--- Documento {i + 1} ---\n{doc.page_content[:500]}")

            qa_chain = load_qa_chain(llm=model, chain_type="stuff", prompt=custom_prompt)
            respuesta = qa_chain.run(
                input_documents=documentos_relevantes,
                question=query,
                callbacks=[tracer]
            )

        st.success("¡Respuesta generada!")
        st.markdown(f"**Respuesta:** {respuesta}")