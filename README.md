# CULTURAL-AI-PRESERVING-KERALA-S-HERITAGE-THROUGH-RETRIEVAL-AUGMENTED-GENERATION


## PROJECT OVERVIEW:

Kerala Cultural AI is an intelligent Retrieval-Augmented Generation (RAG) system designed to provide accurate, context-aware information about Kerala's rich cultural traditions, festivals, rituals, and heritage.
The system integrates local document knowledge bases with multilingual question answering, voice input capabilities, and text-to-speech output—all powered by a local Large Language Model (LLM).

## GOAL:


Our goal is to create a culturally grounded AI historian that answers questions using stored cultural memory instead of generating generic, hallucinated responses.


## DATASET:

I'm include three type of data for creating my dataset

First one is TEXT DOCUMENTS
Cultural descriptions, festival explanations, ritual procedures, and traditional stories stored in data/text/

Second one is PDF FILES
Cultural articles, heritage documentation, and research materials stored in dataa/pdf

And last and final data in my dataset is AUDIO FILES 
Recorded cultural explanations and traditional narratives stored in dataaa/audio/, transcribed using speech-to-text


## TECH STACK:

Python, Flask, LangChain, FAISS, SentenceTransformers, LLaMA LLM, HTML, CSS, JavaScript, RAG Architecture


## PROCESS:

In my project here mainly two type of process

1st is RETRIEVAL PHASE and another is GENERATIVE PHASE

RETRIEVAL PHASE

Load and process text, PDF, and audio files
Split content using RecursiveCharacterTextSplitter (500-800 tokens, 50-100 overlap)
Generate embeddings with multilingual model
Store vectors using FAISS locally

GENERATIVE PHASE

Embed user questions into vector space
Retrieve top-k similar context chunks
Pass context to LLM for answer generation
Enforce language matching in prompts
Convert text answers to speech

## RESULT:

* Retrieval significantly improves answer factuality
* Malayalam responses are coherent with clear prompt guidance
* Mistral 7B provides stable outputs with temperature near 0
* FAISS enables fast vector search even with large datasets
* Combined document retrieval with generative AI
* Reduced hallucination through context grounding
* Supported multilingual cultural interaction
* Operated fully offline using local models


## CONCLUSION:


Cultural AI successfully demonstrates how Retrieval-Augmented Generation can be applied to preserve and deliver regional cultural knowledge through a multilingual, offline-capable system.





