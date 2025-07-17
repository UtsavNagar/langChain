from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

document = [
    "Sachin Tendulkar is known as the 'God of Cricket' and was the first player to score 100 international centuries.",
    "Virat Kohli became the fastest batsman to reach 8,000, 9,000, 10,000, and 11,000 ODI runs.",
    "Muttiah Muralitharan holds the record for the highest number of wickets in both Test and ODI cricket.",
    "Jacques Kallis is one of the best all-rounders, scoring over 10,000 runs and taking more than 250 wickets in both Tests and ODIs.",
    "MS Dhoni is famous for his calm captaincy and led India to victory in the 2011 ICC Cricket World Cup.",
    "Shane Warne is regarded as one of the greatest leg-spinners in cricket history with over 700 Test wickets."
]
query = "tell me about virat kohli"

model = SentenceTransformer('all-MiniLM-L6-v2')


embeddings = model.encode(document)
embedding = model.encode(query)
score = cosine_similarity([embedding],embeddings)[0]


index, score = sorted(list(enumerate(score)),key=lambda x:x[1])[-1]

print(document[index])