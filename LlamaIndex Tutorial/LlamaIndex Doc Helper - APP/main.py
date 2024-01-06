#-----------------------------------------------------------------------------
#                      LlamaIndex Doc Helper - APP
#                   Data Querying - Prompt - streamlit
# ---------------------------------------------------------------------------
#
#  Alejandro Ricciardi (Omegapy)
#  created date: 01/05/2024
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
#  Implementing Node post-processing Streamlit user interface (UI)
#  - Accessing a Pinecone DB
#  - Creating a vector store object
#  - Store Index in a pinecone vector database
#  - Debugging with LlamaIndex call-back feature
#  - Create an index object
#  - Node post-processing:
#     - SentenceEmbeddingOptimizer (llamaIndex)
#     - Custom LlamaIndex node post-processor: DuplicateRemoverNodePostprocessor
#  - Prompting LLM and getting a response
#  - Implementing Streamlit UI
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
# Vectors, index, and Data Base
from llama_index import (
    VectorStoreIndex, # https://docs.llamaindex.ai/en/stable/module_guides/indexing/vector_store_index.html
    ServiceContext # https://docs.llamaindex.ai/en/stable/module_guides/supporting_modules/service_context.html#servicecontext
)
# Data Base Pinecone
import pinecone
from llama_index.vector_stores import PineconeVectorStore # https://docs.llamaindex.ai/en/stable/examples/vector_stores/PineconeIndexDemo.
# Debugging
from llama_index.callbacks import (
    CallbackManager,
    LlamaDebugHandler,
)
# Chat engine keeps track of the conversation
from llama_index.chat_engine.types import ChatMode
# LLM model
from llama_index.llms import OpenAI # This tells LlamaIndex to utilize ChapGPT 3.5 by default
#---- UI Streamlit
import streamlit as st # https://docs.streamlit.io/get-started

#---- LlamaIndex post-processors
# Node postprocessors are a set of modules that take a set of nodes, and apply some kind of transformation or filtering before returning them.
# In LlamaIndex, node postprocessors are most commonly applied within a query engine,
# after the node retrieval step and before the response synthesis step.
# https://docs.llamaindex.ai/en/stable/module_guides/querying/node_postprocessors/root.
#
# SentenceEmbeddingOptimizer:
# This postprocessor optimizes token usage by removing sentences that are not relevant to the query (this is done using embeddings).
# The percentile cutoff is a measure for using the top percentage of relevant sentences.
# The threshold cutoff can be specified instead, which uses a raw similarity cutoff for picking which sentences to keep.
# https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/OptimizerDemo.html
from llama_index.indices.postprocessor import SentenceEmbeddingOptimizer
# Custom LlamaIndex node post-processors see class DuplicateRemoverNodePostprocessor in directory node_processors
from node_postprocessors.duplicate_postprocessing import DuplicateRemoverNodePostprocessor # Remove duplicated nodes

print("***Streamlit LlamaIndex Documentation Helper***")

#--------------------------------------
#     Global Scope Variables
#--------------------------------------
# Debugging with LlamaIndex
llama_debug = LlamaDebugHandler(print_trace_on_end=True)
callback_manager = CallbackManager(handlers=[llama_debug])
# Service context
service_context = ServiceContext.from_defaults(
    llm=OpenAI(model="gpt-4-1106-preview", temperature=0),
    callback_manager=callback_manager)

#--------------------------------------
#            Functions
#--------------------------------------

#----------------------------------------
# Init. DB Pinecone
# Keeps the connection to the DB alive
# Returns VectorStoreIndex object
#----------------------------------------
@st.cache_resource(show_spinner=False) # Decoration keeps in memory cache and spinning (Connection to DB alive) (Streamlit)
def get_index() -> VectorStoreIndex: # "-> VectorStoreIndex" Metadata describing their parameters and return values
    pinecone.init(
        api_key=os.environ["PINECONE_API_KEY"],
        environment=os.environ["PINECONE_ENVIRONMENT"]
    )
    # Pinecone DB
    index_name = "llamaindex-doc-helper"
    # Checks if the picone DB exists
    if index_name not in pinecone.list_indexes():
        raise ValueError("The index name is not in the list of indexes associated with the provided Pinecone account.")
    # Init. Pinecone Index object
    pinecone_index = pinecone.Index(index_name=index_name)
    # --- Creating a vector store object
    vector_store = PineconeVectorStore(pinecone_index=pinecone_index)

    return VectorStoreIndex.from_vector_store(vector_store=vector_store, service_context=service_context)

#--------------------------------------
#            Main Program
#--------------------------------------

#--- Init. index object
# Loading vector_store into the index, https://docs.llamaindex.ai/en/stable/module_guides/indexing/vector_store_index.htm
index = get_index() # The function will run indefectibly keeping the connection to DB alive

#-----------------------------
# Start of
# Node post-processing
#-----------------------------

# The chat engine keeps of a conversation, is the query engine with a state, it keeps track of the history
# https://docs.llamaindex.ai/en/stable/module_guides/deploying/chat_engines/root.html
# Init. chat engine with st.session_state, it is a like a dictionary, it has keys and values
# st.session_state is a way to share variables between reruns, different session of the same program,
# it remembers variables and prevents it to be rewritten over
# https://docs.streamlit.io/library/api-reference/session-state
if "chat_engine" not in st.session_state.keys():
    # ----- node post-processing - sentence Embeddings optimizer ----
    # Cleans up the nodes data and keep only semantic meaningful data.
    # Note: The post-processor Makes an API call for each sentence to the embedding model, cost money.
    #
    # SentenceEmbeddingOptimizer:
    # This postprocessor optimizes token usage by removing sentences that are not relevant to the query (this is done using embeddings).
    # The percentile cutoff is a measure for using the top percentage of relevant sentences.
    # The threshold cutoff can be specified instead, which uses a raw similarity cutoff for picking which sentences to keep.
    # https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/OptimizerDemo.html
    postprocessor = SentenceEmbeddingOptimizer(
        embed_model=service_context.embed_model, # OpenAi embedding model
        percentile_cutoff=None, # Keeps only the 50% of the top related sentences
        threshold_cutoff=None # Leave out sentences that the similarity score was above for example 0.7 or 70%
    )
    st.session_state.chat_engine = index.as_chat_engine(
        chat_mode=ChatMode.CONTEXT,
        verbose=True,
        node_postprocessors=[
            postprocessor, # postprocessor = SentenceEmbeddingOptimizer
            DuplicateRemoverNodePostprocessor() # Handles duplicated nodes (costume see directory node_processors)
        ]
    )
#-----------------------------
# End of
# Node post-processing
#-----------------------------

#-----------------------------
#       Streamlit UI
#-----------------------------
#---- Init. Webpage
st.set_page_config(
    page_title="Chat with LlamaIndex docs, powered by LlamaIndex",
    page_icon="🦙",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items=None
)
st.title("Chat with LlamaIndex docs 💬🦙")

#---- Int. Chat
if "messages" not in st.session_state.keys():
    st.session_state.messages = [
        {
            # Prompt LLM its roll (context)
            "role": "assistant",
            # First content/response LLM (me is LLM)
            "content": "Ask me a question about LlamaIndex's open source python library?"
        }
    ]

#---- Prompting LLM
# prompt is the user input
if prompt := st.chat_input("Your question"): # In input box
    st.session_state.messages.append({"role": "user", "content": prompt})
#---- Print Messages/content/responses from LLM
# First message/LLM content "Ask me a question about LlamaIndex's open source python library?"
for message in st.session_state.messages:
    with st.chat_message(message["role"]): # avatar/emojy bot
        st.write(message["content"]) # Print message from LLM
#---- Input from user
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"): # avatar/emojy bot
        with st.spinner("Thinking..."): # avatar/emojy thinking spinning
            response = st.session_state.chat_engine.chat(message=prompt)
            nodes = [node for node in response.source_nodes]
            # st.session_state.chat_engine.chat() return an object <class 'llama_index.chat_engine.types.AgentChatResponse'>
            # response.response is a str
            # st.write allows to write arguments to the st app.
            # https://docs.streamlit.io/library/api-reference/write-magic/st.write
            st.write(response.response)
            #-- Displays selected Nodes for troubleshooting purposes
            nodes = [node for node in response.source_nodes]
            for col, node, i in zip(st.columns(len(nodes)), nodes, range(len(nodes))):
                with col:
                    st.header(f"Source Node {i + 1}: score= {node.score}")
                    st.write(node.text)
            # Creates a st message object
            message = {"role": "assistant", "content": response.response}
            # Saves the new message to session messages
            st.session_state.messages.append(message)