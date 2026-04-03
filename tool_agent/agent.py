from google.adk.agents import Agent
# from google.adk.tools import Tool
import datetime


def get_current_time_tool(city: str) -> dict:
    """Returns the current time in format DD:MM:YYYY HH:MM:SS"""
    return {
        "current_time": datetime.now().strftime("%d:%m:%Y %H:%M:%S")
    }

root_agent = Agent(
    name="test_agent",
    description="A test agent for demonstration purposes.",
    model="gemini-2.0-flash",
    instruction="""
    You are a helpful assistant that provides information and answers questions to the best of your ability.
    Ask user his/her name and greet them. Then ask how you can assist them today.
    """,
    tools=[get_current_time_tool],
)