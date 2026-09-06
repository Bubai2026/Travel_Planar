import streamlit as st
from src.agent import plan_trip

st.set_page_config(
    page_title="Agentic Travel Planner",
    page_icon="✈️",
    layout="centered"
)

st.title("✈️ Agentic Travel Planner")

st.write(
    "Plan your trip using an AI agent powered by "
    "LangChain, ChromaDB and structured travel data."
)

query = st.text_area(
    "Describe your trip",
    placeholder=(
        "Example: Plan a 3-day trip to Goa from Kolkata "
        "for two people under INR 25,000. "
        "We like beaches and nightlife."
    ),
    height=150
)

if st.button("Generate Itinerary", type="primary"):
    if not query.strip():
        st.warning("Please describe your trip first.")
    else:
        with st.spinner("Planning your trip..."):
            try:
                response = plan_trip(query)
                st.markdown(response)
            except Exception as e:
                st.error(f"Something went wrong: {str(e)}")

with st.expander("About this project"):
    st.write(
        """
        This is an educational Agentic RAG project.

        The system uses:
        - LangChain for agent orchestration
        - ChromaDB for semantic retrieval
        - HuggingFace embeddings
        - Pandas for structured hotel and flight filtering
        - Groq LLM for reasoning and response generation

        Flight and hotel information is demonstration data and is not real-time.
        """
    )
