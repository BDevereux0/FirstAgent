from modelCommunication.AgentCall import AgentCall
from modelCommunication.MessageBuilder import MessageBuilder


class ConversationAgent:
    def __init__(self, agent_call:AgentCall):
        self.agent_call = agent_call

    def call_model(self, user_messages:str):
        builder = MessageBuilder()
        messages = (builder.create_system_prompt("""
        you are a conversation agent.""")
        .create_conversation_prompt(user_messages)
        .build())

        print(messages)

        return self.agent_call.call_agent(messages)
