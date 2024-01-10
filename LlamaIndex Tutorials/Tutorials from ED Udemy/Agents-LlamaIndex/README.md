-----------------------------------------------------------------------------------------------------------------------------
Agents LlamaIndex
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
Using the LlamaIndex ReactAgent method to create a LlamaIndex Agent that writes haiku (Japanese poem) from a given topic.  

[Agents:](https://docs.llamaindex.ai/en/stable/use_cases/agents.html#agents)  
An agent is an automated reasoning and decision engine. It takes in a user input/query  
and can make internal decisions for executing that query in order to return the correct result.  
The key agent components can include, but are not limited to:  
-	Breaking down a complex question into smaller ones  
-	Choosing an external Tool to use + coming up with parameters for calling the Tool  
- Planning out a set of tasks  
-	Storing previously completed tasks in a memory module
  
Agents used in this project:
- ReAct Agent:  
it uses a loop and a list of provided tools to react and respond to queries.  
- OpenAI Agent:  
OpenAI Agent supports function calling from OpenAI.    
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
- QueryEngineTool: A tool that wraps an existing query engine. Note: since our agent abstractions inherit from BaseQueryEngine, these tools can also wrap other agents

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





