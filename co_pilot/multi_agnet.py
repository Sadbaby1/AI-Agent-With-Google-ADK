from googlr.adk.agents import Agent, SequeentialAgent, ParallelAgent, LoopAgent
from google.adk.tools import google_search, AgentTool, FunctionTool
from google.adk.runner import InMemoryAgentRunner


# resaerch agent
research_agent = Agent(
    name="ResearchAgent",
    model="gemini-3.6-flash",
    instruction="""You are spetialized reserach agent. Your only jopb is to assist with research tasks is to
    use google_serach too to find 2-3 relevant pieces of relevanmt information on the given topic and present 
    fidings in a clear and concise manner. You should not provide any personal opinions or speculations. 
    .""",
    tools=[google_search],
    output_key="research_findings",  # the result of this agnet will be stored in the session state with this key
)
print("Research agent created successfully.")

# summarizer agent
summarizer_agent = Agent(
    name="SummarizerAgent",
    model="gemini-3.6-flash",
    instruction="""You are a specialized summarizer agent. Read the research findings:{research_findings} 
    create a concise summary as bulleted list with 3 -5 points.""",
)

print("Research and Summarizer agents created successfully.")


# Root Coordinatror: Orcherstrate the workflow between the research agent and the summarizer agent
root_agent = Agent(
    name="ReacsearchCoordinantor",
    model="gemini-3.6-flash",
    instruction="""You are a research coordinator agent. Your goal is answer the user's query by orchestrating 
    1. First you MUST call the 'ResearchAgentan' tool to find inform,ation on the topic provided by the user
    2.NEXT, after receving the research findings, you MUST call the 'SummarizerAgent' tool to create a concise summary of the research findings.
    3. Finally, present the final summary to the user as the your final response.""",
    # wrap the sub-agents in 'AgentTool' to make them callable by the root agent.
    tools=[AgentTool(research_agent), AgentTool(summarizer_agent)],
)

print("Root agent created successfully.")

runner = InMemoryAgentRunner(agent=root_agent)
response = await runner.run_debug(
    "What are the latest advancements in quantum computing to day and what do they mean?"
)
