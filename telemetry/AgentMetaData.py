class AgentMetaData:
    def __init__(self):
        self.input_tokens = 0
        self.output_tokens = 0


    def set_input_tokens(self, i_tokens:int):
        self.input_tokens=i_tokens

    def set_output_tokens(self, o_tokens:int):
        self.output_tokens=o_tokens


