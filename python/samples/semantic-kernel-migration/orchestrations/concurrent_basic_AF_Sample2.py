# Copyright (c) Microsoft. All rights reserved.

"""Side-by-side concurrent orchestrations for Agent Framework and Semantic Kernel."""

from agent_framework import ConcurrentBuilder
from agent_framework.azure import AzureOpenAIChatClient
from azure.identity import AzureCliCredential

PROMPT = "Explain the concept of temperature from multiple scientific perspectives."

chat_client = AzureOpenAIChatClient(credential=AzureCliCredential())

researcher = chat_client.create_agent(
    instructions=(
        "You're an expert market and product researcher. Given a prompt, provide concise, factual insights,"
        " opportunities, and risks."
    ),
    name="researcher",
)

marketer = chat_client.create_agent(
    instructions=(
        "You're a creative marketing strategist. Craft compelling value propositions and target messaging"
        " aligned to the prompt."
    ),
    name="marketer",
)

legal = chat_client.create_agent(
    instructions=(
        "You're a cautious legal/compliance reviewer. Highlight constraints, disclaimers, and policy concerns"
        " based on the prompt."
    ),
    name="legal",
)
workflow = ConcurrentBuilder().participants([researcher, marketer, legal]).build()

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
