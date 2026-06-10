# RAG-learn-code
RAG Project Initialization
# RAG PDF Assistant

AI-powered PDF Question Answering system built using Retrieval-Augmented Generation (RAG) to enable intelligent document search and contextual responses from uploaded PDFs.

## Overview

Reading large PDF documents and manually searching for information can be time-consuming. RAG PDF Assistant solves this problem by combining semantic search and Generative AI to retrieve relevant document content and generate context-aware answers.

This project allows users to upload PDFs, ask questions, and receive intelligent responses through an interactive web interface.

## Problem Statement

Traditional document search relies on keyword matching and manual reading, which often misses context and slows information retrieval. This project was developed to create an AI-driven system capable of understanding document meaning and answering user queries more efficiently.

## Features

* PDF Upload and Processing
* Semantic Search using Vector Database
* Context-Aware Question Answering
* Gemini-based Response Generation
* Persistent Vector Storage with Qdrant
* Interactive Streamlit Interface
* Event-driven PDF ingestion and query processing using Inngest functions
* Docker-based Containerized Setup
* Local Deployment

## Tech Stack

**Frontend**

* Streamlit

**Backend**

* FastAPI

**AI / RAG**

* Gemini API
* Qdrant Vector Database
* Retrieval-Augmented Generation (RAG)

**Workflow & Infrastructure**

* Inngest
* Docker

## System Architecture

### FLOW 1: INGESTION

PDF Upload
    ->
Inngest Event
    ->
Chunk PDF
    ->
Generate Embeddings
    ->
Store in Qdrant


### FLOW 2: QUERY

User Question
    ->
Inngest Event
    ->
Embed Query
    ->
Retrieve Top-K Chunks
    ->
Gemini
    ->
Answer

## Project Workflow

1. User uploads a PDF document.
2. Text is extracted and processed.
3. Document embeddings are created and stored in Qdrant.
4. User submits a question.
5. Relevant document chunks are retrieved through semantic search.
6. Gemini generates a context-aware response.
7. Streamlit displays the final answer.

## Project Structure

```bash
RAG-PDF-Assistant/
│
├── app.py
├── main.py
├── qdrant_storage.py
├── streamlit_app.py
├── Dockerfile
├── requirements.txt
└── README.md
```

## Installation & Setup

### Clone Repository

```bash
git clone https://github.com/GaziAman-Khan/RAG-learn-code/tree/main
cd RAG-learn-code
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Backend

```bash
uvicorn main:app --reload
```

### Run Streamlit Frontend

```bash
streamlit run app.py
```

## Usage

1. Launch the application locally.
2. Upload a PDF document.
3. Ask questions related to the document.
4. Receive AI-generated contextual answers.

## Key Learnings

Through this project, I gained hands-on experience with:

* Retrieval-Augmented Generation (RAG)
* Vector Databases and Semantic Search
* FastAPI Backend Development
* Event-Driven Processing using Inngest
* Docker-based Application Setup
* Building AI-powered Document Intelligence Systems


## Author

**Gazi Aman Khan**
AI & ML Engineer | GenAI & Data Science Enthusiast
