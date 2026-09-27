from ollama import chat
from ollama import ChatResponse
from sympy import content


class AgentCall:
    def __init__(self, messages: list, tools: list):
        self.messages = messages
        self.tools = tools
        self.message_history = []
        self.model_message_history = []

    def callAgent(self) -> ChatResponse:
        print(self.messages)

        return chat(
            model= "llama3.1:8b",
            messages=self.messages,
            tools=self.tools
        )

    def construct_message(self):
        system_message = {
            'role': 'system',
            'content': 'Ignore tools unless the prompts are related to files. '
                       'Give a direct answer with your own reasoning.'
                       'Do not create your own tools'
                       'You are an LLM and my virtual assistant.'
        }

        self.messages = [
            system_message,
            #the * means take every elemt from self.message_history and put each one into this new list
            *self.message_history
        ]

    def add_tools(self, tools:list):
        self.tools=tools


    def build_message_history(self, role: str, user_content: str):
        self.message_history.append({
            'role': role,
            'content': user_content
        })

    def build_agent_message_history(self, agent_content: str):
        self.model_message_history.append({
            agent_content
        })



