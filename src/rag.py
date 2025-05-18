from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OllamaEmbeddings
from langchain.vectorstores import Chroma

def cargar_documento(pdf_path):
    loader = PyPDFLoader(pdf_path)
    documentos = loader.load()
    return documentos

def dividir_documentos(docs):
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    return splitter.split_documents(docs)

def crear_vectores(chunks, persist_dir="chromadb"):
    embedding = OllamaEmbeddings(model="nomic-embed-text")
    vectordb = Chroma.from_documents(chunks, embedding, persist_directory=persist_dir)
    vectordb.persist()
    return vectordb

def cargar_vectores(persist_dir="chromadb"):
    embedding = OllamaEmbeddings(model="nomic-embed-text")
    return Chroma(persist_directory=persist_dir, embedding_function=embedding)