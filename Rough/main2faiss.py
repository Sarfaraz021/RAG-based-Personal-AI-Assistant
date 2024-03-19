from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader
import os

os.environ["OPENAI_API_KEY"] = "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"


loader = PyPDFLoader(
    r"D:\RAG-based-Personal-AI-Assistant\Main Code\Data\Sarfaraz\Ahmed Cover letter.pdf")
pages = loader.load_and_split()


faiss_index = FAISS.from_documents(pages, OpenAIEmbeddings())
docs = faiss_index.similarity_search(
    "what is written in the sarafarz ahmeds cover letter", k=2)

for doc in docs:
    print(str(doc.metadata["page"]) + ":", doc.page_content[:])
