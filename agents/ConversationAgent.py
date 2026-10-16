from modelCommunication.AgentCall import AgentCall
from modelCommunication.MessageBuilder import MessageBuilder


class ConversationAgent:
    def __init__(self, agent_call:AgentCall):
        self.agent_call = agent_call

    def call_model(self, user_messages:str):
        builder = MessageBuilder()
        messages = (builder.create_system_prompt(
            """you are a conversation agent.
            Always response using this JSON structure:
            {
                "Answer": "Model response"
            }""")
        .create_conversation_prompt(user_messages)
        .build())

        return self.agent_call.call_agent(messages)
