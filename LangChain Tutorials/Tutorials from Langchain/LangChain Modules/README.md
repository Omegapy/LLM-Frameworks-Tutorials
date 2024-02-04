-----------------------------------------------------------------------------------------------------------------------------
# LangChain Modules
-----------------------------------------------------------------------------------------------------------------------------

 Alejandro Ricciardi (Omegapy)  
 created date: 01/22/2024  

Projects Description:  
This project is a series of LangChain Modules tutorials on Jupyter Notebook.  
The tutorials are a series LangChain Python code examples from the https://python.langchain.com/ website

Specifically from the section [Modules](https://python.langchain.com/docs/modules)

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

#### Project Map Main
- [Model IO](#model-io)
- [Retrieval](#retrieval)
- [Agents](#agents)

Directory:
- [Model IO](https://github.com/Omegapy/LLM-Frameworks-Tutorials/tree/main/LangChain%20Tutorials/Tutorials%20from%20Langchain/LangChain%20Modules/Model%20IO)
- [Retrieval](https://github.com/Omegapy/LLM-Frameworks-Tutorials/tree/main/LangChain%20Tutorials/Tutorials%20from%20Langchain/LangChain%20Modules/Retrieval)
- [Agents](https://github.com/Omegapy/LLM-Frameworks-Tutorials/tree/main/LangChain%20Tutorials/Tutorials%20from%20Langchain/LangChain%20Modules/Agents)

-----------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------
# Model IO
[Model IO](https://github.com/Omegapy/LLM-Frameworks-Tutorials/tree/main/LangChain%20Tutorials/Tutorials%20from%20Langchain/LangChain%20Modules/Model%20IO)

-----------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------

Projects Description:  
**LangChain** is a framework for developing applications powered by language models.  
**In this project:**  
I explore the concept Model i/o, the core element of any language model application is...the model.   
LangChain gives you the building blocks to interface with any language model.

<img width="800" src="https://github.com/Omegapy/LLM-Frameworks-Tutorials/blob/main/LangChain%20Tutorials/Tutorials%20from%20Langchain/LangChain%20Modules/Model%20IO/pic/model_io.jpg">

[Conceptual Guide](https://python.langchain.com/docs/modules/model_io/concepts)  
A conceptual explanation of messages, prompts, LLMs vs ChatModels, and output parsers. You should read this before getting started.  
[Quickstart](https://python.langchain.com/docs/modules/model_io/quick_start)  
Covers the basics of getting started working with different types of models. You should walk through [this section]( https://python.langchain.com/docs/modules/model_io/output_parsers/) if you want to get an overview of the functionality.  
[Prompts](https://python.langchain.com/docs/modules/model_io/prompts/)  
This section deep dives into the different types of prompt templates and how to use them.  
[LLMs](https://python.langchain.com/docs/modules/model_io/llms/)  
This section covers functionality related to the LLM class. This is a type of model that takes a text string as input and returns a text string.  
[ChatModels](https://python.langchain.com/docs/modules/model_io/chat/)  
This section covers functionality related to the ChatModel class. This is a type of model that takes a list of messages as input and returns a message.  
[Output Parsers](https://python.langchain.com/docs/modules/model_io/output_parsers/)  
Output parsers are responsible for transforming the output of LLMs and ChatModels into more structured data. This section covers the different types of output parsers.  

**Project Map:**
- API Key
- Quickstart
    - Models
    - Prompt Templates
    - Output parsers
    - Composing with LCEL
- Concepts
     - Models (concept)
     - Messages (concept)
     - Prompts (concept)
     - Output Parsers (concept) 

Notebook:
[Model IO.ipynb](https://github.com/Omegapy/LLM-Frameworks-Tutorials/blob/main/LangChain%20Tutorials/Tutorials%20from%20Langchain/LangChain%20Modules/Model%20IO/Model%20IO.ipynb)

[Go back to the Project Main Map](#project-map-main)

-----------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------
# Retrieval
[Retrieval](https://github.com/Omegapy/LLM-Frameworks-Tutorials/tree/main/LangChain%20Tutorials/Tutorials%20from%20Langchain/LangChain%20Modules/Retrieval)

-----------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------

Projects Description:  
This project is a series of LangChain data retrieval for LLMs tutorials on Jupyter Notebook.  
The tutorials are a series LangChain Python code examples from the https://python.langchain.com/ website

Specifically from the section [Retrieval](https://python.langchain.com/docs/modules/data_connection/)

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

**Project Map:**
- Document loaders
- Text Splitters
- Text embedding models

Notebooks:
- [Document loaders.ipynb](https://github.com/Omegapy/LLM-Frameworks-Tutorials/blob/main/LangChain%20Tutorials/Tutorials%20from%20Langchain/LangChain%20Modules/Retrieval/Document%20loaders.ipynb)
- [Text Splitters.ipynb](https://github.com/Omegapy/LLM-Frameworks-Tutorials/blob/main/LangChain%20Tutorials/Tutorials%20from%20Langchain/LangChain%20Modules/Retrieval/Text%20Splitters.ipynb)
- [Text embedding models.ipynb](https://github.com/Omegapy/LLM-Frameworks-Tutorials/blob/main/LangChain%20Tutorials/Tutorials%20from%20Langchain/LangChain%20Modules/Retrieval/Text%20embedding%20models.ipynb)

[Go back to the Project Main Map](#project-map-main)

-----------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------
# Agents
[Agents](https://github.com/Omegapy/LLM-Frameworks-Tutorials/tree/main/LangChain%20Tutorials/Tutorials%20from%20Langchain/LangChain%20Modules/Agents)

-----------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------

Projects Description:  
This project is a series of LangChain data retrieval for LLMs tutorials on Jupyter Notebook.  
The tutorials are a series LangChain Python code examples from the https://python.langchain.com/ website

Specifically from the section [Agents](https://python.langchain.com/docs/modules/agents/)

**Agents**

The core idea of agents is to use a language model to choose a sequence of actions to take. In chains, a sequence of actions is hardcoded (in code). In agents, a language model is used as a reasoning engine to determine which actions to take and in which order.

[Quickstart](https://python.langchain.com/docs/modules/agents/quick_start)
For a quick start to working with agents, please check out this getting started guide. This covers basics like initializing an agent, creating tools, and adding memory.

[Concepts](https://python.langchain.com/docs/modules/agents/concepts)
There are several key concepts to understand when building agents: Agents, AgentExecutor, Tools, Toolkits. For an in depth explanation.

[Agent Types](https://python.langchain.com/docs/modules/agents/agent_types/)  
There are many different types of agents to use. For a overview of the different types and when to use them.

[Tools](https://python.langchain.com/docs/modules/data_connection/vectorstores/)  
With the rise of embeddings, there has emerged a need for databases to support efficient storage and searching of these embeddings. LangChain provides integrations with over 50 different vectorstores, from open-source local ones to cloud-hosted proprietary ones, allowing you to choose the one best suited for your needs. LangChain exposes a standard interface, allowing you to easily swap between vector stores.

How To Guides
Agents have a lot of related functionality! Check out comprehensive guides including:
- [Building a custom agent](https://python.langchain.com/docs/modules/agents/how_to/custom_agent)
- [Streaming (of both intermediate steps and tokens](https://python.langchain.com/docs/modules/agents/how_to/streaming)
- [Building an agent that returns structured output](https://python.langchain.com/docs/modules/agents/how_to/agent_structured) 
- Lots of functionality around using AgentExecutor, including: 
       - [using it as an iterator](https://python.langchain.com/docs/modules/agents/how_to/agent_iter)
       - [handle parsing errors](https://python.langchain.com/docs/modules/agents/how_to/handle_parsing_errors)
       - [returning intermediate steps](https://python.langchain.com/docs/modules/agents/how_to/intermediate_steps)
       - [capping the max number of iterations](https://python.langchain.com/docs/modules/agents/how_to/max_iterations)
       - [timeouts for agents]( https://python.langchain.com/docs/modules/agents/how_to/max_time_limit)

**Project Map Main**
- Quickstart
- Concepts
- Agent Types
- How To
- Tools

Notebooks:
- [Quickstart.ipynb](https://github.com/Omegapy/LLM-Frameworks-Tutorials/blob/main/LangChain%20Tutorials/Tutorials%20from%20Langchain/LangChain%20Modules/Agents/Quickstart.ipynb)
- [Concepts.ipynb](https://github.com/Omegapy/LLM-Frameworks-Tutorials/blob/main/LangChain%20Tutorials/Tutorials%20from%20Langchain/LangChain%20Modules/Agents/Concepts.ipynb) 
- [Agent Types.ipynb](https://github.com/Omegapy/LLM-Frameworks-Tutorials/blob/main/LangChain%20Tutorials/Tutorials%20from%20Langchain/LangChain%20Modules/Agents/Agent%20Types.ipynb)
- [How To.ipynb](https://github.com/Omegapy/LLM-Frameworks-Tutorials/blob/main/LangChain%20Tutorials/Tutorials%20from%20Langchain/LangChain%20Modules/Agents/How%20To.ipynb)
- [Tools.ipynb](https://github.com/Omegapy/LLM-Frameworks-Tutorials/blob/main/LangChain%20Tutorials/Tutorials%20from%20Langchain/LangChain%20Modules/Agents/Tools.ipynb


[Go back to the Project Main Map](#project-map-main)


