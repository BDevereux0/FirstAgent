from modelCommunication.AgentCall import AgentCall
from routerAgent.RouterAgent import RouterAgent
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

router_agent = RouterAgent()

user_menu_input = ''

while user_menu_input.lower() != 'n':
    print("Enter a message for the router")
    router_input_message: str = input()
    router_agent.build_message(router_input_message)
    print(router_agent.message_to_router)

    router_response = router_agent.call_router_agent()
    print("Stop reason:", router_response.done_reason)
    print("Output tokens:", router_response.eval_count)
    print("Response:", repr(router_response.message.content))
    print(router_response.message)
    print(router_response.message.content)

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
            try:
                result = function_to_call(**arguments)
                print(result)
            except TypeError as e:
                print(f"Error: {e}")
            print(response.message.tool_calls)
            print(response.message.content)
    else:
        print(response.message.content)
    print("Another message?")
    user_menu_input = input()


