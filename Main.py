from AgentApplication import AgentApplication
from agents.ConversationAgent import ConversationAgent
from agents.RouterAgent import RouterAgent
from agents.ToolAgent import ToolAgent
from modelCommunication.AgentCall import AgentCall

agent_call = AgentCall()
router_agent = RouterAgent(agent_call)
tool_agent = ToolAgent(agent_call)
conversation_agent = ConversationAgent(agent_call)
app_start = AgentApplication(tool_agent, router_agent, conversation_agent)
app_start.run()


