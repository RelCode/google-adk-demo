from google.adk.agents.llm_agent import Agent
from google.adk.models.lite_llm import LiteLlm
import os
from dotenv import load_dotenv

load_dotenv() # load environment variables from .env file

os.environ["AZURE_AI_API_KEY"] = os.getenv("AZURE_KEY","")

print("AZURE_AI_API_KEY:", os.environ["AZURE_AI_API_KEY"])

# mock tool implementation
def get_current_weather(location: str):
    """Get the current weather in a given location"""
    return f"The current weather in {location} is sunny with a temperature of 25°C."

root_agent = Agent(
    model=LiteLlm(model="azure_ai/gpt-5.2"),
    name="root_agent",
    description="The root agent that receives user queries and delegates tasks to sub-agents.",
    instruction="You are a helpful assistant that can answer questions about the weather. If the user asks about the weather, use the get_current_weather tool to provide an answer.",
    tools=[get_current_weather]
)