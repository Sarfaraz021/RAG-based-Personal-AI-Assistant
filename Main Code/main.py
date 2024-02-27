from pinecone import Pinecone
from dotenv import load_dotenv
import os
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore


load_dotenv('var.env')
key = os.getenv('OPENAI_API_KEY')
# initialize connection to pinecone (get API key at app.pinecone.io)
api_key = ''

# configure client
pc = Pinecone(api_key=api_key)


loader = TextLoader("Main Code\Data\ahmed.txt")
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings()


index_name = "langchain-test-index"

docsearch = PineconeVectorStore.from_documents(docs, embeddings, index_name=index_name)

query = "What did the president say about Ketanji Brown Jackson"
docs = docsearch.similarity_search(query)
print(docs[0].page_content)
