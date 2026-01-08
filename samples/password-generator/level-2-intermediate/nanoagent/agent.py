"""
Nanoagent Level 2: Intermediate Agent with Tool Calling

This agent demonstrates:
- Tool definition with Pydantic schemas
- Tool calling loop (agent decides when to use tools)
- System instruction loading from file
- Structured tool responses

Usage:
    uv run agent.py "Generate a secure 20-character password"
    uv run agent.py --mock "Check if 'password123' is secure"
"""

import argparse
import asyncio
import json
import os
import sys
import warnings
from pathlib import Path

from tools import get_tool_schemas, execute_tool

# Load system instructions from file
INSTRUCTIONS_PATH = Path(__file__).parent / "instructions" / "system.md"


# Keep the console output clean: LiteLLM/OpenAI response models can trigger noisy
# Pydantic v2 serializer warnings when internally converted to plain Python.
warnings.filterwarnings(
    "ignore",
    category=UserWarning,
    message=r"^Pydantic serializer warnings:.*",
)


def _load_dotenv_if_available() -> None:
    """Load environment variables from a local .env if python-dotenv is available."""
    try:
        from dotenv import load_dotenv
    except Exception:
        return

    load_dotenv(dotenv_path=Path(__file__).parent / ".env")


def _get_llm_config() -> tuple[str, str | None, str | None]:
    """Resolve model + credentials from environment variables."""
    model = os.getenv("NANOAGENT_MODEL", "gpt-4.1-mini")
    api_key = os.getenv("NANOAGENT_API_KEY") or os.getenv("OPENAI_API_KEY")
    api_base = (
        os.getenv("NANOAGENT_API_BASE")
        or os.getenv("OPENAI_API_BASE")
        or os.getenv("OPENAI_BASE_URL")
    )
    return model, api_key, api_base


def load_system_instructions() -> str:
    """Load system instructions from markdown file."""
    if INSTRUCTIONS_PATH.exists():
        return INSTRUCTIONS_PATH.read_text()
    return "You are a helpful password generator assistant."


# Mock responses for demo mode
MOCK_TOOL_CALLS = {
    "generate": {
        "tool_calls": [{
            "id": "call_001",
            "type": "function",
            "function": {
                "name": "generate_password",
                "arguments": '{"length": 16, "include_uppercase": true, "include_lowercase": true, "include_numbers": true, "include_symbols": true}'
            }
        }],
        "final_response": """Here's your secure password: `{tool_result}`

**Password Analysis:**
- Length: 16 characters ✓
- Contains uppercase letters ✓
- Contains lowercase letters ✓
- Contains numbers ✓
- Contains special symbols ✓

This password has high entropy and would take centuries to crack with current brute-force methods."""
    },
    "check": {
        "tool_calls": [{
            "id": "call_002",
            "type": "function",
            "function": {
                "name": "check_password_strength",
                "arguments": '{"password": "password123"}'
            }
        }],
        "final_response": """**Password Strength Analysis:**

{tool_result}

**Recommendations:**
1. Add uppercase letters (A-Z)
2. Add special symbols (!@#$%^&*)
3. Increase length to at least 16 characters
4. Avoid common words like "password"

Would you like me to generate a stronger password for you?"""
    }
}


async def call_llm_with_tools(
    messages: list[dict],
    tools: list[dict],
    mock: bool = False,
    mock_scenario: str = "generate"
) -> object:
    """
    Call the LLM with tool definitions and handle tool calls.
    
    Returns the LLM response which may include tool_calls.
    """
    if mock:
        print("\n[MOCK MODE] Would send to LLM with tools:")
        print(f"  Messages: {len(messages)} messages")
        print(f"  Tools: {[t['function']['name'] for t in tools]}")
        return {"tool_calls": MOCK_TOOL_CALLS[mock_scenario]["tool_calls"]}
    
    try:
        from litellm import acompletion
    except ImportError:
        print("Error: litellm not installed. Run 'uv sync' or use --mock flag.")
        sys.exit(1)

    _load_dotenv_if_available()
    model, api_key, api_base = _get_llm_config()
    if not api_key or not api_base:
        print(
            "Error: missing LLM configuration. Set NANOAGENT_API_KEY and NANOAGENT_API_BASE "
            "(or OPENAI_API_KEY and OPENAI_API_BASE).\n"
            "Tip: create a .env file next to agent.py with these values."
        )
        sys.exit(2)
    
    response = await acompletion(
        model=model,  # Can be any litellm-supported model
        api_key=api_key,  # API key to your OpenAI-compatible endpoint
        api_base=api_base,  # API base URL for your endpoint
        messages=messages,
        tools=tools,
        tool_choice="auto",
        temperature=0.7,
    )
    
    return response.choices[0].message


async def run_agent(user_input: str, mock: bool = False) -> None:
    """
    Run the intermediate agent with tool calling capability.
    
    This implements a tool-calling loop:
    1. Send user message + tools to LLM
    2. If LLM returns tool_calls, execute them
    3. Send tool results back to LLM
    4. Repeat until LLM returns final response
    """
    print(f"\n{'='*60}")
    print("NANOAGENT LEVEL 2: Agent with Tool Calling")
    print(f"{'='*60}")
    print(f"\nUser: {user_input}")
    
    # Determine mock scenario based on input
    mock_scenario = "check" if "check" in user_input.lower() else "generate"
    
    # Load system instructions
    system_prompt = load_system_instructions()
    
    # Initialize conversation
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_input}
    ]
    
    # Get tool schemas
    tools = get_tool_schemas()
    
    print("\nAgent thinking (with tools available)...\n")
    
    # Tool calling loop
    max_iterations = 5
    for iteration in range(max_iterations):
        response = await call_llm_with_tools(messages, tools, mock=mock, mock_scenario=mock_scenario)
        
        # Check if LLM wants to call tools
        tool_calls = response.get("tool_calls") if isinstance(response, dict) else getattr(response, "tool_calls", None)
        
        if not tool_calls:
            # No tool calls - this is the final response
            final_content = response.get("content") if isinstance(response, dict) else response.content
            print(f"Agent: {final_content}")
            break
        
        # Execute each tool call
        print(f"[Agent is using tools...]")
        tool_results = []
        
        for tool_call in tool_calls:
            if isinstance(tool_call, dict):
                func = tool_call["function"]
                tool_name = func["name"]
                tool_args = json.loads(func["arguments"])
                tool_id = tool_call["id"]
            else:
                tool_name = tool_call.function.name
                tool_args = json.loads(tool_call.function.arguments)
                tool_id = tool_call.id
            
            print(f"  → Calling {tool_name}({tool_args})")
            result = execute_tool(tool_name, tool_args)
            print(f"  ← Result: {result[:100]}..." if len(str(result)) > 100 else f"  ← Result: {result}")
            
            tool_results.append({
                "tool_call_id": tool_id,
                "result": result
            })
        
        if mock:
            # In mock mode, show the final response with tool results
            final_response = MOCK_TOOL_CALLS[mock_scenario]["final_response"]
            final_response = final_response.format(tool_result=tool_results[0]["result"])
            print(f"\nAgent: {final_response}")
            break
        
        # Add assistant message with tool calls
        messages.append({
            "role": "assistant",
            "content": None,
            "tool_calls": tool_calls
        })
        
        # Add tool results
        for result in tool_results:
            messages.append({
                "role": "tool",
                "tool_call_id": result["tool_call_id"],
                "content": result["result"]
            })
    
    print(f"\n{'='*60}\n")


def main():
    """Entry point for the agent."""
    parser = argparse.ArgumentParser(
        description="Level 2 Nanoagent: Agent with tool calling capabilities"
    )
    parser.add_argument(
        "prompt",
        nargs="?",
        default="Generate a secure 16-character password for my email account",
        help="The prompt to send to the agent"
    )
    parser.add_argument(
        "--mock",
        action="store_true",
        help="Run in mock mode without calling the LLM API"
    )
    
    args = parser.parse_args()
    
    asyncio.run(run_agent(args.prompt, mock=args.mock))


if __name__ == "__main__":
    main()
