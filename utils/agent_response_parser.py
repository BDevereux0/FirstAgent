import json

from ollama import ChatResponse


def response_parser(response: ChatResponse) -> dict:
        return json.loads(response.message.content)