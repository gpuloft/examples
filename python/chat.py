"""Chat completion against GPULoft with the OpenAI SDK."""
import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(base_url=os.environ["GPULOFT_BASE_URL"], api_key=os.environ["GPULOFT_API_KEY"])

resp = client.chat.completions.create(
    model="llama-3.3-70b-instruct",
    messages=[{"role": "user", "content": "Explain KV-cache reuse in two sentences."}],
)
print(resp.choices[0].message.content)
