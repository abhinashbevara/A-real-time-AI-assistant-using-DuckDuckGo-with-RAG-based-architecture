# 🤖 Real-Time AI Assistant (RAG + DuckDuckGo + Ollama)

A real-time AI assistant that answers user queries using **live web search** and a **local LLM (Ollama)**.
This project implements a **Retrieval-Augmented Generation (RAG)** pipeline using LangChain.

---

## 🚀 Features

* 🔍 Real-time search using DuckDuckGo
* 🧠 Local LLM powered by Ollama (llama3 / phi3)
* 🔗 RAG pipeline (Search → Context → LLM → Answer)
* ⚡ Lightweight and runs locally
* 💬 Interactive CLI chatbot
* 🛠 Built using LangChain

---

## 🧠 Architecture

User Query → DuckDuckGo Search → Context Injection → LLM → Response

This ensures answers are:

* Up-to-date 📅
* Relevant 🎯
* Context-aware 🧩

---

## 🛠 Tech Stack

* Python 🐍
* LangChain
* Ollama (Local LLM)
* DuckDuckGo Search Tool
* Runnable Pipelines

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/abhinashbevara/A-real-time-AI-assistant-using-DuckDuckGo-with-RAG-based-architecture.git
cd A-real-time-AI-assistant-using-DuckDuckGo-with-RAG-based-architecture
```

---

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Install and run Ollama

Download from: https://ollama.com

Then run:

```bash
ollama pull llama3:2b
ollama run llama3:2b
```

---

## ▶️ Usage

Run the application:

```bash
python app.py
```

Example:

```text
You: What is machine learning?
🤖: Machine learning is a field of AI that enables systems to learn from data...
```

---

## 📁 Project Structure

```
├── app.py
├── requirements.txt
└── README.md
```

---

## ⚠️ Notes

* Ensure Ollama is running before starting the app
* For low RAM systems, use:

```python
OllamaLLM(model="phi3")
```

---

## 🌟 Future Improvements

* 🌐 Web UI using Streamlit
* 🧠 Add conversation memory
* 📄 Document-based RAG (PDFs, Docs)
* ⚡ Faster API-based models

---

## 🙌 Acknowledgements

* LangChain
* Ollama
* DuckDuckGo

---

## 📬 Contact

If you liked this project, feel free to connect or contribute!
** Name:B.Abhinash
** Contact: abhibevera06@gmail.com

---

⭐ Don't forget to star the repo if you found it useful!
