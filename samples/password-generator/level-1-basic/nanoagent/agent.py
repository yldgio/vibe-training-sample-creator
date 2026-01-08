"""
Nanoagent Level 1: Basic One-Shot Agent

This is the simplest possible agent implementation:
- Single prompt → single response
- No tools, no memory, no orchestration
- Demonstrates the core LLM interaction pattern

Usage:
    uv run agent.py "Generate a secure password with 16 characters"
    uv run agent.py --mock "Generate a password"  # No API key needed
"""

import argparse
import asyncio
import os
import sys
import warnings
from pathlib import Path

# Mock responses for demo mode (no API key required)
MOCK_RESPONSES = {
    "default": """Here's a secure 16-character password: `Kj9#mPx2$vNq8&Lw`

This password includes:
- Uppercase letters (K, P, N, L)
- Lowercase letters (j, m, x, v, q, w)  
- Numbers (9, 2, 8)
- Special characters (#, $, &)

The password has high entropy and would take centuries to crack with current technology."""
}


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
    """Resolve model + optional credentials from environment variables."""
    model = os.getenv("NANOAGENT_MODEL", "gpt-4.1-mini")
    api_key = os.getenv("NANOAGENT_API_KEY") or os.getenv("OPENAI_API_KEY")
    api_base = (
        os.getenv("NANOAGENT_API_BASE")
        or os.getenv("OPENAI_API_BASE")
        or os.getenv("OPENAI_BASE_URL")
    )
    return model, api_key, api_base


async def call_llm(prompt: str, mock: bool = False) -> str:
    """
    Call the LLM with a simple prompt and return the response.
    
    Args:
        prompt: The user's request
        mock: If True, return a mock response without calling the API
    
    Returns:
        The LLM's response text
    """
    if mock:
        print("\n[MOCK MODE] Would send to LLM:")
        print(f"  System: You are a helpful assistant that generates secure passwords.")
        print(f"  User: {prompt}")
        print()
        return MOCK_RESPONSES["default"]
    
    # Import litellm only when needed (allows mock mode without dependencies)
    try:
        from litellm import acompletion
    except ImportError:
        print("Error: litellm not installed. Run 'uv sync' or use --mock flag.")
        sys.exit(1)

    _load_dotenv_if_available()
    model, api_key, api_base = _get_llm_config()
    
    # Simple one-shot completion
    # litellm automatically uses OPENAI_API_KEY, ANTHROPIC_API_KEY, etc.
    request = {
        "model": model,  # Can be any litellm-supported model
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant that generates secure passwords. "
                           "Always explain the password composition and security features."
            },
            {
                "role": "user", 
                "content": prompt
            }
        ],
        "temperature": 0.7,
        "max_tokens": 500,
    }

    # Only pass credentials/base if explicitly configured. Otherwise LiteLLM can
    # pick them up from the provider-specific env vars.
    if api_key:
        request["api_key"] = api_key
    if api_base:
        request["api_base"] = api_base

    response = await acompletion(**request)
    
    return response.choices[0].message.content


async def run_agent(user_input: str, mock: bool = False) -> None:
    """
    Run the basic agent with the given input.
    
    This is the simplest agent pattern:
    1. Take user input
    2. Send to LLM
    3. Print response
    """
    print(f"\n{'='*60}")
    print("NANOAGENT LEVEL 1: Basic One-Shot Agent")
    print(f"{'='*60}")
    print(f"\nUser: {user_input}")
    print("\nAgent thinking...\n")
    
    response = await call_llm(user_input, mock=mock)
    
    print(f"Agent: {response}")
    print(f"\n{'='*60}\n")


def main():
    """Entry point for the agent."""
    parser = argparse.ArgumentParser(
        description="Level 1 Nanoagent: Basic one-shot password generator agent"
    )
    parser.add_argument(
        "prompt",
        nargs="?",
        default="Generate a secure password with 16 characters including uppercase, lowercase, numbers, and symbols",
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
