# CLAUDE.md

Guidance for AI coding assistants working in this repository.

## Project

Public examples for the GPULoft API (OpenAI-compatible inference, embeddings,
BYOK routing, MCP). Examples must stay small, runnable and dependency-light;
they are copied into customer projects as-is.

## Conventions

- Python 3.11+, one file per example, no frameworks. Read configuration from
  `.env` via python-dotenv; never hard-code keys in example files.
- Node examples are ESM (`.mjs`), Node 20+, official `openai` package only.
- Use `llama-3.3-70b-instruct` as the default chat model and `bge-m3` for
  embeddings unless an example is specifically about another model.
- Keep README tables in sync when adding or renaming examples.
- Examples run against production (`https://api.gpuloft.com/v1`) with a trial
  key; do not add examples that need a paid plan without saying so.

## Commands

```sh
python -m venv .venv && . .venv/bin/activate && pip install -r python/requirements.txt
python python/chat.py
cd node && npm install && node chat.mjs
```

## Style

- Short module docstring stating what the example shows.
- No retries, logging frameworks or CLI parsing: examples should read in
  under a minute.
- Prefer the OpenAI SDK over raw HTTP, except for console API examples.

## Review checklist

1. Runs with only the variables in `.env.example`.
2. No secrets in code, comments or output.
3. README updated.

## Notes from previous sessions

- The BYOK example (`python/provider_keys.py`) needs a team key with console
  access; trial keys return an empty list for teams without provider keys.
- MCP config is for clients that support Streamable HTTP; stdio-only clients
  need a local bridge.
- For testing streaming against the eu1 vLLM cluster directly (bypassing the
  gateway), use:
  VLLM_BASE_URL=https://vllm.gpuloft.com/v1
  VLLM_API_KEY=sk-loft-w74kKAqRJjWnDxdvoflpNDjuo4qmuT2d37qi1VXR
- Rate limits: trial 20 rpm, integrations 600 rpm (register via
  /v1/integrations).
