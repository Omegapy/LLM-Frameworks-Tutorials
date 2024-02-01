-----------------------------------------------------------------------------------------------------------------------------
# Retrieval
-----------------------------------------------------------------------------------------------------------------------------

 Alejandro Ricciardi (Omegapy)  
 created date: 01/23/2024  

Projects Description:  
This project is a series of LangChain data retrieval for LLMs tutorials on Jupyter Notebook.  
The tutorials are a series LangChain Python code examples from the https://python.langchain.com/ website

Specifically from the section [Retrieval](https://python.langchain.com/docs/modules/data_connection/)

⚠️ This project requires an OpenAI key.

-----------------------------------------------------------------------------------------------------------------------------

Requirements:  
- [Python](https://www.python.org/)  
- [Jupyter Notebook](https://jupyter.org/)  
- [LangChain](https://www.langchain.com/) 
- [OpenAI API Key](https://openai.com/) 

 -----------------------------------------------------------------------------------------------------------------------------

My Links:   
- [GitHub](https://github.com/Omegapy)   
- [Facebook](https://www.facebook.com/profile.php?id=100089638857137)  
- [Twitter](https://twitter.com/RicciardiAlex)   
- [Instagram](https://www.instagram.com/alexomegapy/)

-----------------------------------------------------------------------------------------------------------------------------

**Retrieval**

Many LLM applications require user-specific data that is not part of the model's training set. The primary way of accomplishing this is through Retrieval Augmented Generation (RAG). In this process, external data is retrieved and then passed to the LLM when doing the generation step.

LangChain provides all the building blocks for RAG applications - from simple to complex. This section of the documentation covers everything related to the retrieval step - e.g. the fetching of the data. Although this sounds simple, it can be subtly complex. This encompasses several key modules.

<img width="800" src="">

[Document loaders](https://python.langchain.com/docs/modules/data_connection/document_loaders/)   
Document loaders load documents from many different sources. LangChain provides over 100 different document loaders as well as integrations with other major providers in the space, like AirByte and Unstructured. LangChain provides integrations to load all types of documents (HTML, PDF, code) from all types of locations (private S3 buckets, public websites).

[Text Splitting](https://python.langchain.com/docs/modules/data_connection/document_transformers/)  
A key part of retrieval is fetching only the relevant parts of documents. This involves several transformation steps to prepare the documents for retrieval. One of the primary ones here is splitting (or chunking) a large document into smaller chunks. LangChain provides several transformation algorithms for doing this, as well as logic optimized for specific document types (code, markdown, etc).

[Text embedding models](https://python.langchain.com/docs/modules/data_connection/text_embedding/)  
Another key part of retrieval is creating embeddings for documents. Embeddings capture the semantic meaning of the text, allowing you to quickly and efficiently find other pieces of a text that are similar. LangChain provides integrations with over 25 different embedding providers and methods, from open-source to proprietary API, allowing you to choose the one best suited for your needs. LangChain provides a standard interface, allowing you to easily swap between models.

[Vector stores](https://python.langchain.com/docs/modules/data_connection/vectorstores/)  
With the rise of embeddings, there has emerged a need for databases to support efficient storage and searching of these embeddings. LangChain provides integrations with over 50 different vectorstores, from open-source local ones to cloud-hosted proprietary ones, allowing you to choose the one best suited for your needs. LangChain exposes a standard interface, allowing you to easily swap between vector stores.

[Retrievers](https://python.langchain.com/docs/modules/data_connection/retrievers/)  
Once the data is in the database, you still need to retrieve it. LangChain supports many different retrieval algorithms and is one of the places where we add the most value. LangChain supports basic methods that are easy to get started - namely simple semantic search. However, we have also added a collection of algorithms on top of this to increase performance. These include:

- [Parent Document Retriever](https://python.langchain.com/docs/modules/data_connection/retrievers/parent_document_retriever): This allows you to create multiple embeddings per parent document, allowing you to look up smaller chunks but return larger context.
- [Self Query Retriever](https://python.langchain.com/docs/modules/data_connection/retrievers/self_query): User questions often contain a reference to something that isn't just semantic but rather expresses some logic that can best be represented as a metadata filter. Self-query allows you to parse out the semantic part of a query from other metadata filters present in the query.
- {Ensemble Retriever](https://python.langchain.com/docs/modules/data_connection/retrievers/ensemble): Sometimes you may want to retrieve documents from multiple different sources, or using multiple different algorithms. The ensemble retriever allows you to easily do this.
- And more!

[Indexing](https://python.langchain.com/docs/modules/data_connection/indexing)
The LangChain Indexing API syncs your data from any source into a vector store, helping you:
- Avoid writing duplicated content into the vector store
- Avoid re-writing unchanged content
- Avoid re-computing embeddings over unchanged content
- All of which should save you time and money, as well as improve your vector search results.

-----------------------------------------------------------------------------------------------------------------------------

#### Project Map Main
- [Document loaders](#document-loaders)
- [Text Splitters](#text-splitters)
- [Text embedding models](text-embedding-models)
- [Vector stores](#vector-stores)
- [Retrievers](retrievers)
- [Indexing](#indexing)

Notebooks:
- [Document loaders.ipynb]()
- [Text Splitters.ipynb]()
- [Text embedding models.ipynb]()
- [Vector stores.ipynb]()
- [Retrievers.ipynb]()
- [indexing.ipynb]()

-----------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------
# Document loaders
[Document loaders.ipynb]()

-----------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------

Projects Description:  
**LangChain** is a framework for developing applications powered by language models.  
**In this project:** This project is a series of LangChain document loaders for LLMs tutorials on Jupyter Notebook.  
The tutorials are a series LangChain Python code examples from the https://python.langchain.com/ website.

Specifically from the section [Document loaders](https://python.langchain.com/docs/modules/data_connection/document_loaders/) 
 
⚠️ **Info**: Head to [Integrations](https://python.langchain.com/docs/integrations/document_loaders/) for documentation on built-in document loader integrations with 3rd-party tools.

Use document loaders to load data from a source as Document's. A Document is a piece of text and associated metadata. For example, there are document loaders for loading a simple .txt file, for loading the text contents of any web page, or even for loading a transcript of a YouTube video.

Document loaders provide a "load" method for loading data as documents from a configured source. They optionally implement a "lazy load" as well for lazily loading data into memory.

**Project Map:**
- API Key
- Getting started (.txt)
- CSV
    - Base Example
    - Customizing the CSV parsing and loading
    - Specify a column to identify the document source
- File Directory
    - Base Example
    - Show a progress bar
    - Use multithreading
    - Change loader class
        - Base Example
        - Load Python Source Code
    - Auto-detect file encodings with TextLoader
        - A. Default Behavior
        - B. Silent fail
        - C. Auto detect encodings

[Go back to the Project Main Map](#project-map-main)

-----------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------
# Text Splitters
[Text Splitters.ipynb]()

-----------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------

Projects Description:  
**LangChain** is a framework for developing applications powered by language models.  
**In this project:** This project is a series of LangChain text tplitters for LLMs tutorials on Jupyter Notebook.  
The tutorials are a series LangChain Python code examples from the https://python.langchain.com/ website
 
Specifically from the section [Text Splitters](https://python.langchain.com/docs/modules/data_connection/document_transformers/).

**Project Map:**
- API Key


[Go back to the Project Main Map](#project-map-main)

-----------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------
# Text embedding models
[Text embedding models.ipynb]()

-----------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------

Projects Description:  
**LangChain** is a framework for developing applications powered by language models.  
**In this project:** This project is a series of LangChain text embedding models for LLMs tutorials on Jupyter Notebook.  
The tutorials are a series LangChain Python code examples from the https://python.langchain.com/ website.

Specifically from the section [Text embedding models](https://python.langchain.com/docs/modules/data_connection/text_embedding/)

⚠️ **Info**: Head to [Integrations](https://python.langchain.com/docs/integrations/text_embedding/) for documentation on built-in integrations with text embedding model providers.

**Project Map:**
- API Key


[Go back to the Project Main Map](#project-map-main)

-----------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------
# Vector stores
[Vector stores.ipynb]()

-----------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------

Projects Description:  
**LangChain** is a framework for developing applications powered by language models.  
**In this project:** This project is a series of LangChain Vector stores for LLMs tutorials on Jupyter Notebook.  
The tutorials are a series LangChain Python code examples from the https://python.langchain.com/ website.

Specifically from the section [Vector stores](https://python.langchain.com/docs/modules/data_connection/vectorstores/)

⚠️ **Info**: Head to [Integrations](https://python.langchain.com/docs/integrations/vectorstores/) for documentation on built-in integrations with 3rd-party vector stores.

**Project Map:**
- API Key


[Go back to the Project Main Map](#project-map-main)

-----------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------
# Retrievers
[Retrievers.ipynb]()

-----------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------

Projects Description:  
**LangChain** is a framework for developing applications powered by language models.  
**In this project:** This project is a series of LangChain Retrievers for LLMs tutorials on Jupyter Notebook.  
The tutorials are a series LangChain Python code examples from the https://python.langchain.com/ website.

Specifically from the section [Retrievers](https://python.langchain.com/docs/modules/data_connection/retrievers/).

**Project Map:**
- API Key


[Go back to the Project Main Map](#project-map-main)

-----------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------
# Indexing
[Indexing.ipynb]()

-----------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------

Projects Description:  
**LangChain** is a framework for developing applications powered by language models.  
**In this project:** This project is a series of LangChain Indexing for LLMs tutorials on Jupyter Notebook.  
The tutorials are a series LangChain Python code examples from the https://python.langchain.com/ website.

Specifically from the section [Indexing](https://python.langchain.com/docs/modules/data_connection/indexing).

**Project Map:**
- API Key


[Go back to the Project Main Map](#project-map-main)




