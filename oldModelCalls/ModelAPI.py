from ollama import chat
from ollama import ChatResponse

response: ChatResponse = chat(model='llama3.1:8b', messages=[
    {
        'role': 'user',
        'content': 'What is 2 + 2?'
    },
])
print(response['message']['content'])

#print(response.message.content)