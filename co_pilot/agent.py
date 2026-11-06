from google.adk.agents.llm_agent import Agent
from google.ak.tools import google_search
from google.adk.runner import InMemoryAgentRunner
import datetime as dt


# Mock tool implementation
def get_current_time(city: str) -> dict:
    """Returns the current time in a specified city."""
    current_time = dt.datetime.now()
    return {
        "status": "success",
        "city": city,
        "time": current_time.strftime("%I:%M %p"),
    }


# define the root agent with the tool
root_agent = Agent(
    model="gemini-3.6-flash",
    name="my_assistante",
    description="A helpful assistant for user questions.",
    instruction="Answer user questions to the best of your knowledge",
    tools=[get_current_time, google_search],
)
print("Root agent created successfully.")

runner = InMemoryAgentRunner(agent=root_agent)
print("Runner created successfully.")
response = await runner.run_debug(
    "What is Agent Developement Kit fropm Google? what languages is SDK available in?"
)
