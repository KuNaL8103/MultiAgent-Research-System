from langchain.agents import create_agent
from langchain_groq import ChatGroq
from tools import web_search
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0)

def build_search_agent():
    return create_agent(
        model=llm,
        tools=[web_search],
    )