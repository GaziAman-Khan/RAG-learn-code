# RAG PDF Assistant

AI-powered PDF Question Answering system built using Retrieval-Augmented Generation (RAG), FastAPI, Streamlit, Gemini, and Qdrant Vector Database.

The application enables users to upload PDF documents, perform semantic search, and receive context-aware answers generated directly from the document content.

---

## Live Demo

**Frontend Application:**
https://rag-pdf-application.streamlit.app/

**GitHub Repository:**
https://github.com/GaziAman-Khan/RAG-learn-code

---

## Overview

RAG PDF Assistant is an end-to-end AI application that combines document processing, semantic search, vector databases, and Large Language Models (LLMs) to create an intelligent document question-answering system.

Instead of manually searching through lengthy PDFs, users can ask natural language questions and receive accurate, context-aware answers grounded in the uploaded document.

---

## Problem Statement

Traditional document search relies heavily on keyword matching and manual reading, making it difficult to quickly locate relevant information.

This project addresses that challenge by:

* Converting document content into semantic embeddings
* Storing embeddings in a vector database
* Retrieving relevant content using similarity search
* Generating contextual answers using Gemini

---

## Features

* Upload PDF documents through a web interface
* Automatic text extraction and chunking
* Semantic embeddings using Gemini Embedding API
* Vector storage and retrieval with Qdrant
* Context-aware question answering using Gemini
* Adjustable Top-K retrieval
* Interactive Streamlit user interface
* FastAPI backend APIs
* Cloud deployment using Render and Streamlit Community Cloud

---

## Tech Stack

### Frontend

* Streamlit

### Backend

* FastAPI

### AI & RAG

* Google Gemini API
* Gemini Embeddings
* Retrieval-Augmented Generation (RAG)

### Vector Database

* Qdrant Cloud

### Deployment

* Streamlit Community Cloud
* Render

---

## System Architecture

### PDF Ingestion Flow

User Uploads PDF

↓

Streamlit Frontend

↓

FastAPI Backend

↓

PDF Text Extraction

↓

Document Chunking

↓

Gemini Embeddings

↓

Qdrant Vector Database

---

### Question Answering Flow

User Question

↓

FastAPI Backend

↓

Question Embedding

↓

Qdrant Similarity Search

↓

Top-K Relevant Chunks

↓

Gemini LLM

↓

Generated Answer

↓

Streamlit Frontend

---

## Project Workflow

### Document Ingestion

1. User uploads a PDF document.
2. Text is extracted from the PDF.
3. Content is divided into smaller chunks.
4. Gemini generates embeddings for each chunk.
5. Embeddings are stored in Qdrant.

### Question Answering

1. User submits a question.
2. The question is converted into an embedding.
3. Qdrant retrieves the most relevant chunks.
4. Retrieved context is sent to Gemini.
5. Gemini generates a context-aware response.
6. The answer is displayed in the Streamlit application.

---

## Screenshots

### PDF Upload Interface

<img width="1915" height="838" alt="image" src="https://github.com/user-attachments/assets/62ac75a0-989f-4b81-b51b-6488eee3b735" />


### Question Answering Interface

<img width="959" height="416" alt="image" src="https://github.com/user-attachments/assets/75090b9d-4457-44d9-a169-3e5c5947b5d2" />


### Generated Response

<img width="960" height="416" alt="image" src="https://github.com/user-attachments/assets/e7ac0ac8-75bd-4747-a01c-af30f1957bc9" />


---

## Installation

### Clone Repository

```bash
git clone https://github.com/GaziAman-Khan/RAG-learn-code.git

cd RAG-learn-code
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run FastAPI Backend

```bash
uvicorn main:app --reload
```

### Run Streamlit Frontend

```bash
streamlit run streamlit_app.py
```

---

## Environment Variables

Create a `.env` file and add:

```env
GEMINI_API_KEY=your_api_key

QDRANT_URL=your_qdrant_url

QDRANT_API_KEY=your_qdrant_api_key
```

---

## Key Learnings

Through this project, I gained hands-on experience with:

* Retrieval-Augmented Generation (RAG)
* Vector Databases and Semantic Search
* Embedding Models
* FastAPI Backend Development
* Streamlit Application Development
* API Integration
* Cloud Deployment
* Building End-to-End AI Applications

---

## Future Improvements

* Multi-document querying
* Source citations in responses
* Conversation memory
* Faster batch embedding generation
* Support for DOCX and TXT files
* Advanced reranking strategies

---

## Author

**Gazi Aman Khan**

AI & ML Engineer | GenAI & Data Science Enthusiast

GitHub: https://github.com/GaziAman-Khan
