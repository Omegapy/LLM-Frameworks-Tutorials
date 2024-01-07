#-----------------------------------------------------------------------------
#                             Agents LlamaIndex
# ---------------------------------------------------------------------------
#
#  Alejandro Ricciardi (Omegapy)
#  created date: 01/06/2024
#
# Credit:
# Udemy - Eden Marco.
# LlamaIndex- Develop LLM powered applications with LlamaIndex:
# https://www.udemy.com/course/lamaindex/
# All the files and folders have been modified from the original source to meet my requirements or to add functionalities to the programs.
# Furthermore, the code lines are heavily commented on; this is a tutorial, after all.
#
# --------------------------------------------------------------------------
#
#  Description:
#  Using the LlamaIndex ReactAgent method,
#  creates an LlamaIndex Agent that writes haiku (japanese poem) from a given topic.
#
#  Agents:
#  An “agent” is an automated reasoning and decision engine. It takes in a user input/query
#  and can make internal decisions for executing that query in order to return the correct result.
#  The key agent components can include, but are not limited to:
#    •	Breaking down a complex question into smaller ones
#    •	Choosing an external Tool to use + coming up with parameters for calling the Tool
#    •	Planning out a set of tasks
#    •	Storing previously completed tasks in a memory module
#  https://docs.llamaindex.ai/en/stable/use_cases/agents.html#agents
#
#--- A ReAct Agent uses a loop and a list of provided tools to react with s and response to query.
#
#  Tools: ( From LlamaIndex Documentation)
#  Having proper tool abstractions is at the core of building data agents.
#  Defining a set of Tools is similar to defining any API interface,
#  with the exception that these Tools are meant for agent rather than human use.
#  We allow users to define both a Tool as well as a ToolSpec containing a series of functions under the hood.
#  A Tool implements a very generic interface - simply define __call__
#  and also return some basic metadata (name, description, function schema).
#  A Tool Spec defines a full API specification of any service that can be converted into a list of Tools.
#  We offer a few different types of Tools:
#    •	FunctionTool: A function tool allows users to easily convert any user-defined function into a Tool.
#       It can also auto-infer the function schema.
#    •	QueryEngineTool: A tool that wraps an existing query engine. Note:
#       since our agent abstractions inherit from BaseQueryEngine, these tools can also wrap other agents
# https://docs.llamaindex.ai/en/stable/module_guides/deploying/agents/tools/root.html#tools
#
#----------------------------------------------------------------------------

#--------------------------------------
#            Dependencies
#--------------------------------------

#----- APY Key
import os
from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv())
OPENAI_API_KEY = os.environ.get("OPEN_AI_KEY")
PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")
PINECONE_ENVIRONMENT = os.environ.get("PINECONE_ENVIRONMENT")
#----- LlamaIndex
#from llama_index.llms import OpenAI

from llama_index.agent import ReActAgent # https://docs.llamaindex.ai/en/stable/examples/agent/react_agent_with_query_engine.html
from llama_index.tools import FunctionTool
from llama_index.callbacks import LlamaDebugHandler, CallbackManager

import subprocess


#--------------------------------------
#     Global Scope Variables
#--------------------------------------
llm = OpenAI() # Default in Jan. 2024 chatgpt 3.5

#--------------------------------------
#            Functions
#--------------------------------------

# def write_haiku(topic: str) -> str:
#     """
#     This function is used by a function tool to writes a haiku about a given topic.
#     """
#     return llm.complete(f"wrtie me a haiku about {topic}")
#
# def count_characters(text: str) -> int:
#     """
#     This function is used by a function tool to count the number of characters in text.
#     """
#     return len(text)
#
# def open_application(application_name: str) -> str:
#     """
#     This function opens an application in my computer
#     """
#     try:
#         subprocess.Popen(["C:/Users/User/AppData/Local/open", "-n", "-a", application_name])
#         return "successfully opened application"
#     except Exception as e:
#         print(f"Error: {str(e)}")
#
# def open_url(url: str) -> str:
#     """
#     Opens a url in browser (chrome/ safari/ firefox)
#     """
#     try:
#         subprocess.Popen(["C:/Users/User/AppData/Local/open", "--url", url])
#         return "succesfully open url"
#     except Exception as e:
#         print(f"Error: {str(e)}")
#
# #--------------------------------------
# #            Main Program
# #--------------------------------------
# if __name__ == "__main__":
#     print("**** Hello Agents LlamaIndex ****")
#
#     # A function tool allows users to easily convert any user-defined function into a Tool.
#     # It can also auto-infer the function schema.
#     tool1 = FunctionTool.from_defaults(fn=write_haiku, name="write_haiku") # The name and fn arguments have to have the same spelling
#     tool2 = FunctionTool.from_defaults(fn=count_characters, name="count_characters")
#     tool3 = FunctionTool.from_defaults(fn=open_application, name="open_application")
#     tool4 = FunctionTool.from_defaults(fn=open_url, name="open_url")
#
#     agent = ReActAgent.from_tools(tools=[tool1, tool2], llm=llm, verbose=True)
#
#
#     #--- Prompts
#     llama_debug = LlamaDebugHandler(print_trace_on_end=True)
#     callback_manager = CallbackManager(handlers=[llama_debug])
#     agent = ReActAgent.from_tools(
#         tools=[tool1, tool2, tool3],
#         llm=llm,
#         verbose=True,
#         callback_manager=callback_manager,
#     )
#     # res = agent.query("Write me a haiku about tennis and then count the characters in it")
#     # res = agent.query("Open discord in my computer")
#     res = agent.query(
#         "write a haiku about trees and then Open the url https://www.youtube.com/watch?v=dQw4w9WgXcQ in my chrome"
#     )
#     print(res)
#
# """
# Output:
#
# Thought: I need to use a tool to help me write a haiku about tennis.
# Action: write_haiku
# Action Input: {'topic': 'tennis'}
# Observation: Racket strikes the ball,
# Graceful dance on the court's stage,
# Love for tennis calls.
# Thought: Now I need to count the characters in the haiku.
# Action: count_characters
# Action Input: {'text': 'Racket strikes the ball,\\nGraceful dance on the court\\'}
# Observation: 54
# Thought: I can answer without using any more tools.
# Response: The haiku about tennis has 54 characters.
# The haiku about tennis has 54 characters.
#
# """
#
# """
# Output explanation:
#
# Prompt : "Write me a haiku about tennis and then count the characters in it"
#
# -- Reasoning: ReActAgent Loop 1 --
# Thought: I need to use a tool to help me write a haiku about tennis. <-- First part of the prompt (Write me a haiku about tennis)
# Action: write_haiku
# Action Input: {'topic': 'tennis'} <-- ReActAgent chooses tool1 to display haiku about tennis
# Observation: Racket strikes the ball, <-- Output of the tool
# Graceful dance on the court's stage,
# Love for tennis calls.
#
# -- Reasoning: ReActAgent Loop 2 --
# Thought: Now I need to count the characters in the haiku. <-- Second part of the prompt (and then count the characters in it)
# Action: count_characters
# Action Input: {'text': 'Racket strikes the ball,\\nGraceful dance on the court\\'}
# Observation: 54 <-- Output of the tool
#
# -- Reasoning: ReActAgent Loop 3 --
# Thought: I can answer without using any more tools. <-- No more tools match the prompt
# -- end loop --
#
# -- Outputs response
# Response: The haiku about tennis has 54 characters.
# The haiku about tennis has 54 characters.
#
# """