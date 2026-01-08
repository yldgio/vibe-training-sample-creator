# Nanoagent Level 2: Agent with Tool Calling

This intermediate agent demonstrates tool calling, instruction loading, and structured responses.

## What This Demonstrates

- **Tool Calling**: Agent decides when to use tools based on user request
- **Pydantic Schemas**: Type-safe tool definitions with automatic validation
- **Instruction Loading**: System prompts loaded from external files
- **Tool Loop**: Iterative tool calling until task completion

## Architecture

```
┌─────────┐     ┌─────────────┐     ┌─────────┐
│  User   │────▶│    Agent    │────▶│   LLM   │
│  Input  │     │             │◀────│         │
└─────────┘     └──────┬──────┘     └─────────┘
                       │
            ┌──────────┴──────────┐
            ▼                     ▼
      ┌──────────┐          ┌──────────┐
      │  Tools   │          │Instructions│
      │ Registry │          │  (system.md)│
      └──────────┘          └──────────┘
```

## Tool Calling Flow

```
1. User: "Generate a password"
2. Agent → LLM: [user message + tool schemas]
3. LLM → Agent: tool_call(generate_password, {length: 16, ...})
4. Agent: Executes generate_password() → "Kj9#mPx2$vNq8&Lw"
5. Agent → LLM: [tool result]
6. LLM → Agent: "Here's your password: Kj9#mPx2$vNq8&Lw"
7. Agent → User: Final response
```

## Setup

```bash
# Install dependencies with uv
uv sync

# Create a .env file (recommended)
# - edit .env next to agent.py and set NANOAGENT_API_KEY / NANOAGENT_API_BASE
# - this repo ships a template .env; keep real secrets out of source control
#
# Alternatively you can export environment variables:
#   OPENAI_API_KEY=...
#   OPENAI_API_BASE=...
```

## Usage

```bash
# Generate a password
uv run agent.py "Generate a secure 20-character password"

# Check password strength
uv run agent.py "Check if 'myP@ssw0rd!' is secure enough"

# Generate multiple passwords
uv run agent.py "Give me 5 password options to choose from"

# Mock mode (no API key)
uv run agent.py --mock "Generate a password"
```

## Code Structure

| File | Purpose |
|------|---------|
| `agent.py` | Main agent with tool calling loop |
| `tools/password_tools.py` | Tool definitions with Pydantic schemas |
| `tools/__init__.py` | Tool registry exports |
| `instructions/system.md` | System instructions (loaded at runtime) |

## Key Concepts

### 1. Pydantic Tool Schemas
```python
class GeneratePasswordInput(BaseModel):
    length: int = Field(default=16, ge=8, le=128)
    include_uppercase: bool = Field(default=True)
    # ... automatic JSON schema generation
```

### 2. Tool Registry
```python
TOOLS = {
    "generate_password": {
        "function": generate_password,
        "schema": GeneratePasswordInput,
        "description": "Generate a secure password"
    }
}
```

### 3. Tool Calling Loop
```python
while True:
    response = await call_llm_with_tools(messages, tools)
    if not response.tool_calls:
        break  # Final response
    # Execute tools, add results to messages
```

### 4. Instruction Loading
```python
system_prompt = Path("instructions/system.md").read_text()
messages = [{"role": "system", "content": system_prompt}, ...]
```

## Available Tools

| Tool | Description |
|------|-------------|
| `generate_password` | Generate a single secure password |
| `check_password_strength` | Analyze password and get recommendations |
| `generate_multiple_passwords` | Generate multiple passwords at once |

## Differences from Level 1

| Aspect | Level 1 | Level 2 (This) |
|--------|---------|----------------|
| Tools | None | 3 password tools |
| Instructions | Hardcoded | External file |
| LLM Calls | Single | Multiple (loop) |
| Validation | None | Pydantic schemas |

## Next Steps

See `level-3-advanced/nanoagent/` for multi-agent orchestration with handoffs.
