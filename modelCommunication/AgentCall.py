from ollama import chat
from ollama import ChatResponse


class AgentCall:
    def __init__(self, messages: list, tools: list):
        self.messages = messages
        self.tools = tools
        self.message_history = []
        self.model_message_history = []

    def callAgent(self) -> ChatResponse:
        return chat(
            model= "llama3.1:8b",
            messages=self.messages,
            tools=self.tools
        )

    #constructs messages by adding each previous message to the model call, so it knows what we've been
    #talking about
    def construct_message(self):
        self.messages = [
             {                  'role': 'system',
                                 'content': 'Always respond with text, not just a tool response'
                                            'Give a direct answer with your own reasoning.'
                                            'Do not create your own tools'
                                            'You are an LLM and my virtual assistant.'},

            #the * means take every element from self.message_history and put each one into this new list
            *reversed(self.message_history)
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



