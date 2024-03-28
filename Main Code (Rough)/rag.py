from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_pinecone import PineconeVectorStore
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.prompts.prompt import PromptTemplate
from langchain.chains import RetrievalQA
from langchain.memory import ConversationBufferMemory
from langchain_community.document_loaders import DirectoryLoader

from settings import index_name


class RAG:
    def finetune(self, directory_path):
        loader = DirectoryLoader(directory_path)
        documents = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=10000, chunk_overlap=200)
        docs = text_splitter.split_documents(documents)
        embeddings = OpenAIEmbeddings()

        vectbd = PineconeVectorStore.from_documents(
            docs, embeddings, index_name=index_name)
        retriever = vectbd.as_retriever()
        return retriever

    def chat_completion(self, prompt):
        response = chain.invoke(prompt)
        return response['result']


# chain = None  # Initialize outside the class


    def initialize_rag(directory_path):
        global chain
        llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.2)

        template = """
        INSTRUCTIONS: 
        ...
        {question}
        Answer:
        """

        prompt = PromptTemplate(
            input_variables=["history", "context", "question"],
            template=template,
        )

        chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type='stuff',
            retriever=rag.finetune(directory_path),
            chain_type_kwargs={
                "verbose": False,
                "prompt": prompt,
                "memory": ConversationBufferMemory(memory_key="history", input_key="question"),
            }
        )
