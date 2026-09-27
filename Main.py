from modelCommunication.AgentCall import AgentCall
from tools.CompleteToolList import CompleteToolList
from tools.FileTools import find_file
from telemetry.AgentMetaData import AgentMetaData

tool_listing = CompleteToolList()
telemetry = AgentMetaData()
call_agent = AgentCall(
    #Leave tools black, [], if no tool. Don't put "none"
     [{'role':'user',
        'content': 'why is the sky blue?'}],
    []
)

available_functions = {
   "find_file":find_file
}

user_menu_input = ''

while user_menu_input.lower() != 'n':
    call_agent.add_tools(tool_listing.tools)
    print("Enter a message")
    user_input_message:str = input()

    #this part calls the agent and i append the user's messages to keep context.
    call_agent.build_message_history("user", user_input_message)
    call_agent.construct_message()
    #sends the
    response = call_agent.callAgent()
    call_agent.build_agent_message_history(response.message.content)

    #saves input tokens
    telemetry.set_input_tokens(response.prompt_eval_count)
    print('input tokens: ' + str(telemetry.input_tokens))
    #saves output tokens
    telemetry.set_output_tokens(response.eval_count)
    print('output tokens: ' + str(telemetry.output_tokens))




    if response.message.tool_calls:
        for tool_call in response.message.tool_calls:
            function_name = tool_call.function.name
            arguments = tool_call.function.arguments

            function_to_call = available_functions[function_name]
            # ** means unpack a dictionary into name keyword arguments
            result = function_to_call(**arguments)
            print(response.message.tool_calls)
            print(result)
            print(response.message.content)
    else:
        print(response.message.content)
    print("Another message?")
    user_menu_input = input()


