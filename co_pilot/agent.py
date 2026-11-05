from google.adk.agents.llm_agent import Agent
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


root_agent = Agent(
    model="gemini-3.6-flash",
    name="root_agent",
    description="A helpful assistant for user questions.",
    instruction="Answer user questions to the best of your knowledge",
    tools=[get_current_time],
)
