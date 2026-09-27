"""Embeddings with bge-m3."""
import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(base_url=os.environ["GPULOFT_BASE_URL"], api_key=os.environ["GPULOFT_API_KEY"])

out = client.embeddings.create(model="bge-m3", input=["GPUs are fast", "so are TPUs"])
print(len(out.data), "vectors of", len(out.data[0].embedding), "dimensions")
