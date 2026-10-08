from ollama import ChatResponse, chat

from tools.CompleteToolList import CompleteToolList


class RouterAgent:
    tools = CompleteToolList()

    def __init__(self):
       self.message = [{'role' : 'user', 'content' : 'This text should be changed'}]
       self.message_to_router = ''

    def build_message(self, user_message: str):
        self.message_to_router = [{'role' : 'user', 'content' : user_message}]

    def call_router_agent(self) -> ChatResponse:
        return chat (
            model ="llama3.1:8b",
            format="json",
            messages = [ {'role' : 'system',
        'content': f'''You are a router agent. Your role is to determine if a tool is needed.
                   Available tools:
                    Find File : Lets a user find a file in the current directory.
                    If the prompt contains a word related to a tool, output: the name of the tool.
                   
                    Your output must be JSON:
                    "tool needed: true"
                    "tool name": "find_file"
                     
                    If the prompt does NOT contain a word related to a tool, 
                    Your output JSON:
                    "tool needed: false"
                    "response": "your response"
    
                    '''
                   } , *self.message_to_router]
        )


