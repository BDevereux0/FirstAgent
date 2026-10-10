from ollama import ChatResponse


class AgentApplication:

    #the router_agent is a dependency. This is dependency injection.
    def __init__(self, router_agent, conversation_agent):
        self.router_agent = router_agent
        self.conversation_agent = conversation_agent

    #main section of the app. Coordinate's app logic, not contain it all.
    def run(self):
        user_input = ''
        while user_input != 'n':
            user_input = input("Enter message or enter 'n' to stop: ")
            self.router_call(user_input)

    def router_call(self, user_message: str):
        response: ChatResponse = self.conversation_agent.call_model(user_message)
        print(response.message)
        #router agent call

        #if a tool is present send to tool agent

        #if no tool is present send to conversation agent


