# 🚀 Custom RAG Pipeline for PDF Documents

An end-to-end **Retrieval-Augmented Generation (RAG)** pipeline built from scratch in Python using **LangChain**, **ChromaDB**, **SentenceTransformers**, and **PyMuPDF**. 

This system ingests PDF documents, converts them into dense vector embeddings, stores them in a persistent vector database, and uses semantic search to supply relevant context to an LLM for precise question answering.

---

## 📋 Table of Contents
- [Features](#-features)
- [Architecture](#-architecture)
- [Tech Stack](#-tech-stack)
- [Installation & Setup](#-installation--setup)
- [Project Structure](#-project-structure)
- [Usage](#-usage)
- [Module Breakdown](#-module-breakdown)
- [License](#-license)

---

## ✨ Features
* **Automated PDF Ingestion**: Load and parse multiple PDF files from a target folder.
* **Vector Embeddings**: Generate dense text embeddings using `SentenceTransformers` (`all-MiniLM-L6-v2`).
* **Persistent Vector Storage**: Store and index vectors using `ChromaDB` for fast similarity searches.
* **Semantic Retriever**: Custom ranking algorithm that converts distance to cosine similarity scores and applies a `score_threshold`.
* **Context-Augmented Generation**: Generates accurate, context-grounded responses using LLM invocation.

---

## 🏗️ Architecture

```text
 ┌─────────────┐     ┌──────────────────┐     ┌─────────────────────┐
 │  PDF Files  │ ──► │ PyMuPDF Ingestion│ ──► │  Text Extracted     │
 └─────────────┘     └──────────────────┘     └──────────┬──────────┘
                                                         │
                                                         ▼
 ┌─────────────┐     ┌──────────────────┐     ┌─────────────────────┐
 │  LLM Answer │ ◄── │ Augmented Prompt │ ◄── │ SentenceTransformer │
 └─────────────┘     └──────────────────┘     │   (Embeddings)      │
                              ▲               └──────────┬──────────┘
                              │                          │
                     ┌──────────────────┐                ▼
                     │   RAG Retriever  │ ◄─── ┌───────────────────┐
                     └──────────────────┘      │ Chroma Vector DB  │
                                               └───────────────────









