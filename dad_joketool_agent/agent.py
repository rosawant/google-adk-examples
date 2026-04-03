from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm


def dad_joke_tool() -> dict:
    """Returns a random dad joke."""
    return {
        "joke": "Why don't scientists trust atoms? Because they make up everything!"
    }

root_agent = Agent(
    model=LiteLlm(model="ollama_chat/gemma:2b"),
    name="dad_joketool_agent",
    description=(
        """This agent tells dad jokes using a custom tool. It uses the LiteLlm model for generating responses."""
    ),
    instruction="""
      You roll dice and answer questions about the outcome of the dice rolls.
    """,
    tools=[
        dad_joke_tool,
    ],
)