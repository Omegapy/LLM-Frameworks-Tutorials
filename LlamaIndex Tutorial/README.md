-----------------------------------------------------------------------------------------------------------------------------
# LlmaIndex Tutorial
-----------------------------------------------------------------------------------------------------------------------------

 Alejandro Ricciardi (Omegapy)  
 created date: 01/03/2024  

-----------------------------------------------------------------------------------------------------------------------------

Projects Description:  
A series of LlamaIndex from Udemy - Eden Marco.  
[LlamaIndex- Develop LLM powered applications with LlamaIndex](https://www.udemy.com/course/lamaindex/)  

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

-----------------------------------------------------------------------------------------------------------------------------

Folders:
- HelloWorld
- LlamaIndex Hello World
- LlamaIndex Doc Helper5


-----------------------------------------------------------------------------------------------------------------------------
## HelloWorld
Folder: HelloWorld
-----------------------------------------------------------------------------------------------------------------------------

Projects Description:  
Create a python environment.  
Initialize projects with pipenv.  
[Pipenv Crash Course](https://www.youtube.com/watch?v=6Qmnh5C4Pmo) 

In Console:  
Install dependencies (if not installed):  
```
python --version
pip3 install pipenv
pipenv --version
```
Create and Initialize pipenv:
``` 
pipenv shell
```
Install Packages:
```
pipenv install llama-index python-dotenv
```
Create a main.py and a .env files:
```
echo>main.
```
Safety Check:
```
pipenv check
```
Launch IDE:  
PyCharm in my case

-----------------------------------------------------------------------------------------------------------------------------
## LlamaIndex Hello World
Folder: LlamaIndex Hello World
-----------------------------------------------------------------------------------------------------------------------------

Projects Description:  
- Load WebPage (dataConnector)

- Store it in an index
- Create a query Engine
- Ask questions about the webpage
- Use the LlamaIndex function:
    - SimpleWebReader
    - VectoreStoreIndex
    - QueryEngine

-----------------------------------------------------------------------------------------------------------------------------
## LlamaIndex Doc Helper
Folder: LlamaIndex Doc Helper
-----------------------------------------------------------------------------------------------------------------------------

Projects Description:  
- Create pipenv (Virtial environment) 
- Install dependencies
- Retrieval
- Download Script (download_docs.py) downloads the LlamaIndex Docs from link
    - You can use the script to download/create a LlamaIndex Doc. folder
    - Or you can unzip the provided llamaindex-docs.zip
- UDownload LlamaIndex Documentation
- Data Index Injection Program
    - Separates LlamaIndex Doc data into chucks
    - Vector Indexing - Embedding With OpenAI
    - Store Index in a pinecone vector database

