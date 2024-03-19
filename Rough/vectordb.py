from langchain.text_splitter import CharacterTextSplitter
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import DirectoryLoader
from pinecone import Pinecone
import os


class Vectordb:

    def vector_embedding(self, index):

        # Initialize Pinecone connection
        pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"),
                      environment='gcp-starter')

        # Check if the index already exists in Pinecone
        if index in pc.list_indexes():
            # If the index exists, load the existing vector embeddings
            self.vectbd = PineconeVectorStore(index_name=index)
            retriever = self.vectbd.as_retriever()
            print("Using existing embeddings from Pinecone.")
        else:
            # If the index does not exist, generate new embeddings
            self.loader = DirectoryLoader(
                r"D:\RAG-based-Personal-AI-Assistant\Main Code\Data\Sarfaraz")
            self.documents = self.loader.load()
            self.text_splitter = CharacterTextSplitter(
                chunk_size=1000, chunk_overlap=0)
            self.docs = self.text_splitter.split_documents(self.documents)
            self.embeddings = OpenAIEmbeddings()
            self.vectbd = PineconeVectorStore.from_documents(
                self.docs, self.embeddings, index_name=index)
            retriever = self.vectbd.as_retriever()
            print("Generated new embeddings and stored in Pinecone.")

        return retriever
