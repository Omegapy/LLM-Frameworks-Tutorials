##----------------------------------------------------------------------------
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
#  Implementing Streamlit user interface (UI) to query LlamaIndex data with an LLM
#  - Accessing a Pinecone DB
#  - Creating a vector store object
#  - Store Index in a pinecone vector database
#  - Debugging with LlamaIndex call-back feature
#  - Create an index object
#  - Prompting LLM and getting a response
#  - Displaying LLM messages and user input  into browser
#  - Using Streamlit as a user interface (UI)
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

#--------------------------------------
#            Functions
#--------------------------------------

#----------------------------------------
# Init. DB Pinecone
# Keeps the connection to the DB alive
# Returns VectorStoreIndex object
#----------------------------------------
@st.cache_resource(show_spinner=False) # Decoration keeps in memory cache and spinning (Connection to DB alive)
def get_index() -> VectorStoreIndex: # "-> VectorStoreIndex" Metadata describing their parameters and return values
    pinecone.init(
        api_key=os.environ["PINECONE_API_KEY"],
        environment=os.environ["PINECONE_ENVIRONMENT"],
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
    # --- Debugging with LlamaIndex
    llama_debug = LlamaDebugHandler(print_trace_on_end=True)
    callback_manager = CallbackManager(handlers=[llama_debug])
    service_context = ServiceContext.from_defaults(callback_manager=callback_manager)

    return VectorStoreIndex.from_vector_store(
        vector_store=vector_store, service_context=service_context
    )

#--------------------------------------
#            Main Program
#--------------------------------------
print("***Streamlit LlamaIndex Documentation Helper***")

#--- Init. index object

# Loading vector_store into the index, https://docs.llamaindex.ai/en/stable/module_guides/indexing/vector_store_index.htm
index = get_index() # The function will run indefectibly keeping the connection to DB alive
# The chat engine keeps of a conversation, is the query engine with a state, it keeps track of the history
# Init. chat engine with st.session_state, it is a like a dictionary, it has keys and values
# st.session_state is a way to share variables between reruns, different session of the same program,
# it remembers variables and prevents it to be rewritten over
# https://docs.streamlit.io/library/api-reference/session-state
if "chat_engine" not in st.session_state.keys():
        st.session_state.chat_engine = index.as_chat_engine( # https://docs.llamaindex.ai/en/stable/module_guides/deploying/chat_engines/root.html
            chat_mode=ChatMode.CONTEXT, verbose=True
        )

#---- Init. Webpage
st.set_page_config(
    page_title="Chat with LlamaIndex docs, powered by LlamaIndex",
    page_icon="🦙",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items=None,
)
st.title("Chat with LlamaIndex docs 💬🦙")

#---- Int. Chat
if "messages" not in st.session_state.keys():
    st.session_state.messages = [
        {
            # Prompt LLM its roll (context)
            "role": "assistant",
            # First content/response LLM (me is LLM)
            "content": "Ask me a question about LlamaIndex's open source python library?",
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
            # st.session_state.chat_engine.chat() return an object <class 'llama_index.chat_engine.types.AgentChatResponse'>
            # response.response is a str
            # st.write allows to write arguments to the st app.
            # https://docs.streamlit.io/library/api-reference/write-magic/st.write
            st.write(response.response)
            # Creates a st message object
            message = {"role": "assistant", "content": response.response}
            # Saves the new message to session messages
            st.session_state.messages.append(message)