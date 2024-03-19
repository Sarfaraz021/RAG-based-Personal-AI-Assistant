import os
from dotenv import load_dotenv

load_dotenv('var.env')

os.getenv('OPENAI_API_KEY')
os.getenv("PINECONE_API_KEY")

index_name = os.getenv("PINECONE_INDEX_NAME")
