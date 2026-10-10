from ollama import chat
from ollama import ChatResponse


class AgentCall:
    #None = none makes the tools param optional
    def __init__(self,tools: list | None = None):
        self.tools = tools
        self.messages = []

    def call_agent(self, messages: list) -> ChatResponse:

        return chat(
            model= "llama3.1:8b",
            messages=self.messages,
            tools=self.tools,
            format="json"
        )