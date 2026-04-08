from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

def generate_dockerfile() -> str:
    """Generates a Dockerfile for a user application."""
    dockerfile = """
    ONLY Generate an ideal Dockerfile with best practices. Do not provide any description
    Include:
    - Base image
    - Installing dependencies
    - Setting working directory
    - Adding source code
    - Running the application
    - Do not repeat steps, only include necessary steps for a simple application
    - Use multi-stage builds if necessary
    - Use environment variables for configuration
    - Expose necessary ports
    - Use a non-root user for security
    - Include a health check if applicable
    - Optimize for caching layers to speed up builds
    - Keep the Dockerfile clean and organized
    - Do not include any comments or explanations, only the Dockerfile content
    """
    return dockerfile.strip()

root_agent = Agent(
    model=LiteLlm(model="ollama_chat/qwen3.5:0.8b"),
    name="generate_dockerfile_agent",
    description=(
        """This agent generates Dockerfiles for user applications. It uses the LiteLlm model for generating responses."""
    ),
    instruction="""
    You are a helpful assistant that generates Dockerfiles. Use the 'generate_dockerfile' tool to create a Dockerfile for a user application.
    - generate_dockerfile: A tool that generates a Dockerfile for a user application.
    """,
    tools=[
        generate_dockerfile,
    ],
)