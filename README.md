# ✈️ Agentic Travel Planner

A simple travel planning assistant built with Python, LangChain, Groq, ChromaDB, HuggingFace embeddings, Pandas, and Streamlit.

The idea behind the project is straightforward: instead of sending every travel question directly to an LLM, the agent can use different tools to find places, hotels, and flights from the available data and then build an itinerary around the user's requirements.

## Live Demo

[Try the app on Streamlit](https://travelplanar-eebi4vfdrzhwt3hdfelqfh.streamlit.app/)

> **Note:** Flight and hotel information in this project comes from local demo datasets. It is not real-time booking or availability data.

## What it can do

- Plan a day-wise trip based on a natural-language request
- Find places using semantic search with ChromaDB
- Search hotels using structured Pandas filters
- Search flights using structured Pandas filters
- Consider budget and user interests while creating an itinerary
- Use an LLM agent to decide which tools are needed
- Run as a Streamlit web application

## How it works

The application follows this basic flow:

```text
User
  ↓
Streamlit UI
  ↓
LangChain Agent
  ↓
 ┌─────────────────┬─────────────────┬─────────────────┐
 ↓                 ↓                 ↓
Places Search    Hotel Search     Flight Search
 ↓                 ↓                 ↓
ChromaDB          Pandas            Pandas
 ↓                 ↓                 ↓
 └─────────────────┴─────────────────┴─────────────────┘
                      ↓
                   Groq LLM
                      ↓
                Travel Itinerary
```

For places, the project uses HuggingFace embeddings with ChromaDB to find semantically relevant attractions.

Hotels and flights are stored as JSON data and filtered with Pandas based on the user's requirements.

The agent then uses the retrieved information to generate the final itinerary.

## Project structure

```text
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
```

### Main files

**`app.py`**  
The Streamlit interface. It accepts the user's travel request and displays the generated itinerary.

**`src/agent.py`**  
Creates the LangChain agent and connects it with the available travel tools and Groq model.

**`src/tools.py`**  
Contains the tools used by the agent:
- `search_places`
- `search_hotels`
- `search_flights`

**`src/ingestion.py`**  
Creates the ChromaDB vector store from the places dataset.

**`src/prompts.py`**  
Contains the instructions that guide the agent when planning a trip.

**`src/config.py`**  
Contains application configuration and reads the Groq API key from Streamlit Secrets.

## Tech stack

- **Python** - application development
- **Streamlit** - web interface and deployment
- **LangChain** - agent and tool orchestration
- **Groq** - LLM inference
- **ChromaDB** - vector database
- **HuggingFace** - text embeddings
- **Pandas** - hotel and flight filtering
- **JSON** - local travel datasets

## Running locally

### 1. Clone the repository

```bash
git clone https://github.com/Bubai2026/Travel_Planar.git
cd Travel_Planar
```

### 2. Create a virtual environment

On Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

On Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add the Groq API key

Create:

```text
.streamlit/secrets.toml
```

and add:

```toml
GROQ_API_KEY = "your_groq_api_key"
```

Do not commit this file to GitHub.

### 5. Start the application

```bash
streamlit run app.py
```

## Deployment

The application is deployed on **Streamlit Community Cloud**.

Deployment settings:

```text
Repository: Bubai2026/Travel_Planar
Branch: main
Main file: app.py
```

The Groq API key is managed through **Streamlit Deployment Secrets** rather than being stored in the repository.

In Streamlit Community Cloud, add:

```toml
GROQ_API_KEY = "your_groq_api_key"
```

under the app's **Secrets** settings.

## Data

The project currently uses three local datasets:

- `places.json` - tourist places and their details
- `hotels.json` - hotel information
- `flights.json` - flight information

These datasets are intentionally small and are mainly used to demonstrate the agent + RAG workflow.

## Rebuilding the vector store

If `places.json` is changed, the ChromaDB store can be rebuilt with:

```bash
python -m src.ingestion
```

The generated vector store is stored in:

```text
vectorstore/places/
```

## Example

You can try a request such as:

```text
Plan a 3-day trip to Goa from Kolkata for two people
under INR 25,000. We like beaches and nightlife.
```

The agent can search for suitable places, hotels, and flights and then use those results to create the itinerary.

## Limitations

This is a project for learning and demonstration.

- Flight data is static.
- Hotel data is static.
- Prices are not live.
- Availability is not live.
- The application does not make bookings.
- The available destinations and travel data are limited to the datasets included in the repository.

So the generated plans should not be treated as real-time travel or booking information.

## Why I built this

This project was built to get hands-on experience with a practical LLM application rather than using an LLM as a simple chatbot.

The main focus was on combining:

```text
LLM
+
Tool Calling
+
RAG / Vector Search
+
Structured Data
+
Web Application
```

into one small application.

## Repository

GitHub:  
https://github.com/Bubai2026/Travel_Planar
