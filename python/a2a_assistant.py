"""Ask the GPULoft account assistant a question over A2A (JSON-RPC)."""
import os
import uuid

import requests
from dotenv import load_dotenv

load_dotenv()
card = requests.get("https://mcp.gpuloft.com/.well-known/agent-card.json", timeout=30).json()
resp = requests.post(
    card["url"],
    headers={"Authorization": f"Bearer {os.environ['GPULOFT_API_KEY']}"},
    json={
        "jsonrpc": "2.0",
        "id": 1,
        "method": "message/send",
        "params": {"message": {"role": "user", "kind": "message", "messageId": str(uuid.uuid4()),
                               "parts": [{"kind": "text", "text": "How much have we spent this month?"}]}},
    },
    timeout=60,
)
resp.raise_for_status()
task = resp.json()["result"]
print(task["artifacts"][0]["parts"][0]["text"])
