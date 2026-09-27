"""List the team's bring-your-own-key provider keys (console API)."""
import os

import requests
from dotenv import load_dotenv

load_dotenv()
resp = requests.get(
    "https://console.gpuloft.com/api/v1/provider-keys",
    headers={"Authorization": f"Bearer {os.environ['GPULOFT_API_KEY']}"},
    timeout=30,
)
resp.raise_for_status()
for key in resp.json()["data"]:
    print(key["name"], key["provider"], key["base_url"])
