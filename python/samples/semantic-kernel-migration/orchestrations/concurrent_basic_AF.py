# Copyright (c) Microsoft. All rights reserved.

"""Side-by-side concurrent orchestrations for Agent Framework and Semantic Kernel."""

from agent_framework import ConcurrentBuilder
from agent_framework.azure import AzureOpenAIChatClient
from azure.identity import AzureCliCredential

PROMPT = "Explain the concept of temperature from multiple scientific perspectives."

chat_client = AzureOpenAIChatClient(credential=AzureCliCredential())

physics = chat_client.create_agent(
    instructions=("You are an expert in physics. Answer questions from a physics perspective."),
    name="physics",
)

chemistry = chat_client.create_agent(
    instructions=("You are an expert in chemistry. Answer questions from a chemistry perspective."),
    name="chemistry",
)

workflow = ConcurrentBuilder().participants([physics, chemistry]).build()

def main() -> None:
    import logging

    from agent_framework.devui import serve

    logging.basicConfig(level=logging.INFO, format="%(message)s")
    logger = logging.getLogger(__name__)

    logger.info("Starting Agent Workflow ()")
    logger.info("Available at: http://localhost:8093")
    serve(entities=[workflow], port=8093, auto_open=True)


if __name__ == "__main__":
    main()
