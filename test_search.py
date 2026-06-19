from agents import build_search_agent

if __name__ == "__main__":
    agent = build_search_agent()
    result = agent.invoke({
        "messages": [("user", "Find recent information about fusion energy")]
    })
    print(result["messages"][-1].content)