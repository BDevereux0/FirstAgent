from AgentApplication import AgentApplication
from agents.ConversationAgent import ConversationAgent
from agents.RouterAgent import RouterAgent
from modelCommunication.AgentCall import AgentCall

agent_call = AgentCall()
router = RouterAgent()
conversation_agent = ConversationAgent(agent_call)
app_start = AgentApplication(router, conversation_agent)
app_start.run()


