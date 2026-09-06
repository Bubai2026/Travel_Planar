import json
import os

from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

from src.config import (
    PLACES_DATA_PATH,
    VECTORSTORE_PATH,
    EMBEDDING_MODEL
)

def load_places():
    with open(PLACES_DATA_PATH, "r", encoding="utf-8") as file:
        return json.load(file)

def create_place_documents(places):
    documents = []

    for place in places:
        text = f"""
Name: {place['name']}
City: {place['city']}
Type: {place['type']}
Rating: {place['rating']}
Approximate Cost: INR {place['price']}
Best For: {', '.join(place['best_for'])}
Typical Duration: {place['duration']}

Description:
{place['description']}
""".strip()

        metadata = {
            "id": place["id"],
            "name": place["name"],
            "city": place["city"],
            "type": place["type"],
            "rating": place["rating"],
            "price": place["price"]
        }

        documents.append(Document(page_content=text, metadata=metadata))

    return documents

def get_embeddings():
    return HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)

def build_vectorstore():
    places = load_places()
    documents = create_place_documents(places)
    embeddings = get_embeddings()

    vectorstore = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        persist_directory=VECTORSTORE_PATH,
        collection_name="travel_places"
    )

    print(f"Created vector store with {len(documents)} documents.")
    return vectorstore

if __name__ == "__main__":
    os.makedirs(VECTORSTORE_PATH, exist_ok=True)
    build_vectorstore()
