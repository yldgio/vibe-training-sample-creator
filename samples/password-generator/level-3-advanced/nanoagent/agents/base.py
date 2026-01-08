"""
Base Agent Class

Provides the foundation for all specialized agents in the multi-agent system.
Each agent has a role, system prompt, and can communicate via messages.
"""

import os
import warnings
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Any


# Keep the console output clean: LiteLLM/OpenAI response models can trigger noisy
# Pydantic v2 serializer warnings when internally converted to plain Python.
warnings.filterwarnings(
    "ignore",
    category=UserWarning,
    message=r"^Pydantic serializer warnings:.*",
)

# LiteLLM can emit a shutdown warning on some platforms when the event loop closes.
# This is noisy and not actionable for this sample.
warnings.filterwarnings(
    "ignore",
    category=RuntimeWarning,
    message=r"^coroutine 'close_litellm_async_clients' was never awaited.*",
)


class AgentRole(Enum):
    """Roles for specialized agents."""
    PLANNER = "planner"
    IMPLEMENTER = "implementer"
    TESTER = "tester"
    COORDINATOR = "coordinator"


@dataclass
class AgentMessage:
    """Message passed between agents."""
    from_agent: AgentRole
    to_agent: AgentRole
    content: str
    metadata: dict = field(default_factory=dict)
    
    def __str__(self) -> str:
        return f"[{self.from_agent.value} → {self.to_agent.value}]: {self.content[:100]}..."


@dataclass
class AgentContext:
    """Shared context passed through the agent pipeline."""
    user_request: str
    plan: str | None = None
    implementation: dict | None = None
    test_results: dict | None = None
    final_response: str | None = None
    history: list[AgentMessage] = field(default_factory=list)
    
    def add_message(self, message: AgentMessage) -> None:
        """Add a message to the history."""
        self.history.append(message)


class BaseAgent(ABC):
    """
    Abstract base class for all agents.
    
    Each agent has:
    - A role (planner, implementer, tester, coordinator)
    - A system prompt defining its behavior
    - An async process method for handling requests
    """
    
    def __init__(self, role: AgentRole, mock: bool = False):
        self.role = role
        self.mock = mock
        self.system_prompt = self._get_system_prompt()

    def _load_dotenv_if_available(self) -> None:
        """Load environment variables from a local .env (or .env.template) if available."""
        try:
            from dotenv import load_dotenv
        except Exception:
            return

        project_root = Path(__file__).resolve().parents[1]
        dotenv_path = project_root / ".env"
        dotenv_template_path = project_root / ".env.template"

        if dotenv_path.exists():
            load_dotenv(dotenv_path=dotenv_path)
        elif dotenv_template_path.exists():
            # Template is committed; it SHOULD contain placeholders only.
            load_dotenv(dotenv_path=dotenv_template_path)

    def _get_llm_config(self) -> tuple[str, str | None, str | None]:
        """Resolve model + optional credentials from environment variables."""
        model = os.getenv("NANOAGENT_MODEL", "gpt-4.1-mini")
        api_key = os.getenv("NANOAGENT_API_KEY") or os.getenv("OPENAI_API_KEY")
        api_base = (
            os.getenv("NANOAGENT_API_BASE")
            or os.getenv("OPENAI_API_BASE")
            or os.getenv("OPENAI_BASE_URL")
        )
        return model, api_key, api_base
    
    @abstractmethod
    def _get_system_prompt(self) -> str:
        """Return the system prompt for this agent."""
        pass
    
    @abstractmethod
    async def process(self, context: AgentContext) -> AgentContext:
        """
        Process the context and return updated context.
        
        Args:
            context: The shared context with user request and previous agent outputs
            
        Returns:
            Updated context with this agent's contribution
        """
        pass
    
    async def call_llm(self, messages: list[dict], tools: list[dict] | None = None) -> str:
        """
        Call the LLM with messages and optional tools.
        
        Returns the response content or tool call results.
        """
        if self.mock:
            return self._get_mock_response()
        
        try:
            from litellm import acompletion
        except ImportError:
            return self._get_mock_response()

        self._load_dotenv_if_available()
        model, api_key, api_base = self._get_llm_config()
        
        kwargs: dict[str, Any] = {
            "model": model,
            "messages": messages,
            "temperature": 0.7,
        }

        # Only pass credentials/base if explicitly configured. Otherwise LiteLLM can
        # pick them up from provider-specific env vars.
        if api_key:
            kwargs["api_key"] = api_key
        if api_base:
            kwargs["api_base"] = api_base

        if tools:
            kwargs["tools"] = tools
            kwargs["tool_choice"] = "auto"
        
        response = await acompletion(**kwargs)
        return response.choices[0].message.content
    
    @abstractmethod
    def _get_mock_response(self) -> str:
        """Return a mock response for demo mode."""
        pass
    
    def log(self, message: str) -> None:
        """Log a message with agent role prefix."""
        print(f"  [{self.role.value.upper()}] {message}")
