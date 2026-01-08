"""
Planner Agent

Analyzes user requirements and creates a structured plan for password generation.
Hands off to the Implementer agent.
"""

from .base import BaseAgent, AgentRole, AgentContext, AgentMessage


class PlannerAgent(BaseAgent):
    """
    The Planner agent analyzes requirements and creates implementation plans.
    
    Responsibilities:
    - Parse user requirements
    - Identify password constraints
    - Create structured implementation plan
    - Assess security considerations
    """
    
    def __init__(self, mock: bool = False):
        super().__init__(AgentRole.PLANNER, mock)
    
    def _get_system_prompt(self) -> str:
        return """You are a Planning Agent specialized in analyzing password requirements.

Your job is to:
1. Analyze the user's password requirements
2. Identify constraints (length, character types, use case)
3. Create a structured plan for password generation
4. Consider security implications

Output your plan in this format:
---
REQUIREMENTS:
- [List extracted requirements]

CONSTRAINTS:
- Length: [number]
- Character types: [list]
- Use case: [description]

SECURITY CONSIDERATIONS:
- [List security notes]

IMPLEMENTATION PLAN:
1. [Step 1]
2. [Step 2]
...
---

Be concise but thorough."""
    
    async def process(self, context: AgentContext) -> AgentContext:
        """Analyze requirements and create a plan."""
        self.log("Analyzing user requirements...")
        
        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": f"Create a plan for: {context.user_request}"}
        ]
        
        plan = await self.call_llm(messages)
        context.plan = plan
        
        # Create handoff message
        message = AgentMessage(
            from_agent=self.role,
            to_agent=AgentRole.IMPLEMENTER,
            content=f"Plan created. Handing off to implementer.",
            metadata={"plan": plan}
        )
        context.add_message(message)
        
        self.log("Plan created. Handing off to Implementer.")
        return context
    
    def _get_mock_response(self) -> str:
        return """---
REQUIREMENTS:
- Generate a secure password
- Length: 16 characters
- Include all character types

CONSTRAINTS:
- Length: 16
- Character types: uppercase, lowercase, numbers, symbols
- Use case: General secure password

SECURITY CONSIDERATIONS:
- Use cryptographically secure random generation
- Ensure high entropy
- Avoid predictable patterns

IMPLEMENTATION PLAN:
1. Configure password options (length=16, all char types enabled)
2. Generate password using secure random
3. Verify password meets all constraints
4. Calculate and report strength score
---"""
