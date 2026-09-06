import json
import pandas as pd

from langchain.tools import tool
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

from src.config import (
    EMBEDDING_MODEL,
    VECTORSTORE_PATH,
    HOTELS_DATA_PATH,
    FLIGHTS_DATA_PATH
)

embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)

places_vectorstore = Chroma(
    collection_name="travel_places",
    persist_directory=VECTORSTORE_PATH,
    embedding_function=embeddings
)

with open(HOTELS_DATA_PATH, "r", encoding="utf-8") as file:
    hotels_data = json.load(file)

with open(FLIGHTS_DATA_PATH, "r", encoding="utf-8") as file:
    flights_data = json.load(file)

hotels_df = pd.DataFrame(hotels_data)
flights_df = pd.DataFrame(flights_data)

@tool
def search_places(query: str, city: str = "", k: int = 5) -> str:
    """Search tourist attractions and places using semantic search."""
    try:
        if city:
            results = places_vectorstore.similarity_search(
                query, k=k, filter={"city": city}
            )
        else:
            results = places_vectorstore.similarity_search(query, k=k)

        if not results:
            return "No places found."

        return "\n\n---\n\n".join(
            result.page_content for result in results
        )
    except Exception as e:
        return f"Error while searching places: {str(e)}"

@tool
def search_hotels(city: str, max_price: float = 0, min_stars: int = 0) -> str:
    """Search hotels in a city with optional price and star-rating filters."""
    df = hotels_df.copy()
    df = df[df["city"].str.lower() == city.lower()]

    if max_price > 0:
        df = df[df["price_per_night"] <= max_price]

    if min_stars > 0:
        df = df[df["stars"] >= min_stars]

    if df.empty:
        return "No hotels found matching the requested criteria."

    output = []
    for _, row in df.head(5).iterrows():
        output.append(
            f"Hotel: {row['name']}\n"
            f"City: {row['city']}\n"
            f"Location: {row['location']}\n"
            f"Price per night: INR {row['price_per_night']}\n"
            f"Stars: {row['stars']}\n"
            f"Rating: {row['rating']}\n"
            f"Amenities: {', '.join(row['amenities'])}\n"
            f"Description: {row['description']}"
        )

    return "\n\n---\n\n".join(output)

@tool
def search_flights(from_city: str, to_city: str, max_price: float = 0) -> str:
    """Search flights between two cities with an optional maximum price."""
    df = flights_df.copy()
    df = df[
        (df["from"].str.lower() == from_city.lower()) &
        (df["to"].str.lower() == to_city.lower())
    ]

    if max_price > 0:
        df = df[df["price"] <= max_price]

    if df.empty:
        return "No flights found matching the requested criteria."

    output = []
    for _, row in df.head(5).iterrows():
        output.append(
            f"Airline: {row['airline']}\n"
            f"Route: {row['from']} -> {row['to']}\n"
            f"Price: INR {row['price']}\n"
            f"Duration: {row['duration']}\n"
            f"Stops: {row['stops']}"
        )

    return "\n\n---\n\n".join(output)
