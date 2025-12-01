# **🤖 Local LangChain Chatbot (Ollama + Streaming)**

A lightweight, fully local chatbot built with **LangChain** and **Ollama**.
It uses the `gemma3:4b` model by default, keeps track of the conversation history, and streams responses token-by-token for a smoother, more natural chat experience.

### **✨ Features**

* **Runs 100% locally** using Ollama (no external API calls).
* **Conversation memory** — the bot always remembers the last turn.
* **Streaming responses** instead of waiting for a full generated chunk.
* **Graceful exit** — type `end` to close the session cleanly.
* **Simple, single-file architecture** for quick experimentation and extension.

### **🧰 Tech Stack**

* Python
* LangChain
* Ollama (`gemma3:4b`)

### **🚀 How to Run**

1. Install **Ollama** and pull the model:

   ```bash
   ollama pull gemma3:4b
   ```
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
3. Start the chatbot:

   ```bash
   python app.py
   ```

### **🛠️ Planned Improvements**

* Add **custom tools** (search, files, shell, calculators, etc.)
* Integrate a small **RAG** layer for knowledge augmentation
* Optional **fine-tuning** of the model for better domain answers
* Add **evaluation** workflows to measure model behavior and quality
* Refactor into modules as the project grows

### **💡 Why This Exists**

This project started as a minimal playground to explore:

* clean LangChain patterns
* local LLM workflows
* streaming UX
* building practical, hackable prototypes

It’s intentionally simple — but also intended to grow.

### **📄 License**

MIT License.
