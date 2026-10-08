from tools.FileTools import find_file


class CompleteToolList:
    def __init__(self):
        #don't invoke the function, using (), just do the name.
        self.tools = [find_file]
        self.tool_list = {'find file': 'Searches for a file',
                          }
