from huggingface_hub import HfApi
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")
print("Token:", token)

api = HfApi(token=token)
model_info = api.model_info("TinyLlama/TinyLlama-1.1B-Chat-v1.0")
print(model_info)
