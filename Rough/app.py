# app.py -----> Overall RAG Functionality
# -----------------WORKING FINE ----------------------#
import os
from dotenv import load_dotenv
from langchain.vectorstores import Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings

from langchain.document_loaders.csv_loader import CSVLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chat_models import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain
import pinecone

load_dotenv('var.env')
key = os.getenv('OPENAI_API_KEY')

file_path = r"C:\Users\Ahmed\Desktop\AISC-RAG\data.csv"


class DocumentOperations:
    def __init__(self, file_path, encoding='utf-8'):
        self.loader = CSVLoader(file_path, encoding=encoding)
        self.data = self.loader.load()

    def split_documents(self):
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000, chunk_overlap=200)
        return text_splitter.split_documents(self.data)


document_ops = DocumentOperations(file_path, encoding='utf-8')
texts = document_ops.split_documents()


class EmbeddingOperations:
    def __init__(self, texts):
        self.embeddings = OpenAIEmbeddings()
        PINECONE_API_KEY = "7bbf5d5b-3838-4803-966b-875738711333"
        PINECONE_API_ENV = "gcp-starter"
        pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_API_ENV)
        self.index_name = "aisc"
        self.docsearch = Pinecone.from_texts(
            [t.page_content for t in texts], self.embeddings, index_name=self.index_name)


embedding_ops = EmbeddingOperations(texts)


class AIOperations:
    def __init__(self, llm):
        self.chain = load_qa_chain(llm, chain_type="stuff")

    def run_chain(self, docs, query):
        return self.chain.run(input_documents=docs, question=query)


llm = ChatOpenAI(temperature=0.2)
ai_ops = AIOperations(llm)

print("\n\n--->Main Start from Here<---\n\n")

while True:
    prompt = input("Enter Prompt: ")
    docs = embedding_ops.docsearch.similarity_search(prompt)
    print("\n")
    print(ai_ops.run_chain(docs, prompt))

    if prompt.upper() == "exit":
        break
