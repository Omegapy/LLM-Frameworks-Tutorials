-----------------------------------------------------------------------------------------------------------------------------
MultyModal RAG LlamaIndex
-----------------------------------------------------------------------------------------------------------------------------


 Alejandro Ricciardi (Omegapy)  
 created date: 12/31/2023  

-----------------------------------------------------------------------------------------------------------------------------
Projects Description:

This repository is a series of tutorials on Multi-modal Retrieval Augmented Generation with LlamaIndex on Jupyter Notebook. 

The tutorials are based on LlamaIndex YouTube video series.  
https://www.youtube.com/@LlamaIndex

-----------------------------------------------------------------------------------------------------------------------------
Requirements:  
Python: https://www.python.org/  
Jupyter Notebook: https://jupyter.org/  
LlamaIndex: https://www.llamaindex.ai/  
OpenAI API Key: https://openai.com/  	

Note: I use [pipenv]( https://pipenv.pypa.io/en/latest/) as my Python virtual environment

-----------------------------------------------------------------------------------------------------------------------------

Links:   
GitHub: https://github.com/Omegapy   
Facebook: https://www.facebook.com/profile.php?id=100089638857137  
Twitter: https://twitter.com/RicciardiAlex  
Instagram: https://www.instagram.com/alexomegapy/

-----------------------------------------------------------------------------------------------------------------------------
 Projects map:  
 
Jupyter Notebooks LlamaIndex Tutorials:  
- MultiModal Retrieval GPT4V.ipynb

Folders:
- Cars (Folder with car pics)

-----------------------------------------------------------------------------------------------------------------------------

#### Advanced Multi-Modal Retrieval using GPT4V (vision) and Multi-Modal Index/Retriever (MultiModal Retrieval GPT4V.ipynb)
-----------------------------------------------------------------------------------------------------------------------------
Advanced Multi-Modal Retrieval using GPT4V (vision) and Multi-Modal Index/Retriever
Alejandro Ricciardi (Omegapy)  
created date: 01/01/2024
GitHub: https://github.com/Omegapy

Projects Description:
Multi-Modal retrieval system using LlamaIndex with GPT4-V and CLIP.
Tutorial from LlamaIndex.

LlamaIndex Multi-Modal Retrieval

- Text embedding index: Generate GPT text embeddings
- Images embedding index: [CLIP](https://github.com/openai/CLIP) embeddings from OpenAI for images


Encoding queries:
* Encode query text for text index using ada
* Encode query text for image index using CLIP

Framework: [LlamaIndex](https://github.com/run-llama/llama_index)

Steps:
1. Using Multi-Modal LLM GPT4V class to understand multiple images
2. Download texts, images, pdf raw files from related Wikipedia articles and SEC 10K report
2. Build Multi-Modal index and vector store for both texts and images
4. Retrieve relevant text and image simultaneously using Multi-Modal Retriever according to the image reasoning from Step 1

credit:  
[LlamaIndex Youtube video](https://www.youtube.com/watch?v=35RlrrgYDyU)  
[Jupyter Notebook: Multi-modal retrieval and querying](https://colab.research.google.com/gist/seldo/057406cf3b49a3ed41f9f17a02930996/gpt4v_multi_modal_retrieval.ipynb#scrollTo=3bbc9a0e)

-----------------------------------------------------------------------------------------------------------------------------

#### Image to Image Retrieval using CLIP embedding and image correlation reasoning using GPT4V  
(Image to Image Retrieval Clip GPT4V.ipynb)  

-----------------------------------------------------------------------------------------------------------------------------
Build an Image to Image retrieval program using LlamaIndex with GPT4-V and CLIP.
Tutorial from LlamaIndex.

Framework: [LlamaIndex](https://github.com/run-llama/llama_index)

Steps:
1. Download texts, images, pdf raw files from Wikipedia pages
2. Build Multi-Modal index and vector store for both texts and images
3. Retrieve relevant images given a image query using Multi-Modal Retriever
4. Using GPT4V for reasoning the correlations between the input image and retrieved images

credit:  
[LlamaIndex Youtube video](https://www.youtube.com/watch?v=35RlrrgYDyU)  
[Jupyter Notebook: Multi-modal retrieval and querying](https://colab.research.google.com/gist/seldo/e15152f0e7893353b7498331aab6f2f9/image_to_image_retrieval.ipynb#scrollTo=fc691ca8)
