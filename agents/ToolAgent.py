from modelCommunication.AgentCall import AgentCall
from modelCommunication.MessageBuilder import MessageBuilder
from tools.CompleteToolList import CompleteToolList


class ToolAgent:
    def __init__(self, agent_call: AgentCall):
        self.agent_call = agent_call

    def call_model(self, user_message):
        builder = MessageBuilder()
        tools = CompleteToolList().available_functions
        message = builder.create_conversation_prompt(f"""
        You are a tool model. Your job is to execute tools. List of tools: {tools}      
        
        
        """).create_conversation_prompt(user_message).build()

        return self.agent_call.call_agent(message)
