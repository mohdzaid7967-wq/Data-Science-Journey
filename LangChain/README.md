# LangChain — Building LLM-Powered Applications

This section of my **Data Science Journey** focuses on **LangChain**, a framework for developing applications powered by Large Language Models (LLMs).

The goal is to understand how LLMs can be connected with prompts, tools, external data sources, memory, structured outputs, agents, and application workflows to build practical AI systems.

---

## 🧠 What is LangChain?

LangChain is a framework for building applications around Large Language Models.

Instead of using an LLM only for simple question-and-answer tasks, LangChain provides abstractions for connecting an LLM with:

- Prompts
- Tools
- APIs
- Databases
- Documents
- Retrievers
- Memory
- Structured outputs
- Agents
- Application workflows

A simplified architecture:

```text
User
  ↓
Application
  ↓
LangChain
  ↓
Prompt / Model / Tools / Retrieval
  ↓
LLM
  ↓
Response

Typical LangChain Application Architecture
                 User
                   ↓
              Application
                   ↓
                Prompt
                   ↓
               LangChain
              /    |     \
             /     |      \
          Tools   RAG     Memory
            ↓      ↓        ↓
          APIs   Vector   History
                 Store
                   ↓
                  LLM
                   ↓
             Final Response