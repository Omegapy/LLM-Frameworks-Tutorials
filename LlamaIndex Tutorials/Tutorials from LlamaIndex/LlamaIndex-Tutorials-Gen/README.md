-----------------------------------------------------------------------------------------------------------------------------
LlamaIndex Tutorials
-----------------------------------------------------------------------------------------------------------------------------


 Alejandro Ricciardi (Omegapy)  
 created date: 12/23/2023  

-----------------------------------------------------------------------------------------------------------------------------
Projects Description:

This repository is a series of LlamaIndex Tutorials on Jupyter Notebook.  
The tutorials are based on LlamaIndex Discover LlamaIndex YouTube video series.  
https://www.youtube.com/playlist?list=PLTZkGHtR085ZjK1srrSZIrkeEzQiMjO9W

-----------------------------------------------------------------------------------------------------------------------------
Requirements:  
Python: https://www.python.org/  
Jupyter Notebook: https://jupyter.org/  
LlamaIndex: https://www.llamaindex.ai/  
OpenAI API Key: https://openai.com/  

-----------------------------------------------------------------------------------------------------------------------------

Links:   
GitHub: https://github.com/Omegapy   
Facebook: https://www.facebook.com/profile.php?id=100089638857137  
Twitter: https://twitter.com/RicciardiAlex  
Instagram: https://www.instagram.com/alexomegapy/

-----------------------------------------------------------------------------------------------------------------------------
 Projects map:  
 
Jupyter Notebooks LlamaIndex Tutorials:
- LlamaIndex LLMs-Prompts.ipynb
- LlamaIndex Doc-Metadata.ipynp

Folders:
- Doc (document/data)
- llama_docs_bot (Python files)
-----------------------------------------------------------------------------------------------------------------------------

#### 1. LlamaIndex LLMs-Prompts: LlamaIndex Intro. Tutorial (1- LlamaIndex LLMs-Prompts.ipynb)
-----------------------------------------------------------------------------------------------------------------------------
Testing an LLM using the primary prompt templates used in LlamaIndex.  
LlamaIndex LLMs-Prompts tutorial based on LlamaIndex Bottoms-Up Development video series

- Initialization 
    - API Keys
    - LLM Init.
    - Load File

- Templates
    - Context
    - Refined Context - More Context

- Chat
    - Simulate a ChatBot that can answer questions about llama-index.

Credit: LlamaIndex https://www.youtube.com/watch?v=p0jcvGiBKSA&t=201s

-----------------------------------------------------------------------------------------------------------------------------

#### 2. LlamaIndex Doc-Metadata: LlamaIndex Intro. Tutorial (2- LlamaIndex Doc-Metadata.ipynb)
-----------------------------------------------------------------------------------------------------------------------------
Load data and create document objects in LlamaIndex. Specifically markdown files for now. And read Metadata.  

Initialization
- For markdown Docs. Reader see llama_docs_bot/markdown_docs_reader.py (it Extract text from markdown files into Document objects.)
- Load markdown docs from a director function
- loads project documents from each folder

Read Metadata
- MetadataMode makes printed files look nice
- Improve the Metadata print formatting 

Metadata Printing Advanced Customization
- Hide the File Name from the LLM
- Hide the File Name from the Embedding Model 

credit: LlamaIndex https://www.youtube.com/watch?v=nGNoacku0YY

-----------------------------------------------------------------------------------------------------------------------------

#### 3. Evaluation Baseline LLM: LlamaIndex Intro. Tutorial (3- Evaluation Baseline LLM.ipynb)
-----------------------------------------------------------------------------------------------------------------------------
Using LlamaIndex to evaluate an LLM query with the following two main evaluations:
- ResponseSourceEvaluator:
    - uses an LLM to decide if the response is similar enough to the sources 
        - a good measure for hallucination detection!
- QueryResponseEvaluator:
    - uses an LLM to decide if a response is similar enough to the original query 
        - a good measure for checking if the query was answered!

Project Map:

- API Key
- Loading Docs
    - load_markdown_docs() Function
    - Load documents from each folder.
- Create the indices
   - Create a vector store index for each folder 
- Create Query Engine Tools
    - Create a Unified Query Engine
- Test the Query Engine
    - Evaluate the Baseline
        - Generate the Dataset
        - Evaluate with the Dataset
        - Investigating Hallucinations
        - Generating response from a known hallucinated_questions
    
Credit: LlamaIndex https://www.youtube.com/watch?v=2c64G-iDJKQ

-----------------------------------------------------------------------------------------------------------------------------

#### 4. Embeddings LlamaIndex-OpenAI: LlamaIndex Intro. Tutorial (4- Embeddings LlamaIndex-OpenAI.ipynb)
-----------------------------------------------------------------------------------------------------------------------------
Projects Description:
Embeddings are numerical representations of text. To generate embeddings for text, a specific model is required.

In LlamaIndex, the default embedding model is text-embedding-ada-002 from OpenAI.  
You can also leverage any embedding models offered by Langchain and Huggingface using our LangchainEmbedding wrapper.

credit: LlamaIndex https://www.youtube.com/watch?v=2c64G-iDJKQ&t=47s
