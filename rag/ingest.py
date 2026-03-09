import os
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import TextLoader

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

docs = []

for file in os.listdir("docs"):

    loader = TextLoader(f"docs/{file}", encoding="utf-8")
    docs.extend(loader.load())

vectordb = FAISS.from_documents(docs, embeddings)

vectordb.save_local("vectorstore")

print("Vector database created successfully")