# Nanoagent Level 1: Basic One-Shot Agent

This is the simplest possible agent implementation demonstrating a one-shot prompt/response pattern.

## What This Demonstrates

- **Single LLM call**: One prompt in, one response out
- **No tools**: Pure text generation
- **No memory**: Each call is independent
- **Provider-agnostic**: Uses litellm for any LLM backend

## Architecture

```
┌─────────┐     ┌─────────┐     ┌─────────┐
│  User   │────▶│  Agent  │────▶│   LLM   │
│  Input  │     │         │◀────│         │
└─────────┘     └────┬────┘     └─────────┘
                     │
                     ▼
               ┌─────────┐
               │ Response│
               └─────────┘
```

## Setup

```bash
# Install dependencies with uv
uv sync

# Create a .env file (recommended)
# - edit .env next to agent.py
#   - NANOAGENT_API_KEY (or OPENAI_API_KEY)
#   - NANOAGENT_API_BASE (or OPENAI_API_BASE) for OpenAI-compatible endpoints (e.g., Azure)
#
# Alternatively you can export environment variables:
#   OPENAI_API_KEY=...
#   OPENAI_API_BASE=...
```

## Usage

```bash
# Run with default prompt
uv run agent.py

# Run with custom prompt
uv run agent.py "Generate a 20-character password for a banking app"

# Run in mock mode (no API key required)
uv run agent.py --mock "Generate a password"
```

## Code Structure

| File | Purpose |
|------|---------|
| `agent.py` | Single-file agent implementation |
| `pyproject.toml` | uv package configuration |

## Key Concepts

### 1. Async Pattern
```python
async def call_llm(prompt: str) -> str:
    response = await acompletion(model="gpt-4o-mini", messages=[...])
    return response.choices[0].message.content
```

### 2. Mock Mode
The `--mock` flag allows running without API keys:
- Shows what would be sent to the LLM
- Returns predefined responses
- Perfect for demos and testing

### 3. Provider Agnostic
litellm abstracts the LLM provider:
```python
# Works with any of these:
model="gpt-4o-mini"           # OpenAI
model="claude-3-sonnet"       # Anthropic  
model="azure/gpt-4"           # Azure OpenAI
model="ollama/llama2"         # Local Ollama
```

## Limitations

This basic agent cannot:
- Remember previous conversations
- Use tools or call functions
- Make multiple LLM calls
- Handle complex multi-step tasks

These capabilities are added in Level 2 and Level 3.

## Next Steps

See `level-2-intermediate/nanoagent/` for an agent with tool calling capabilities.
