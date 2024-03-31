# from pinecone import Pinecone
# from dotenv import load_dotenv
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain_pinecone import PineconeVectorStore
# import os
# from langchain_openai import ChatOpenAI, OpenAIEmbeddings
# from langchain.prompts.prompt import PromptTemplate
# from langchain.chains import RetrievalQA
# from langchain.memory import ConversationBufferMemory
# from langchain_community.document_loaders import DirectoryLoader
# load_dotenv('var.env')

# os.getenv('OPENAI_API_KEY')
# os.getenv("PINECONE_API_KEY")

# index_name = os.getenv("PINECONE_INDEX_NAME")


# class RAG:

#     def finetune(self, directory_path):

#         loader = DirectoryLoader(directory_path)
#         documents = loader.load()
#         print(f"length of docs : {len(documents)}")
#         text_splitter = RecursiveCharacterTextSplitter(
#             chunk_size=10000, chunk_overlap=200)

#         docs = text_splitter.split_documents(documents)
#         embeddings = OpenAIEmbeddings()

#         Pinecone(api_key=os.getenv("PINECONE_API_KEY"),
#                  environment='gcp-starter')

#         vectbd = PineconeVectorStore.from_documents(
#             docs, embeddings, index_name=index_name)
#         retriever = vectbd.as_retriever()

#         return retriever

#     def chat_completion(self):

#         while True:

#             prompt = input("Enter Prompt: ")
#             print("")

#             if prompt.upper() == "exit":
#                 print("Thanks!!")
#                 break

#             else:
#                 assistant_response = chain.invoke(prompt)
#                 print(f"AI Assistnat: {assistant_response['result']}")
#                 print("*********************************")


# rag_1 = RAG()  # class object

# llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.2)

# template = """
# INSTRUCTIONS:

# You are a helpful assistant that will respond to my queries/prompts in a professional manner. You will answer the question, prompt, or query of the user in the French language if the user's prompt, query, or input is in French, and vice versa for all other languages.

# Such as:

# Else if the query or user input is in English language, then do response in English.
# For Examples:
#     prompt: what is ai?
#     Asisstant: AI, or Artificial Intelligence, is like teaching a computer or machine to think and learn like a human. It allows machines to perform tasks that usually require human intelligence, such as recognizing speech, making decisions, and solving problems. Just like humans learn from experience, AI improves over time by learning from data.


# if the query or user input is in French language, then do response in French.
#  For Examples:
#     prompt: Qu'est-ce que l'IA ?
#     Asisstant: L'IA, ou Intelligence Artificielle, c'est comme apprendre à un ordinateur ou à une machine à penser et à apprendre comme un humain. Elle permet aux machines d'effectuer des tâches qui nécessitent généralement de l'intelligence humaine, telles que reconnaître la parole, prendre des décisions et résoudre des problèmes. Tout comme les humains apprennent de l'expérience, l'IA s'améliore au fil du temps en apprenant à partir des données.

# And follow this for all other langauges.

# <ctx>
# {context}
# </ctx>
# ------
# <hs>
# {history}
# </hs>
# ------
# {question}
# Answer:
# """

# prompt = PromptTemplate(
#     input_variables=["history", "context", "question"],
#     template=template,
# )

# directory_path = r"D:\RAG-based-Personal-AI-Assistant\Main Code\Data\empty"

# chain = RetrievalQA.from_chain_type(
#     llm=llm,
#     chain_type='stuff',
#     retriever=rag_1.finetune(directory_path),
#     chain_type_kwargs={
#         "verbose": False,
#         "prompt": prompt,
#         "memory": ConversationBufferMemory(
#             memory_key="history",
#             input_key="question"),
#     }
# )


# print("----------RAG----------\n")

# while True:
#     print("\n*******************************")
#     choice = input("Enter 1 for RAG Assistant or 2 to Finetune RAG: ")

#     try:
#         choice_int = int(choice)
#         if choice_int == 1:
#             rag_1.chat_completion()
#         elif choice_int == 2:
#             path = input(
#                 "Enter Directory path to finetune the RAG: ")
#             rag_1.finetune(path)
#             print(
#                 "\nFinetuning done Successfully. Now you can chat the updated RAG Asisstant\n")
#             print("*******************************")
#             rag_1.chat_completion()
#         else:
#             print("Invalid choice. Please enter 1 or 2.")
#     except ValueError:
#         print("Please enter a numerical value.")

# from langchain_community.document_loaders import TextLoader
# from langchain_openai import OpenAIEmbeddings
# from langchain.text_splitter import CharacterTextSplitter
# import openai
# import os
# openai.api_key = "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"
# os.environ["OPENAI_API_KEY"] = openai.api_key
# file_path = r"D:\RAG-based-Personal-AI-Assistant\roshni.txt"
# loader = TextLoader(file_path, encoding="utf-8")
# documents = loader.load()
# text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
# docs = text_splitter.split_documents(documents)

# embeddings = OpenAIEmbeddings()
