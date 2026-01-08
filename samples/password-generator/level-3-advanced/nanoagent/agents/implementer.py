"""
Implementer Agent

Executes the plan by generating passwords using available tools.
Hands off to the Tester agent.
"""

import json
from .base import BaseAgent, AgentRole, AgentContext, AgentMessage

# Import tools
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from tools.shared_tools import generate_password, GeneratePasswordInput


class ImplementerAgent(BaseAgent):
    """
    The Implementer agent executes plans and generates passwords.
    
    Responsibilities:
    - Parse the plan from Planner
    - Execute password generation with appropriate settings
    - Document the implementation
    - Hand off results to Tester
    """
    
    def __init__(self, mock: bool = False):
        super().__init__(AgentRole.IMPLEMENTER, mock)
    
    def _get_system_prompt(self) -> str:
        return """You are an Implementation Agent that executes password generation plans.

Given a plan, you will:
1. Extract the password configuration from the plan
2. Call the password generation tool
3. Document what was generated

Output format:
---
CONFIGURATION:
- Length: [number]
- Uppercase: [yes/no]
- Lowercase: [yes/no]
- Numbers: [yes/no]
- Symbols: [yes/no]

GENERATED PASSWORD: [password]

IMPLEMENTATION NOTES:
- [Any relevant notes]
---"""
    
    async def process(self, context: AgentContext) -> AgentContext:
        """Execute the plan and generate passwords."""
        self.log("Executing implementation plan...")
        
        # Parse plan to extract configuration (simplified)
        config = self._parse_plan(context.plan)
        
        # Generate password using tool
        self.log(f"Generating password with config: {config}")
        password = generate_password(GeneratePasswordInput(**config))
        
        implementation = {
            "config": config,
            "password": password,
            "notes": "Generated using cryptographically secure random"
        }
        context.implementation = implementation
        
        # Create handoff message
        message = AgentMessage(
            from_agent=self.role,
            to_agent=AgentRole.TESTER,
            content=f"Password generated. Handing off to tester for validation.",
            metadata={"implementation": implementation}
        )
        context.add_message(message)
        
        self.log(f"Password generated: {password[:4]}{'*' * (len(password)-4)}")
        self.log("Handing off to Tester for validation.")
        return context
    
    def _parse_plan(self, plan: str | None) -> dict:
        """Parse the plan to extract password configuration."""
        # Default configuration
        config = {
            "length": 16,
            "include_uppercase": True,
            "include_lowercase": True,
            "include_numbers": True,
            "include_symbols": True
        }
        
        if not plan:
            return config
        
        # Simple parsing (in production, use LLM for this)
        plan_lower = plan.lower()
        
        # Try to extract length
        import re
        length_match = re.search(r'length[:\s]+(\d+)', plan_lower)
        if length_match:
            config["length"] = int(length_match.group(1))
        
        return config
    
    def _get_mock_response(self) -> str:
        return "Implementation complete."
