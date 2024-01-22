-----------------------------------------------------------------------------------------------------------------------------
# Tutorial LangChain LCEL
-----------------------------------------------------------------------------------------------------------------------------

 Alejandro Ricciardi (Omegapy)  
 created date: 01/18/2024  

Projects Description:  
This project is a series of LangChain Expression Language (LCEL) tutorials on Jupyter Notebook.  
The tutorials are a series of LangChain LCEL (in Python) code examples from the https://python.langchain.com/ website

Specifically from the section [LangChain Expression Language (LCEL)]( https://python.langchain.com/docs/expression_language/)

⚠️ This project requires an OpenAI key.

-----------------------------------------------------------------------------------------------------------------------------

**LangChain** is a framework for developing applications powered by language models. It enables applications that:
- **Are context-aware**: connect a language model to sources of context (prompt instructions, few shot examples, content to ground its response in, etc.)
- **Reason:** rely on a language model to reason (about how to answer based on provided context, what actions to take, etc.)
This framework consists of several parts.
- **LangChain Libraries:** The Python and JavaScript libraries. Contains interfaces and integrations for a myriad of components, a basic run time for combining these components into chains and agents, and off-the-shelf implementations of chains and agents.
- **LangChain Templates:** A collection of easily deployable reference architectures for a wide variety of tasks.
- **LangServe:** A library for deploying LangChain chains as a REST API.
- **LangSmith:** A developer platform that lets you debug, test, evaluate, and monitor chains built on any LLM framework and seamlessly integrates with LangChain.

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
- [Intro. to LangChain LCEL](#intro-to-langchain-lcel) 
- [Why Use LCEL](#why-use-lcel) 
- [Interface Runnable Class](#interface-runnable-class) 
- [How To](#how-to)
- [Cookbook](#cookbook)


Notebooks:
- [Intro LangChain LCEL.ipynb](https://github.com/Omegapy/LLM-Frameworks-Tutorials/blob/main/LangChain%20Tutorials/Tutorials%20from%20Langchain/Intro%20LangChain%20LCEL.ipynb)
- [Why LCEL.ipynb](https://github.com/Omegapy/LLM-Frameworks-Tutorials/blob/main/LangChain%20Tutorials/Tutorials%20from%20Langchain/Why%20LCEL.ipynb)
- [Interface - Runnable Class.ipynb](https://github.com/Omegapy/LLM-Frameworks-Tutorials/blob/main/LangChain%20Tutorials/Tutorials%20from%20Langchain/Interface%20-%20Runnable%20Class.ipynb)
- [How To.ipynb](https://github.com/Omegapy/LLM-Frameworks-Tutorials/blob/main/LangChain%20Tutorials/Tutorials%20from%20Langchain/How%20To.ipynb)
- [Cookbook.ipynb]()

-----------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------
# Intro. to LangChain LCEL
[Intro LangChain LCEL.ipynb](https://github.com/Omegapy/LLM-Frameworks-Tutorials/blob/main/LangChain%20Tutorials/Tutorials%20from%20Langchain/Intro%20LangChain%20LCEL.ipynb)

-----------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------

Projects Description:  
**LangChain** is a framework for developing applications powered by language models.  
**In this project:**  I get started using LCEL.    
LCEL makes it easier to build complex chains from basic components, and supports out of the box functionality such as streaming, parallelism, and logging.

**Project Map:**
- API Key
- Getting started
    - Basic example **```chain = prompt | model | output_parser```**
        - Prompt (Human Message) **```prompt_value = prompt.invoke({"topic": "ice cream"})```**
        - Model (AIMessage) **```message = model.invoke(prompt_value)```**
                - ChatModel Output
                - LLM Output
        - Output parser (takes AIMessage or any string and converts it) **```output_parser.invoke(message)```**
        - Entire Pipeline **```(prompt | model | output_parser).invoke({"topic": "ice cream"})```**
- RAG Search **```chain = setup_and_retrieval | prompt | model | output_parser```**
    - Example
    - Example Explanation

[Go back to the Project Main Map](#project-map-main)

-----------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------
 # Why Use LCEL
[Why LCEL.ipynb](https://github.com/Omegapy/LLM-Frameworks-Tutorials/blob/main/LangChain%20Tutorials/Tutorials%20from%20Langchain/Why%20LCEL.ipynb)

-----------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------

Projects Description:  
**LangChain** is a framework for developing applications powered by language models.  
**In this project:**  I compare using LCEL and using LangChain without LCEL.   
LCEL makes it easier to build complex chains from basic components, and supports out of the box functionality such as streaming, parallelism, and logging

**Project Map:**
<table>
  <tr>
    <td>API Key</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Basic Example Using LCEL</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Invoke</td>
    <td>With LCEL</td>
    <td>Without LCEL</td>
  </tr>
  <tr>
    <td>Stream</td>
    <td>With LCEL</td>
    <td>Without LCEL</td>
  </tr>
  <tr>
    <td>Batch</td>
    <td>With LCEL</td>
    <td>Without LCEL</td>
  </tr>
  <tr>
    <td>Async</td>
    <td>With LCEL</td>
    <td>Without LCEL</td>
  </tr>
  <tr>
    <td>LLM instead of chat model</td>
    <td>With LCEL</td>
    <td>Without LCEL</td>
  </tr>
  <tr>
    <td>Different model provider</td>
    <td>With LCEL</td>
    <td>Without LCEL</td>
  </tr>
  <tr>
    <td>Runtime configurability</td>
    <td>With LCEL</td>
    <td>Without LCEL</td>
  </tr>
  <tr>
    <td>Logging</td>
    <td>With LCEL</td>
    <td>Without LCEL</td>
  </tr>
  <tr>
    <td>Fallbacks</td>
    <td>With LCEL</td>
    <td>Without LCEL</td>
  </tr>
  <tr>
    <td>Full code comparison</td>
    <td>With LCEL</td>
    <td>Without LCEL</td>
  </tr>
</table><be>

[Go back to the Project Main Map](#project-map-main)

-----------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------
# Interface Runnable Class
[Interface - Runnable Class.ipynb](https://github.com/Omegapy/LLM-Frameworks-Tutorials/blob/main/LangChain%20Tutorials/Tutorials%20from%20Langchain/Interface%20-%20Runnable%20Class.ipynb)

-----------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------

Projects Description:  
**LangChain** is a framework for developing applications powered by language models. It enables applications that:

**In this project:**  I explore the concept of the [Runnable](https://api.python.langchain.com/en/stable/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable) protocol. Using LangChain Expression Language (LCEL).

```class langchain_core.runnables.base.Runnable``` 

A unit of work that can be invoked, batched, streamed, transformed and composed.
- ```invoke```/```ainvoke```: Transforms a single input into an output.
- ```batch```/```abatch```: Efficiently transforms multiple inputs into outputs.
- ```stream```/```astream```: Streams output from a single input as it’s produced.
- ```astream_log```: ```Streams``` output and selected intermediate results from an input.

**Project map:**
- API Key
- Base Example
- Input Schema
    - Chain Schema
    - Prompt Schema
    - Model Schema
- Output Schema
    - Chain Schema
    - Prompt Schema
    - Model Schema
- Batch
- Async
    - Async Stream
    - Async Invoke
    - Async Batch
- Parallelism
    - Chains NOT ran in parallel
    - Chains ran in parallel
- Parallelism on batches
    - Batches NOT ran in parallel
    - Batches ran in parallel

[Go back to the Project Main Map](#project-map-main)

-----------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------
# How To
[How To.ipynb](https://github.com/Omegapy/LLM-Frameworks-Tutorials/blob/main/LangChain%20Tutorials/Tutorials%20from%20Langchain/How%20To.ipynb)

-----------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------

Projects Description:  
**LangChain** is a framework for developing applications powered by language models. 

**In this project:** 
I explore how to apply LCEL to different code applications such as manipulating data and adding messages.

**Project map:**
- API Key
- Manipulating Inputs Output (RunnableParallel)
    - Base Example
    - Using itemgetter as shorthand
    - Parallelism
        - Base Example
        - Parallelism running independent processes
- Passing data through (RunnablePassthrough
    - Retrieval Example
- Run Custom Functions
    - Base Example
    - Accepting a Runnable Config - (Token Used)
- Dynamically route logic based on input (RunnableBranch
    - Using a RunnableBranch
- Bind runtime args
    - Base Example
    - Attaching OpenAI functions
    - Attaching OpenAI tools
    - Configuration Fields
        - With LLMs (llm temp)
        - With HubRunnables (prompt switching
    - Configurable Alternatives)
        - With LLMs (model Alt
        - With Prompts
        - With Prompts and LLMs
    - Saving configurations
- Create a runnable with the @chain decorator
- Handling LLM API Errors)
    - OpenAI Key Fallbacks Anthropic Key
    - Anthropic Key Fallbacks OpenAI Key
    - Model RateLimits Fallbacks using prompt templates (OpenAI gpt-4  Fallbacks to OpenAI gpt-3.5)
- Stream custom generator functions
    - Sync version
    - Async version
- Inspect Runnables
    - Base Example
    - Print a graph
- Chain Memory (Add message history (memory))
    - Setup](#setup)
        - Docker Explained
        - REDIS Server and Docker Container
        - LangSmith
    - Example: Dict input, message output
    - Adding message history
    - Invoking with config
    - Example: messages input, dict output
    - More examples

[Go back to the Project Main Map](#project-map-main)

-----------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------
# Cookbook
[Cookbook.ipynb]() 

-----------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------

**In this project:** 
I explore example of code for accomplishing common tasks with the LangChain Expression Language (LCEL). These examples show how to compose different Runnable (the core LCEL interface) components to achieve various tasks. If you’re just getting acquainted with LCEL, the [Prompt + LLM](https://python.langchain.com/docs/expression_language/cookbook/prompt_llm_parser) is a good place to start.

**Project map:**
- API Keys 
- Prompt + LLM
    - PromptTemplate + LLM 
        - Base Example
        - Attaching Stop Sequences
        - Attaching Function Call information
    - PromptTemplate + LLM + OutputParser
        - Base Example
        - Functions Output Parser
    - Simplifying input
- RAG
    - Base Example
    - Conversational Retrieval Chain (chat_message_history)
        - Base Example
        - With Memory and returning source documents
- Multiple chains
    - Base Example
        - Using itemgetter
    - Branching and Merging
- Querying a SQL DB
    - Installing Chinook SQL DB
    - Querying a SQL DB  Base Example
- Code writing (Agent Functions in Python)
- Routing by semantic similarity
- Adding memory to Chains
- Adding moderation
- Managing prompt size (Tokens) 





