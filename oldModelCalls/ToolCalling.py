from ollama import chat
from ollama import ChatResponse
from pydantic import FilePath


# Two ways to add tools, define the function as below or the dictionary labeled "add_two_numbers_tool
def add_two_numbers(a: int, b: int) -> int:
    """
    Add two numbers

    Args:
        a (int): The first number
        b (int): The second number

    Returns:
        int: The sum of the two numbers
    """

    return int(a) + int(b)

add_two_numbers_tool = {
    'type': 'function',
    'function':{
        'name': 'add_two_numbers',
        'description': 'Add two numbers',
        'parameters': {
            'type': 'object',
            'required': ['a','b'],
            'properties': {
                'a': {'type': 'integer', 'description': 'The first number'},
                'b': {'type': 'integer', 'description': 'The second number'}
            },
        },
    },
}

def read_file(filename):
    """
    Reads a file

    Args:
        a (str): The filename

    Returns:
        file contents
    """

def subtract_two_numbers(a: int, b:int)->int:
    """
    Subtract two numbers

    Args:
        a (int): The first number
        b (int): The second number

    Returns:
        int: The difference between two numbers
    """
    return int(a) - int(b)


messages = [
    {'role': 'system',
             'content': 'If no tool is present, answer with inference'},
    {'role': 'user',
             'content':
             'what is 2+2?'
                 'What is the closest planet to the sun?'

             }]

print('Prompt', messages[0]['content'])

available_functions = {
    'add_two_numbers': add_two_numbers,
    'add_two numbers_tool': add_two_numbers_tool,
    'subtract_two_numbers': subtract_two_numbers,
}

response: ChatResponse = chat(
    'llama3.1:8b',
    messages=messages,
    tools=[add_two_numbers_tool, subtract_two_numbers]
)

if response.message.tool_calls:
    for tool_call in response.message.tool_calls:

            function_name = tool_call.function.name
            arguments = tool_call.function.arguments

            print("Function requested:", function_name)
            print("Arguments requested:", arguments)

            function_to_call = available_functions[function_name]
            #** means unpack a dictionary into name keyword arguments
            result = function_to_call(**arguments)
            print(result)
else:
    print(response.message.content)






