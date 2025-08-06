from dotenv import load_dotenv
import os
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
import openai
from openai import OpenAI

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
client = OpenAI(api_key=openai_api_key)

#loading the vector store
vector_store = FAISS.load_local("faiss_index", embeddings=embeddings, allow_dangerous_deserialization=True)

#asking a question 
question=input("What is your question? ")
retrieved_docs = vector_store.similarity_search(question, k=2)

#combine retrieved content 
context = "\n".join([doc.page_content for doc in retrieved_docs])

#buliding the prompt
prompt = f"""
use the context below to answer the question.
context: {context}
question: {question}
answer:
"""
response = client.chat.completions.create(
    model="gpt-3.5-turbo",  
    messages=[{"role": "user", "content": prompt}],
    temperature=0.2,
)
#printing the response 
print("\n💡 GPT Answer:")
print(response.choices[0].message.content)

