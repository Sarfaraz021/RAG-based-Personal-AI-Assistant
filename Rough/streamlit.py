# from langchain_community.document_loaders import TextLoader
# from langchain.chat_models import ChatOpenAI
# from langchain.chains.question_answering import load_qa_chain
# from langchain.prompts import PromptTemplate
# from langchain_community.document_loaders import Docx2txtLoader

from pinecone import Pinecone
from dotenv import load_dotenv
from langchain.text_splitter import CharacterTextSplitter, RecursiveCharacterTextSplitter
from langchain_pinecone import PineconeVectorStore
import os
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
import openai
from langchain.prompts.prompt import PromptTemplate
from langchain.chains import RetrievalQA
from langchain.memory import ConversationBufferMemory
from langchain_community.document_loaders import DirectoryLoader
import streamlit as st
load_dotenv('var.env')

os.getenv('OPENAI_API_KEY')
os.getenv("PINECONE_API_KEY")

index_name = os.getenv("PINECONE_INDEX_NAME")
directory_path = r"D:\RAG-based-Personal-AI-Assistant\Main Code\Data\empty"


class RAG:

    def finetune(self, directory_path):

        loader = DirectoryLoader(directory_path)
        documents = loader.load()
        print(f"length of docs : {len(documents)}")
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=10000, chunk_overlap=200)

        docs = text_splitter.split_documents(documents)
        embeddings = OpenAIEmbeddings()

        Pinecone(api_key=os.getenv("PINECONE_API_KEY"),
                 environment='gcp-starter')

        vectbd = PineconeVectorStore.from_documents(
            docs, embeddings, index_name=index_name)
        retriever = vectbd.as_retriever()

        return retriever

    def chat_completion(self, userinput):

        chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type='stuff',
            retriever=rag_1.finetune(directory_path),
            # input_key='query',
            # memory=memory,
            chain_type_kwargs={
                "verbose": False,
                "prompt": prompt,
                "memory": ConversationBufferMemory(
                    memory_key="history",
                    input_key="question"),
            }
        )

        assistant_response = chain.invoke(userinput)
        response = assistant_response['result']
        return response


llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.2)

template = """
INSTRUCTIONS: 

You are a helpful assistant that will respond to my queries/prompts in a professional manner. 

REMEMBER:

You will answer the question, prompt, or query of the user according to the users language. if it is french, you will also answer in french, but if it is english, then you will also follow english and same for other languages.

Such as:

if the query or user input is in French language, then do response in French.
Examples:

    prompt: what is ai?
    Asisstant: AI, or Artificial Intelligence, is like teaching a computer or machine to think and learn like a human. It allows machines to perform tasks that usually require human intelligence, such as recognizing speech, making decisions, and solving problems. Just like humans learn from experience, AI improves over time by learning from data.


Else if the query or user input is in English language, then do response in English.
Examples:
    prompt: Qu'est-ce que l'IA ?
    Asisstant: L'IA, ou Intelligence Artificielle, c'est comme apprendre à un ordinateur ou à une machine à penser et à apprendre comme un humain. Elle permet aux machines d'effectuer des tâches qui nécessitent généralement de l'intelligence humaine, telles que reconnaître la parole, prendre des décisions et résoudre des problèmes. Tout comme les humains apprennent de l'expérience, l'IA s'améliore au fil du temps en apprenant à partir des données.


<ctx>
{context}
</ctx>
------
<hs>
{history}
</hs>
------
{question}
Answer:
"""

prompt = PromptTemplate(
    input_variables=["history", "context", "question"],
    template=template,
)

rag_1 = RAG()  # class object


st.title("RAG Assistant")

choice = st.radio("Choose an option:", ('RAG Assistant', 'Finetune RAG'))

if choice == 'RAG Assistant':
    user_input = st.text_input("Enter your prompt:")
    if st.button("Submit"):
        if user_input:
            # Call your chat_completion method
            response = rag_1.chat_completion(user_input)
            st.text_area(f"AI Assistant: {response}")
        else:
            st.warning("Please enter a prompt.")

elif choice == 'Finetune RAG':
    uploaded_files = st.file_uploader(
        "Choose files for finetuning the RAG:", accept_multiple_files=True, type=['txt', 'docx', 'pdf'])
    if st.button("Finetune"):
        if uploaded_files:
            # Save uploaded files to the specified directory
            for uploaded_file in uploaded_files:
                file_path = os.path.join(directory_path, uploaded_file.name)
                with open(file_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())

            # Call the finetune method with the directory path
            finetuning_message = rag_1.finetune(directory_path)
            st.success(
                "Finetuning done successfully. You can chat with the updated RAG")
            st.info(finetuning_message)

        else:
            st.warning("Please upload files.")
