##----------------------------------------------------------------------------
#                         LlamaIndex Doc Helper
#                           Data Querying
# ---------------------------------------------------------------------------
#
#  Alejandro Ricciardi (Omegapy)
#  created date: 01/03/2024
#
# Credit:
# Udemy - Eden Marco.
# LlamaIndex- Develop LLM powered applications with LlamaIndex:
# https://www.udemy.com/course/lamaindex/
#
# --------------------------------------------------------------------------
#
#  Description:
#  Data Querying
#  - Accessing a Pinecone DB
#  - Creating a vector store object
#  - Store Index in a pinecone vector database
#  - Debugging with LlamaIndex call-back feature
#  - Create an index object
#  - Prompting LLM and getting a response
#
#----------------------------------------------------------------------------

#--------------------------------------
#            Dependencies
#--------------------------------------

#----- APY Key
import os
from dotenv import load_dotenv,find_dotenv
from llama_index.callbacks import CallbackManager

load_dotenv(find_dotenv())
OPENAI_API_KEY = os.environ.get("OPEN_AI_KEY")
PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")
PINECONE_ENVIRONMENT = os.environ.get("PINECONE_ENVIRONMENT")

#----- LlamaIndex
from llama_index import VectorStoreIndex, \
    ServiceContext  # https://docs.llamaindex.ai/en/stable/module_guides/indexing/vector_store_index.html
from llama_index.vector_stores import PineconeVectorStore # https://docs.llamaindex.ai/en/stable/examples/vector_stores/PineconeIndexDemo.html
from llama_index.callbacks import (
    CallbackManager,
    LlamaDebugHandler,
)

#---- Init. Pinecone
import pinecone
pinecone.init(
    api_key=PINECONE_API_KEY,
    environment=PINECONE_ENVIRONMENT,
)

#--------------------------------------
#            Main Program
#--------------------------------------
if __name__ == '__main__':
    print("\nHello Word, RAG...")

    # ------------------------
    #     Data Querying
    # ------------------------

    #--- Pinecone DB
    index_name = "llamaindex-doc-helper"
    # Checks if the picone DB exists
    if index_name not in pinecone.list_indexes():
        print(
            "\n\033[96m The index name is not in the list of indexes associated with the provided Pinecone account.\n")
        # Hard exit
        exit()
    # Init. Pinecone Index object
    pinecone_index = pinecone.Index(index_name=index_name)

    #--- Creating a vector store object
    vector_store = PineconeVectorStore(pinecone_index=pinecone_index)

    #--- Debugging with LlamaIndex
    llama_debug = LlamaDebugHandler(print_trace_on_end=True)
    callback_manager = CallbackManager(handlers=[llama_debug])
    service_context = ServiceContext.from_defaults(callback_manager=callback_manager)

    #--- Init. index object
    # Loading vector_store into the index, https://docs.llamaindex.ai/en/stable/module_guides/indexing/vector_store_index.html
    index = VectorStoreIndex.from_vector_store(vector_store=vector_store, service_context=service_context)

    #--- Querying
    query = "What is a LlamaIndex query engine?"
    #-- Query Engine, https://docs.llamaindex.ai/en/stable/module_guides/deploying/query_engine/root.html
    query_engine = index.as_query_engine()
    # Prompting LLM and getting a response
    response = query_engine.query(query)
    print(f"\n\033[1;37;40m{response}")


