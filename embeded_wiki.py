import os 
from dotenv import load_dotenv
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter

#load open AI Api key 
load_dotenv()
openai_api_key=os.getenv("OPENAI_API_KEY")
embeddings=OpenAIEmbeddings(openai_api_key=openai_api_key)
#preparing for chunking and metadata tracking 
docs_folder= "wikipedia_docs"
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)

all_chunks = []
all_metadata = []

# Loop through all files in the docs folder
for filename in os.listdir(docs_folder):
    if filename.endswith(".txt"):
        file_path = os.path.join(docs_folder, filename)
        with open(file_path, 'r', encoding='utf-8') as file:
            raw_text = file.read()

        # Split the text into chunks
        chunks = text_splitter.split_text(raw_text)

        # Add chunks and metadata to the lists
        all_chunks.extend(chunks)
        all_metadata.extend([{"source": filename}] * len(chunks))

# Optional: Sanitize chunks (remove empty or non-string entries)
cleaned_chunks = []
cleaned_metadata = []
for chunk, meta in zip(all_chunks, all_metadata):
    if isinstance(chunk, str) and chunk.strip():
        cleaned_chunks.append(chunk)
        cleaned_metadata.append(meta)

# Embed and store in FAISS
vector_store = FAISS.from_texts(cleaned_chunks, embedding=embeddings, metadatas=cleaned_metadata)
vector_store.save_local("faiss_index")

print("✅ Embedding and storing completed successfully.")
print(f"✅ Stored {len(cleaned_chunks)} chunks from {len(os.listdir(docs_folder))} Wikipedia articles.")
# The code reads text files from a specified directory, splits the text into manageable chunks, embeds them using OpenAI's embeddings, and stores them in a FAISS vector store for efficient retrieval. It also tracks metadata for each chunk to maintain context.