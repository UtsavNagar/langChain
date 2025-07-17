from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv

load_dotenv()

model = SentenceTransformer('all-MiniLM-L6-v2')

sentences = [
    "Delhi is the capital of India.",
    "Mumbai is the financial capital of India.",
    "Chennai is known for its cultural heritage.",
    "Kolkata is a major port city in eastern India."
]

embeddings = model.encode(sentences)

print(str(embeddings))
