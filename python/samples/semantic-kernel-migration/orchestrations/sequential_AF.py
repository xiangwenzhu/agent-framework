# Copyright (c) Microsoft. All rights reserved.

"""Side-by-side sequential orchestrations for Agent Framework and Semantic Kernel."""

import asyncio

from agent_framework import SequentialBuilder
from agent_framework.azure import AzureOpenAIChatClient
from azure.identity import AzureCliCredential

PROMPT = "Write a tagline for a budget-friendly eBike."

chat_client = AzureOpenAIChatClient(credential=AzureCliCredential())

writer = chat_client.create_agent(
    instructions=("You are a concise copywriter. Provide a single, punchy marketing sentence based on the prompt."),
    name="writer",
)

reviewer = chat_client.create_agent(
    instructions=("You are a thoughtful reviewer. Give brief feedback on the previous assistant message."),
    name="reviewer",
)

workflow = SequentialBuilder().participants([writer, reviewer]).build()

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

