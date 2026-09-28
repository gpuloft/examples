"""Authenticate with OAuth client credentials instead of an API key.

Registers a client on first run (dynamic client registration) and prints the
credentials to put in .env, then gets an access token and lists models.
"""
import os

import requests
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
ISSUER = "https://console.gpuloft.com"

client_id = os.environ.get("GPULOFT_CLIENT_ID")
client_secret = os.environ.get("GPULOFT_CLIENT_SECRET")
if not client_id:
    reg = requests.post(
        f"{ISSUER}/oauth/register",
        json={"client_name": "gpuloft-examples", "grant_types": ["client_credentials"],
              "token_endpoint_auth_method": "client_secret_basic"},
        timeout=30,
    )
    reg.raise_for_status()
    client_id, client_secret = reg.json()["client_id"], reg.json()["client_secret"]
    print(f"Registered. Add to .env:\nGPULOFT_CLIENT_ID={client_id}\nGPULOFT_CLIENT_SECRET=<secret>\n")

token = requests.post(
    f"{ISSUER}/oauth/token",
    auth=(client_id, client_secret),
    data={"grant_type": "client_credentials", "scope": "models:read inference"},
    timeout=30,
)
token.raise_for_status()

client = OpenAI(base_url="https://api.gpuloft.com/v1", api_key=token.json()["access_token"])
for model in client.models.list():
    print(model.id)
