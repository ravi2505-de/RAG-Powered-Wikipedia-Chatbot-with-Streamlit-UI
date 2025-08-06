import os
from dotenv import load_dotenv
import streamlit as st
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from openai import OpenAI

# Load environment variables
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client and embeddings
client = OpenAI(api_key=openai_api_key)
embedding = OpenAIEmbeddings(openai_api_key=openai_api_key)

# Load the FAISS vector store
vector_store = FAISS.load_local("faiss_index", embedding, allow_dangerous_deserialization=True)

# Streamlit UI
st.set_page_config(page_title="RAG Chat - Wikipedia Bot", page_icon="🧠")
st.title("🔍 Ask Wikipedia using GPT + FAISS")

query = st.text_input("Enter your question:")

if query:
    # Step 1: Get top similar documents from FAISS
    docs = vector_store.similarity_search(query, k=3)
    context = "\n\n".join([doc.page_content for doc in docs])

    # Step 2: Create prompt and call OpenAI
    prompt = f"""Use the context below to answer the question as accurately as possible.\n\nContext:\n{context}\n\nQuestion: {query}\nAnswer:"""

    with st.spinner("Generating answer..."):
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )
        answer = response.choices[0].message.content

    # Step 3: Display the answer
    st.markdown("### 💡 GPT Answer")
    st.write(answer)

   
