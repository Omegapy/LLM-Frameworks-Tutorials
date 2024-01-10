-----------------------------------------------------------------------------------------------------------------------------
LlamaIndex Doc Helper - APP
-----------------------------------------------------------------------------------------------------------------------------

 Alejandro Ricciardi (Omegapy)  
 created date: 01/05/2024 

Credit:  
Udemy - Eden Marco.  
[LlamaIndex- Develop LLM powered applications with LlamaIndex](https://www.udemy.com/course/lamaindex/)  
All the files and folders have been modified from the original source to meet my requirements or to add functionalities to the programs. 
Furthermore, the code lines are heavily commented on; this is a tutorial, after all.

-----------------------------------------------------------------------------------------------------------------------------

Projects Description:  
LlamaIndex Doc Helper - APP is a chatbot document assistant that provides information about LlamaIndex based on the LlamaIndex documentation.  
The program implements Retrieval Augmented Generation (RAG) to generate inquiry responses.
- Create pipenv (Virtual environment) 
- Install dependencies
- Retrieval
- Download Script (download_docs.py) downloads the LlamaIndex Docs from link
    - You can use the script to download/create a LlamaIndex Doc. folder
    - Or you can unzip the provided llamaindex-docs.zip
- UDownload LlamaIndex Documentation
- Data Index (injection.py)
    - Separates LlamaIndex Doc data into chucks
    - Vector Indexing - Embedding With OpenAI
    - Store Index in a pinecone vector database
- Implementing Node post-processing Streamlit user interface (UI) 
   - Accessing a Pinecone DB
   - Creating a vector store object
   - Store Index in a pinecone vector database
   - Debugging with LlamaIndex call-back feature
   - Create an index object
   - Node post-processing:
      - SentenceEmbeddingOptimizer (llamaIndex)
      - Custom LlamaIndex node post-processor: DuplicateRemoverNodePostprocessor
   - Prompting LLM and getting a response
   - Implementing Streamlit UI

-----------------------------------------------------------------------------------------------------------------------------

Requirements:  
- [Python](https://www.python.org/)   
- [LlamaIndex](https://www.llamaindex.ai/)  
- [OpenAI API](https://openai.com/)  

-----------------------------------------------------------------------------------------------------------------------------

My Links:   
- [GitHub](https://github.com/Omegapy)   
- [Facebook](https://www.facebook.com/profile.php?id=100089638857137)  
- [Twitter](https://twitter.com/RicciardiAlex)   
- [Instagram](https://www.instagram.com/alexomegapy/)   






