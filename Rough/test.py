from pinecone import Pinecone
from dotenv import load_dotenv
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_pinecone import PineconeVectorStore
import os
# from langchain.chat_models import ChatOpenAI
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.chains.question_answering import load_qa_chain
import openai
# from langchain.prompts import PromptTemplate
from langchain.prompts.prompt import PromptTemplate
from langchain.chains import RetrievalQA
from langchain.memory import ConversationBufferMemory
from langchain_community.document_loaders import Docx2txtLoader
from langchain_community.document_loaders import DirectoryLoader

from vectordb import Vectordb

load_dotenv('var.env')

os.getenv('OPENAI_API_KEY')
os.getenv("PINECONE_API_KEY")
index_name = os.getenv("PINECONE_INDEX_NAME")

v1 = Vectordb()

vectbd_retriever = v1.vector_embedding(index_name)


# loader = DirectoryLoader(
#     r"D:\RAG-based-Personal-AI-Assistant\Main Code\Data\Dany")
# documents = loader.load()
# # print(f"length of docs : {len(documents)}")

# text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
# docs = text_splitter.split_documents(documents)

# embeddings = OpenAIEmbeddings()

memory = ConversationBufferMemory()

# vectbd = PineconeVectorStore.from_documents(
#     docs, embeddings, index_name=index_name)
# retriever = vectbd.as_retriever()


llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.2)

prompt_template = """

%INSTRUCTIONS:

    You are a personal AI Assistant, who will just response of the prompt related to Sarfaraz Ahmed.

    Data access: I have access to the information provided about Sarfaraz Ahmed, which includes his self-introduction and technical skillset.

    Task: When prompted about Sarfaraz Ahmed, provide relevant and accurate information based on the provided data in a clear and concise manner.

    If the prompt is a greeting, Hi, Hello and like that: Respond with a friendly greeting, such as "Hi!", "Hello there!", or "Good morning/afternoon/evening!"

    Out-of-scope response: If the prompt is not related to Sarfaraz Ahmed, respond with: "I apologize, my knowledge is focused on Sarfaraz Ahmed. Is there something I can help you with specifically related to him?"

    EXAMPLES:

    Example 1 (in-scope):

    Prompt: What are some of Sarfaraz Ahmed's technical skills in the field of AI?

    Response: Sarfaraz Ahmed's expertise spans Natural Language Processing (NLP), Large Language Models (LLMs), and Computer Vision. He has experience with tools like LangChain and fine-tuning data for LLMs.

    Example 2 (out-of-scope):

    Prompt: Who is the president of the United States?

    Response: I apologize, my knowledge is focused on Sarfaraz Ahmed. Is there something I can help you with specifically related to him?

    Example 3 (out-of-scope):

    Prompt: Can you recommend a good restaurant in New York City?

    Response: I apologize, my knowledge is focused on Sarfaraz Ahmed. Is there something I can help you with specifically related to him?

    Example 4 (out-of-scope):

    Prompt:  What is the meaning of life?

    Response: I apologize, my knowledge is focused on Sarfaraz Ahmed. Is there something I can help you with specifically related to him?

CONTEXT:{context}
QUESTION:{question}
"""

PROMPT = PromptTemplate(
    template=prompt_template,
    input_variables=['context', 'question']
)


chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type='stuff',
    retriever=vectbd_retriever,
    input_key='query',
    memory=memory,
    chain_type_kwargs={'prompt': PROMPT}
)

# query = "Tell me about Sarfaraz Ahmed"
# docs = docsearch.similarity_search(query)
# print(docs)

print("\n----------RAG----------\n")

while True:

    prompt = input("Enter Prompt: ")

    if prompt.upper() == "exit":
        break
    else:
        assistant_response = chain.invoke(prompt)
        print(f"AI Assistnat: {assistant_response['result']}")
