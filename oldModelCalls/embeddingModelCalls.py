from importlib.resources import read_text

from sentence_transformers import SentenceTransformer, util
from pathlib import Path
from ollama import chat
from ollama import ChatResponse


model_path = "ibm-granite/granite-embedding-small-english-r2"

file = Path("/home/brandon-devereux/programming/mentorProjects/NoteCapsule/docs/PRD.md")

text = file.read_text()

model = SentenceTransformer(model_path)

input_queries = [
    "Are you a meat popsicle?"
]

input_query2 = [
    "MVP includes the core Discord-to-email"
]

input_passages = [
    text ]

query_embeddings = model.encode(input_queries)
passage_embeddings = model.encode(input_passages)



query2_embedding = model.encode(input_query2)

print(util.cos_sim(query_embeddings, passage_embeddings))
print(util.cos_sim(query2_embedding, passage_embeddings))
