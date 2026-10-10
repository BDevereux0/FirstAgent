def build_message_history(self, role: str, user_content: str):
    self.message_history.append({
        'role': role,
        'content': user_content
    })


def build_agent_message_history(self, agent_content: str):
    self.model_message_history.append({
        agent_content
    })