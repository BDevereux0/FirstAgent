from ollama import chat
from ollama import ChatResponse
from sympy import false

from tools.CompleteToolList import CompleteToolList


class AgentCall:
    #None = none makes the tools param optional
    def __init__(self,tools: list | None = None):
        self.tools = CompleteToolList().tools

    def call_agent(self, user_messages: list) -> ChatResponse:
        return chat(
            model= "qwen3.5:9b",
            messages=user_messages,
            tools=self.tools,
            think=False
        )
    #Added this second one because the ollama docs say that the model will heavely favor
    #a tool response if they are present in the model call.
    def router_call_agent(self, user_messages:list) -> ChatResponse:
        tools = CompleteToolList()
        tool_list = tools.tools
        return chat(
            model = "qwen3.5:9b",
            messages=user_messages,
            format="json",
            think=False
        )