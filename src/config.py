import streamlit as st


GROQ_API_KEY = st.secrets["GROQ_API_KEY"]

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

VECTORSTORE_PATH = "vectorstore/places"

PLACES_DATA_PATH = "data/raw/places.json"
HOTELS_DATA_PATH = "data/raw/hotels.json"
FLIGHTS_DATA_PATH = "data/raw/flights.json"

TOP_K = 5