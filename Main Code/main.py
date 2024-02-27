from pinecone import Pinecone
from dotenv import load_dotenv
import os
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings

load_dotenv('var.env')
key = os.getenv('OPENAI_API_KEY')
# initialize connection to pinecone (get API key at app.pinecone.io)
api_key = '06adbd3d-ae02-4246-ac25-2039f86cec55'

# configure client
pc = Pinecone(api_key=api_key)


loader = TextLoader("../../modules/state_of_the_union.txt")
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings()
