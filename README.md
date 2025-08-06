# 🔍 RAG-Powered Wikipedia Chatbot with Streamlit UI

This project is a Retrieval-Augmented Generation (RAG) pipeline that uses **LangChain**, **FAISS**, and **OpenAI** to build a smart chatbot over Wikipedia articles. It allows you to ask questions and get GPT-4 or GPT-3.5 responses grounded in real context.

---

## 📌 Features

- 🧠 **RAG Architecture** using LangChain
- 📄 Embeds Wikipedia documents with **OpenAIEmbeddings**
- 📦 Fast vector search with **FAISS**
- 🌐 **Streamlit** front-end to chat with your data
- 🔗 Easily extendable to PDFs, APIs, or research papers

---

## 🛠️ Tech Stack

| Layer        | Tools Used                          |
|--------------|--------------------------------------|
| LLM          | OpenAI GPT-3.5 / GPT-4               |
| Retrieval    | LangChain + FAISS                    |
| UI           | Streamlit                            |
| Data Source  | Wikipedia (via `wikipedia` Python lib) |
| Auth         | `.env` for API key management        |

---

## 📂 Project Structure

📁 rag-wiki-chatbot/
│
├── 📁 wikipedia_docs/ # Raw .txt files from Wikipedia
├── 📁 faiss_index/ # Vector DB saved locally
│
├── 📄 embed_wiki.py # Script to embed and store documents
├── 📄 query_wiki.py # Script to test similarity search + GPT
├── 📄 streamlit_app.py # Streamlit UI
├── 📄 .env # Your OpenAI API key
├── 📄 requirements.txt # All dependencies
└── 📄 README.md # This file


---

## ✅ Setup Instructions

### 1. Clone the Repo
```
git clone https://github.com/your-username/rag-wiki-chatbot.git
cd rag-wiki-chatbot

2. Install Dependencies
pip install -r requirements.txt

3. Add .env File
Create a file named .env in the root directory with this:
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxx

4. Run Streamlit App
streamlit run streamlit_app.py

If streamlit isn't recognized, use:
python -m streamlit run streamlit_app.py

🔄 Future Improvements
 PDF & CSV document support

 Streamlit Cloud deployment

 Chat history + feedback logging

 API data ingestion (real-time RAG)

📃 License
MIT License – free to use, modify, and build on!

👋 Author
Built with ❤️ by Ravi M

---

### ✅ Next Steps for You

- ✅ Add this to `README.md`
- ✅ Push everything to GitHub
- ✅ Drop me your repo if you'd like a badge or CI tips

Want me to generate a badge, GitHub Actions workflow, or setup for Streamlit Cloud? Just say the word 👨‍💻
