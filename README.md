# 🤖 Agentic RAG Chatbot

An intelligent, agent-based chatbot designed to answer questions directly from your uploaded documents, whether it’s a PDF, PPTX, CSV, DOCX, or TXT. This project brings together Retrieval-Augmented Generation (RAG), OpenAI’s language models, and modular agent architecture to make document-based Q&A seamless and efficient.

---

## 🚀 What It Does

Have a bunch of files but no time to dig through them? Just upload your documents, ask a question, and the chatbot will:
1. Parse and understand the documents,
2. Retrieve the most relevant sections,
3. Generate a helpful, context-aware answer using OpenAI.

This is more than just a chatbot, it’s a practical research assistant for working with multi-format documents.

---

## 🧠 Architecture Overview

This system is built on a **modular agentic framework**:

- **IngestionAgent**: Parses and preprocesses uploaded documents.
- **RetrievalAgent**: Embeds content using sentence-transformers and retrieves semantically relevant chunks via FAISS.
- **LLMResponseAgent**: Generates an answer using OpenAI's `gpt-3.5-turbo`, based on the retrieved context.
- **Model Context Protocol (MCP)**: All agents communicate via structured messages, maintaining clean separation and traceability.

Each agent handles a well-defined responsibility, making the system more scalable and maintainable.

---

## 💻 Tech Stack

- **Language Model**: OpenAI GPT-3.5
- **Embeddings**: Sentence Transformers
- **Vector Store**: FAISS
- **Parsing Libraries**: PyMuPDF, python-docx, python-pptx
- **UI**: Streamlit
- **Environment Management**: Python-dotenv

---


## ⚙️ Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/SatwikaKadiyala/AGENTIC_RAG_CHATBOT.git
cd AGENTIC_RAG_CHATBOT
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add your OpenAI API key

Create a .env file in the root directory:

```
OPENAI_API_KEY=your-api-key-here
```

### 4. Run the app

```bash
streamlit run ui/app.py
```

---

## 📚 Supported File Formats

* PDF ('.pdf')
* Word Documents ('.docx')
* PowerPoint ('.pptx')
* CSV ('.csv')
* TXT ('.txt')
  

---

## ✨ Features

* Multi-format document ingestion
* Agent-based modular architecture
* Clean and intuitive user interface
* Multi-turn conversation support
* Source-aware responses



