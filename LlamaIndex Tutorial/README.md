-----------------------------------------------------------------------------------------------------------------------------
# LlmaIndex Tutorial
-----------------------------------------------------------------------------------------------------------------------------

 Alejandro Ricciardi (Omegapy)  
 created date: 01/03/2024  

-----------------------------------------------------------------------------------------------------------------------------

Projects Description:  
A series of LlamaIndex tutorials based on Udemy - Eden Marco.  
[LlamaIndex- Develop LLM powered applications with LlamaIndex](https://www.udemy.com/course/lamaindex/)  
All the files and folders have been modified from the original source to meet my requirements or to add functionalities to the programs. 
Furthermore, the code lines are heavily commented on; this is a tutorial, after all.

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
- LlamaIndex Doc Helper


-----------------------------------------------------------------------------------------------------------------------------
## HelloWorld
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
-----------------------------------------------------------------------------------------------------------------------------

Projects Description:  
Retrieves LlamaIndex documentation and stores it in a node index.
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
- Data Querying (main.py)
    - Accessing a Pinecone DB
   - Creating a vector store object
   - Store Index in a pinecone vector database
   - Debugging with LlamaIndex call-back feature
   - Create an index object
   - Prompting LLM and getting a response

-----------------------------------------------------------------------------------------------------------------------------
## LlamaIndex Doc Helper - APP
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
      - SentenceEmbeddingOptimizer (LlamaIndex)
      - Custom LlamaIndex node post-processor: DuplicateRemoverNodePostprocessor
   - Prompting LLM and getting a response
   - Implementing Streamlit UI

-----------------------------------------------------------------------------------------------------------------------------
## Agents LlamaIndex
-----------------------------------------------------------------------------------------------------------------------------

Projects Description:  
Using the LlamaIndex ReactAgent method to create a LlamaIndex Agent that writes haiku (Japanese poem) from a given topic.  

[Agents:](https://docs.llamaindex.ai/en/stable/use_cases/agents.html#agents)  
An angent is an automated reasoning and decision engine. It takes in a user input/query  
and can make internal decisions for executing that query in order to return the correct result.  
The key agent components can include, but are not limited to:  
-	Breaking down a complex question into smaller ones  
-	Choosing an external Tool to use + coming up with parameters for calling the Tool  
- Planning out a set of tasks  
-	Storing previously completed tasks in a memory module
  
--- ReAct Agent: it uses a loop and a list of provided tools to react and respond to queries.  
--- OpenAI Agent: OpenAI Agent supports function calling from OpenAI.    
The model is fine-tuned to find the right tool.


[Tools:](https://docs.llamaindex.ai/en/stable/module_guides/deploying/agents/tools/root.html#tools)  
( From LlamaIndex Documentation)   
Having proper tool abstractions is at the core of building data agents.  
Defining a set of Tools is similar to defining any API interface,  
with the exception that these Tools are meant for agent rather than human use.  
We allow users to define both a Tool as well as a ToolSpec containing a series of functions under the hood.  
A Tool implements a very generic interface - simply define __call__  
and also return some basic metadata (name, description, function schema).	  
A Tool Spec defines a full API specification of any service that can be converted into a list of Tools.  
We offer a few different types of Tools:	  
- FunctionTool: A function tool allows users to easily convert any user-defined function into a Tool. It can also auto-infer the function schema.  
-	QueryEngineTool: A tool that wraps an existing query engine. Note: since our agent abstractions inherit from BaseQueryEngine, these tools can also wrap other agents    







