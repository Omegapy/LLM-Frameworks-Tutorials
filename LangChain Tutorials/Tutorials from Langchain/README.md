-----------------------------------------------------------------------------------------------------------------------------
# Tutorial LangChain LCEL
-----------------------------------------------------------------------------------------------------------------------------

 Alejandro Ricciardi (Omegapy)  
 created date: 01/18/2024  

Projects Description: 
 This project is a series of LangChain Expression Language (LCEL)tutorials on Jupyter Notebook.  
The tutorials are a series of LangChain LCEL (in Python) code examples from the https://python.langchain.com/ website

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

  **Project map:**
- Intro. to LangChain LCEL (Intro LangChain LCEL.ipynb)
- Why Use LCEL (Why LCEL.ipynb)

-----------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------
<h2 align="center">Intro. to LangChain LCEL</h2>
(Intro LangChain LCEL.ipynb)

-----------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------

Projects Description:  
**LangChain** is a framework for developing applications powered by language models.  
**In this project:**  I get started using LCEL.    
LCEL makes it easier to build complex chains from basic components, and supports out of the box functionality such as streaming, parallelism, and logging.

⚠️ This project requires an OpenAi key.

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
 <h2 align="center">Why Use LCE</h2>
(Why LCEL.ipynb)

-----------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------

Projects Description:  
**LangChain** is a framework for developing applications powered by language models.  
**In this project:**  I compare using LCEL and using LangChain without LCEL.   
LCEL makes it easier to build complex chains from basic components, and supports out of the box functionality such as streaming, parallelism, and logging

⚠️ This project requires an OpenAi key.

**Project map:**
- API Key
- Basic Example Using LCEL
- Invoke
    - With LCEL
    - Without LCEL
- Stream
    - With LCEL
    - Without LCEL
- Batch
    - With LCEL
    - Without LCEL
- Async
    - With LCEL
    - Without LCEL
- LLM instead of chat model
    - With LCEL
    - Without LCEL
- Different model provider
    - With LCEL
    - Without LCEL
- Runtime configurability
    - With LCEL
    - Without LCEL
- Logging
    - With LCEL
    - Without LCEL
- Fallbacks 
    - With LCEL
    - Without LCEL
- Full code comparison
    - With LCEL
    - Without LCEL






