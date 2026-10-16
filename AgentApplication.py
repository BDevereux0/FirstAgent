from ollama import ChatResponse

from agents.ConversationAgent import ConversationAgent
from agents.RouterAgent import RouterAgent
from agents.ToolAgent import ToolAgent
from tools.CompleteToolList import CompleteToolList
from utils.agent_response_parser import response_parser


class AgentApplication:

    #the router_agent is a dependency. This is dependency injection.
    def __init__(self, tool_agent ,router_agent, conversation_agent) :
        self.tool_agent = tool_agent
        self.router_agent = router_agent
        self.conversation_agent = conversation_agent

    #main section of the app. Coordinate's app logic, not contain it all.
    def run(self):
        user_input = ''
        while user_input != 'n':
            user_input = input("Enter message or enter 'n' to stop: ")
            self.router_call(user_input)

    def router_call(self, user_message: str):
        router_response: ChatResponse = self.router_agent.call_model(user_message)
        returned_router_response = response_parser(router_response)
        print(returned_router_response)

        if returned_router_response.get("tool") is None:
            self.conversation_call(user_message)
        else:
            self.tool_call(user_message)

    def conversation_call(self, user_message):
        conversation_response: ChatResponse = self.conversation_agent.call_model(user_message)
        print(conversation_response.message)
        print("***")
        print("conversation")

    def tool_call(self, user_message):
        tool_response: ChatResponse = self.tool_agent.call_model(user_message)
        print(tool_response.message)
        print("***")
        print("tool")
        tools = CompleteToolList()

        for tool in tool_response.message.tool_calls:
            # := is the walrus operator it does:
            # 1. Assigns a value (in this case to function_to_call
            # 2. Evaluates the value of the if statement
            if function_to_call := tools.available_functions.get(tool.function.name):
                output = function_to_call(**tool.function.arguments)
                print(output)
            else:
                output = 'Function not found'

        print("fk me running")

