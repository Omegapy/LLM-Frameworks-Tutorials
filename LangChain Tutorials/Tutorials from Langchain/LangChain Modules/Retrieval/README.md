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

<img width="800" src="https://github.com/Omegapy/LLM-Frameworks-Tutorials/blob/main/LangChain%20Tutorials/Tutorials%20from%20Langchain/LangChain%20Modules/Retrieval/pic/data_connection.jpg">

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

Notebooks:
- [Document loaders.ipynb](https://github.com/Omegapy/LLM-Frameworks-Tutorials/blob/main/LangChain%20Tutorials/Tutorials%20from%20Langchain/LangChain%20Modules/Retrieval/Document%20loaders.ipynb)
- [Text Splitters.ipynb](https://github.com/Omegapy/LLM-Frameworks-Tutorials/blob/main/LangChain%20Tutorials/Tutorials%20from%20Langchain/LangChain%20Modules/Retrieval/Text%20Splitters.ipynb)
- [Text embedding models.ipynb](https://github.com/Omegapy/LLM-Frameworks-Tutorials/blob/main/LangChain%20Tutorials/Tutorials%20from%20Langchain/LangChain%20Modules/Retrieval/Text%20embedding%20models.ipynb)

-----------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------
# Document loaders
[Document loaders.ipynb](https://github.com/Omegapy/LLM-Frameworks-Tutorials/blob/main/LangChain%20Tutorials/Tutorials%20from%20Langchain/LangChain%20Modules/Retrieval/Document%20loaders.ipynb)

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
        - C. Auto-detect encodings

[Go back to the Project Main Map](#project-map-main)

-----------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------
# Text Splitters
[Text Splitters.ipynb](https://github.com/Omegapy/LLM-Frameworks-Tutorials/blob/main/LangChain%20Tutorials/Tutorials%20from%20Langchain/LangChain%20Modules/Retrieval/Text%20Splitters.ipynb)

-----------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------

Projects Description:  
**LangChain** is a framework for developing applications powered by language models.  
**In this project:** This project is a series of LangChain text tplitters for LLMs tutorials on Jupyter Notebook.  
The tutorials are a series LangChain Python code examples from the https://python.langchain.com/ website
 
Specifically from the section [Text Splitters](https://python.langchain.com/docs/modules/data_connection/document_transformers/).

Once you've loaded documents, you'll often want to transform them to better suit your application. The simplest example is you may want to split a long document into smaller chunks that can fit into your model's context window. LangChain has a number of built-in document transformers that make it easy to split, combine, filter, and otherwise manipulate documents.

When you want to deal with long pieces of text, it is necessary to split up that text into chunks. As simple as this sounds, there is a lot of potential complexity here. Ideally, you want to keep the semantically related pieces of text together. What "semantically related" means could depend on the type of text. This notebook showcases several ways to do that.

At a high level, text splitters work as following:

1. Split the text up into small, semantically meaningful chunks (often sentences).
2. Start combining these small chunks into a larger chunk until you reach a certain size (as measured by some function).
3. Once you reach that size, make that chunk its own piece of text and then start creating a new chunk of text with some overlap (to keep context between chunks).

That means there are two different axes along which you can customize your text splitter:
1. How the text is split
2. How the chunk size is measured

**Types of Text Splitters**
LangChain offers many different types of text splitters. Below is a table listing all of them, along with a few characteristics:

**Name**: Name of the text splitter

**Splits On**: How this text splitter splits text

**Adds Metadata**: Whether or not this text splitter adds metadata about where each chunk came from.

**Description**: Description of the splitter, including recommendation on when to use it.

<table><thead><tr><th>Name</th><th>Splits On</th><th>Adds Metadata</th><th>Description</th></tr></thead><tbody><tr><td>Recursive</td><td>A list of user defined characters</td><td></td><td>Recursively splits text. Splitting text recursively serves the purpose of trying to keep related pieces of text next to each other. This is the recommended way to start splitting text.</td></tr><tr><td>HTML</td><td>HTML specific characters</td><td>✅</td><td>Splits text based on HTML-specific characters. Notably, this adds in relevant information about where that chunk came from (based on the HTML)</td></tr><tr><td>Markdown</td><td>Markdown specific characters</td><td>✅</td><td>Splits text based on Markdown-specific characters. Notably, this adds in relevant information about where that chunk came from (based on the Markdown)</td></tr><tr><td>Code</td><td>Code (Python, JS) specific characters</td><td></td><td>Splits text based on characters specific to coding languages. 15 different languages are available to choose from.</td></tr><tr><td>Token</td><td>Tokens</td><td></td><td>Splits text on tokens. There exist a few different ways to measure tokens.</td></tr><tr><td>Character</td><td>A user defined character</td><td></td><td>Splits text based on a user defined character. One of the simpler methods.</td></tr><tr><td>[Experimental] Semantic Chunker</td><td>Sentences</td><td></td><td>First splits on sentences. Then combines ones next to each other if they are semantically similar enough. Taken from <a href="https://github.com/FullStackRetrieval-com/RetrievalTutorials/blob/main/5_Levels_Of_Text_Splitting.ipynb" target="_blank" rel="noopener noreferrer">Greg Kamradt</a></td></tr></tbody></table>

**Evaluate text splitters**
You can evaluate text splitters with the [Chunkviz utility](https://chunkviz.up.railway.app/) created by Greg Kamradt. ```Chunkviz``` is a great tool for visualizing how your text splitter is working. It will show you how your text is being split up and help in tuning up the splitting parameters.

**Other Document Transforms**
Text splitting is only one example of transformations that you may want to do on documents before passing them to an LLM. Head to Integrations for documentation on built-in document transformer [integrations](https://python.langchain.com/docs/integrations/document_transformers/) with 3rd-party tools.

**Project Map:**
- API Key
- HTMLHeaderTextSplitter
    - Base Example
    - Limitations
- Split by character
- Split code
    - Python
    - JS
    - TS
    - Markdown
    - Latex
    - HTML
    - Solidity
    - c
- MarkdownHeaderTextSplitter
- Recursively split by character
- Semantic Chunking
- Split by tokens
    - tiktoken
    - spaCy
    - SentenceTransformers
    - NTLK
    - Hugging Face tokenizer

[Go back to the Project Main Map](#project-map-main)

-----------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------
# Text embedding models
[Text embedding models.ipynb](https://github.com/Omegapy/LLM-Frameworks-Tutorials/blob/main/LangChain%20Tutorials/Tutorials%20from%20Langchain/LangChain%20Modules/Retrieval/Text%20embedding%20models.ipynb)

-----------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------

Projects Description:  
**LangChain** is a framework for developing applications powered by language models.  
**In this project:** This project is a series of LangChain text embedding models for LLMs tutorials on Jupyter Notebook.  
The tutorials are a series LangChain Python code examples from the https://python.langchain.com/ website.

Specifically from the section [Text embedding models](https://python.langchain.com/docs/modules/data_connection/text_embedding/)

The ```Embeddings class``` is a class designed for interfacing with text embedding models. There are lots of embedding model providers (OpenAI, Cohere, Hugging Face, etc) - this class is designed to provide a standard interface for all of them.

Embeddings create a vector representation of a piece of text. This is useful because it means we can think about text in the vector space, and do things like semantic search where we look for pieces of text that are most similar in the vector space.

The base Embeddings class in LangChain provides two methods: one for embedding documents and one for embedding a query. The former takes as input multiple texts, while the latter takes a single text. The reason for having these as two separate methods is that some embedding providers have different embedding methods for documents (to be searched over) vs queries (the search query itself).

⚠️ **Info**: Head to [Integrations](https://python.langchain.com/docs/integrations/text_embedding/) for documentation on built-in integrations with text embedding model providers.

**Project Map:**
- API Key
- Get started
- CacheBackedEmbeddings
    - Using with a Vector Store
    - Swapping the ByteStore


[Go back to the Project Main Map](#project-map-main)




