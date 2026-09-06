# ✈️ Agentic Travel Planner

A simplified Agentic RAG travel recommendation system built with LangChain, ChromaDB, HuggingFace embeddings, Pandas and Streamlit.

## Architecture

```text
User Query
    ↓
Streamlit
    ↓
LangChain Tool-Calling Agent
    ↓
    ├── Places → ChromaDB semantic search
    ├── Hotels → Pandas filtering
    └── Flights → Pandas filtering
    ↓
Groq LLM
    ↓
Travel Itinerary


Travel_Planar/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── src/
│   ├── __init__.py
│   ├── agent.py
│   ├── config.py
│   ├── ingestion.py
│   ├── prompts.py
│   └── tools.py
│
├── data/
│   └── raw/
│       ├── places.json
│       ├── hotels.json
│       └── flights.json
│
└── vectorstore/
    └── places/