-----------------------------------------------------------------------------------------------------------------------------
# Tutorial LangChain LCEL
-----------------------------------------------------------------------------------------------------------------------------

 Alejandro Ricciardi (Omegapy)  
 created date: 01/18/2024  

Projects Description:  
 This project is a series of LangChain Expression Language (LCEL)tutorials on Jupyter Notebook.  
The tutorials are a series of LangChain LCEL (in Python) code examples from the https://python.langchain.com/ website

⚠️ This project requires an OpenAi key.

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
- [Intro. to LangChain LCEL](#intro-to-langchain-lcel) -|- [Intro LangChain LCEL.ipynb](https://github.com/Omegapy/LLM-Frameworks-Tutorials/blob/main/LangChain%20Tutorials/Tutorials%20from%20Langchain/Intro%20LangChain%20LCEL.ipynb)
- [Why Use LCEL](#why-use-lcel) -|- [Why LCEL.ipynb](https://github.com/Omegapy/LLM-Frameworks-Tutorials/blob/main/LangChain%20Tutorials/Tutorials%20from%20Langchain/Why%20LCEL.ipynb)
- [Interface - Runnable Class](interface---runnable-class) -|- [Interface - Runnable Class.ipynb](https://github.com/Omegapy/LLM-Frameworks-Tutorials/blob/main/LangChain%20Tutorials/Tutorials%20from%20Langchain/Interface%20-%20Runnable%20Class.ipynb)

-----------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------
# Intro. to LangChain LCEL
(Intro LangChain LCEL.ipynb)

-----------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------

Projects Description:  
**LangChain** is a framework for developing applications powered by language models.  
**In this project:**  I get started using LCEL.    
LCEL makes it easier to build complex chains from basic components, and supports out of the box functionality such as streaming, parallelism, and logging.

**Project map:**
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

-----------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------
 # Why Use LCEL
(Why LCEL.ipynb)

-----------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------

Projects Description:  
**LangChain** is a framework for developing applications powered by language models.  
**In this project:**  I compare using LCEL and using LangChain without LCEL.   
LCEL makes it easier to build complex chains from basic components, and supports out of the box functionality such as streaming, parallelism, and logging

**Project map:**
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
</table><br>

-----------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------
# Interface - Runnable Class
(Interface - Runnable Class.ipynb)

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


