from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
import random


def dad_joke_tool() -> dict:
    """Returns a random dad joke."""
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why don't skeletons fight each other? They don't have the guts.",
        "What do you call fake spaghetti? An impasta!",
        "Why did the bicycle fall over? Because it was two-tired!"
    ]
    return {"joke": random.choice(jokes)}

root_agent = Agent(
    model=LiteLlm(model="ollama_chat/qwen3.5:0.8b"),
    name="dad_joketool_agent",
    description=(
        """This agent tells dad jokes using a custom tool. It uses the LiteLlm model for generating responses."""
    ),
    instruction="""
    You are a helpful assistant that tells dad jokes. Use the 'dad_joke_tool' to get a random dad joke and share it with the user.
    - dad_joke_tool: A tool that returns a random dad joke when called.
    """,
    tools=[
        dad_joke_tool,
    ],
)