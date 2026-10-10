

class MessageBuilder:
    def __init__(self):
        self.messages = []

    def message(self):
        pass

    def create_system_prompt(self, system_message:str):
        self.messages.append({'role' : 'system',
         'content' : system_message
        })
        #allows method chaining, w/e that means.
        return self

    def create_conversation_prompt(self, conversation_user_prompt:str):
       self.messages.append({'role' : 'user',
          'content': conversation_user_prompt
       })
       return self

    #this will cause the caller to receive a list of the built prompts.
    def build(self):
        return self.messages.copy()