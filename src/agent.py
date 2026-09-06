
from langchain_groq import ChatGroq
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from src.config import GROQ_API_KEY
from src.prompts import SYSTEM_PROMPT
from src.tools import search_places, search_hotels, search_flights


llm = ChatGroq(
    model="openai/gpt-oss-safeguard-20b",
    temperature=0,
    api_key=GROQ_API_KEY
)

tools = [
    search_places,
    search_hotels,
    search_flights
]

prompt = ChatPromptTemplate.from_messages([
    ("system", SYSTEM_PROMPT),
    ("human", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad")
])

agent = create_tool_calling_agent(
    llm=llm,
    tools=tools,
    prompt=prompt
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    max_iterations=8,
    handle_parsing_errors=True
)


def plan_trip(user_query: str) -> str:
    result = agent_executor.invoke({
        "input": user_query
    })

    return result["output"]
