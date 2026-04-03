from google.adk.agents import Agent

root_agent = Agent(
    name="01_test_agent",
    description="A test agent for demonstration purposes.",
    model="gemini-2.0-flash",
    instruction="""
    You are a helpful assistant that provides information and answers questions to the best of your ability.
    Ask user his/her name and greet them. Then ask how you can assist them today.
    """,
)