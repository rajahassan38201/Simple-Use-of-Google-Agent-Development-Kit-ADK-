from google.adk.agents import Agent
from google.adk.tools import google_search

agent_description = """
First_Agent is an intelligent assistant designed to leverage the Google Search tool for information retrieval and knowledge synthesis. 
It is capable of understanding user queries, formulating effective search strategies, and providing concise and relevant answers based on the search results.
"""

agent_instruction = """
You are an intelligent assistant whose primary function is to answer user questions using the provided Google Search tool. """

root_agent = Agent(
    name="First_Agent",
    model="gemini-2.0-flash-exp",
    description=agent_description,
    instruction=agent_instruction,
    tools=[google_search]
)