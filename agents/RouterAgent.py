from ollama import ChatResponse, chat

from modelCommunication.AgentCall import AgentCall
from modelCommunication.MessageBuilder import MessageBuilder
from tools.CompleteToolList import CompleteToolList


class RouterAgent:

    def __init__(self, agent_call: AgentCall):
        self.agent_call = agent_call

    def call_model(self, user_messages):
        builder = MessageBuilder()
        tools = CompleteToolList()
        message = builder.create_system_prompt(f"""
        You are a tool-routing agent.

        Your task is to determine whether the user's request
        requires one of the available tools.

        Available tools:
        {tools.tool_description}

        Rules:
        1. Select a tool only when the user requests an action
            that the tool can perform.
        2. If no tool is appropriate, return null.
        3. Never invent tool names.
        4. Return only valid JSON. No explanations.

        Output format:
        {{
        "tool": "find_file" | null,
        "content": "original user request"
        }} 
        """).create_conversation_prompt(user_messages).build()

        return self.agent_call.router_call_agent(message)


#  {tools.tool_list} is an example of adding a variable into a string. notice the f""" text {var} text """
