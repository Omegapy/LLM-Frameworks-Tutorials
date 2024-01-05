#----------------------------------------------------------------------------
#                         LlamaIndex Hello World
# ---------------------------------------------------------------------------
#
#  Alejandro Ricciardi (Omegapy)
#  created date: 01/03/2024
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
# Projects Description:
# - Load WebPage (dataConnector)
# - Store it in an index
# - Create a query Engine
# - Ask question about the webpage
# - Use the LlamaIndex function:
#     - SimpleWebReader
#     - VectoreStoreIndex
#     - QueryEngine
#----------------------------------------------------------------------------

#--------------------------------------
#            Dependencies
#--------------------------------------
#----- LlamaIndex
from llama_index.readers import SimpleWebPageReader
from llama_index import VectorStoreIndex
#----- APY Key
import os
from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv())
OPENAI_API_KEY = os.environ.get("OPEN_AI_KEY")

#--------------------------------------
#            Functions
#--------------------------------------
#---- Main
def main(url:str) -> None:
    documents = SimpleWebPageReader(html_to_text=True).load_data(urls=[url]) # needs pipenv install html2text
    index = VectorStoreIndex.from_documents(documents=documents) # Vector store
    query_engine = index.as_query_engine() # using the vector store as a query engine
    # Querying the engine (vector store) with a prompt, LLM returning a response
    # Note: by default the OpenAI model is chatgpt3.5
    response = query_engine.query("Summarize")
    print(f"\n{response}")

#--------------------------------------
#            Main Program
#--------------------------------------
if __name__ == '__main__':
    print("\nHello Word!")
    main(url='https://www.datastax.com/guides/what-is-llamaindex')


