# GPULoft examples

Examples for the [GPULoft](https://gpuloft.com) API: OpenAI-compatible inference for open-weight models on dedicated H100/H200 capacity, with bring-your-own-key routing.

- Docs: https://docs.gpuloft.com
- API base URL: `https://api.gpuloft.com/v1`
- Status: https://status.gpuloft.com

## Setup

```sh
cp .env.example .env   # then set GPULOFT_API_KEY
```

Get a trial key (20 requests/minute, 7 days):

```sh
curl -X POST https://api.gpuloft.com/v1/trial-keys \
  -H "Content-Type: application/json" -d '{"project": "my-app"}'
```

## Examples

| Path | What it shows |
|---|---|
| `python/chat.py` | Chat completions with the OpenAI Python SDK |
| `python/embeddings.py` | Embeddings with `bge-m3` |
| `python/provider_keys.py` | Listing BYOK provider keys through the console API |
| `python/oauth_client_credentials.py` | OAuth client credentials (with dynamic client registration) instead of an API key |
| `python/a2a_assistant.py` | Asking the account assistant a question over A2A |
| `node/chat.mjs` | Streaming chat with the OpenAI Node SDK |
| `mcp/mcp.json` | Connecting an MCP client to `mcp.gpuloft.com` |

## Models

`llama-3.3-70b-instruct`, `qwen2.5-72b-instruct`, `mistral-small-24b-instruct`, `deepseek-r1-distill-llama-70b`, `bge-m3`. See the [docs](https://docs.gpuloft.com) for context lengths and pricing.

## OAuth and A2A

API keys and OAuth access tokens are interchangeable. The authorization server is `https://console.gpuloft.com`
(discovery at `/.well-known/openid-configuration`); MCP clients that support OAuth find it on their own.
The account assistant speaks A2A; its agent card is at `https://mcp.gpuloft.com/.well-known/agent-card.json`.

## Integrations

Tools and agents calling the API on behalf of users can register an integration for a higher rate limit: `POST https://api.gpuloft.com/v1/integrations` with `{"name": "...", "purpose": "..."}`.

## License

MIT
