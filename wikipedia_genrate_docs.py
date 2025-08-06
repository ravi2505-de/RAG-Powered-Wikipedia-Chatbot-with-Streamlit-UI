import os
import wikipedia
wikipedia.set_lang("en")
#creating folders to store the documents 
os.makedirs("wikipedia_docs",exist_ok=True)
#topics to search and store 
topics= ["Large language models","BERT tokenizer","LangChain framework","OpenAI","ChatGPT","GPT-3.5","GPT-4.o","Vector databases","FAISS vector store"]
for topic in topics:
    try:
        #searching for the most relevant page 
       search_results = wikipedia.search(topic)
       if not search_results:
         print(f"❌ No match found for: {topic}")
         continue
       best_match= search_results[0]  # Pick top result
       content = wikipedia.page(best_match).content
       filename = f"wikipedia_docs/{best_match.replace(' ', '_')}.txt"
       with open(filename, "w", encoding="utf-8") as file:
            file.write(content)
       print(f"✅ Saved content for {best_match} to {filename}")

    except wikipedia.exceptions.DisambiguationError as e:
        print(f"⚠️ Skipped {topic} due to disambiguation: {e.options}")
    except Exception as e:
        print(f"❌ Error retrieving or saving content for {topic}: {e}")