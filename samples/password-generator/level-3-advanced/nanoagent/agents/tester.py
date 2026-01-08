"""
Tester Agent

Validates the generated password against requirements and security standards.
Reports results back to the Coordinator.
"""

from .base import BaseAgent, AgentRole, AgentContext, AgentMessage

# Import tools
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from tools.shared_tools import check_password_strength, CheckPasswordStrengthInput


class TesterAgent(BaseAgent):
    """
    The Tester agent validates passwords and reports quality.
    
    Responsibilities:
    - Validate password against requirements
    - Check password strength
    - Identify any issues
    - Provide pass/fail verdict
    """
    
    def __init__(self, mock: bool = False):
        super().__init__(AgentRole.TESTER, mock)
    
    def _get_system_prompt(self) -> str:
        return """You are a Testing Agent that validates generated passwords.

Your job is to:
1. Check the password meets all requirements
2. Analyze password strength
3. Identify any security concerns
4. Provide a clear pass/fail verdict

Output format:
---
VALIDATION RESULTS:
- Length check: [PASS/FAIL]
- Character variety: [PASS/FAIL]
- Strength score: [score]

SECURITY ANALYSIS:
- [Analysis points]

VERDICT: [PASS/FAIL]
RECOMMENDATIONS: [If any]
---"""
    
    async def process(self, context: AgentContext) -> AgentContext:
        """Validate the generated password."""
        self.log("Validating generated password...")
        
        if not context.implementation:
            self.log("ERROR: No implementation to test!")
            context.test_results = {"verdict": "FAIL", "reason": "No password generated"}
            return context
        
        password = context.implementation["password"]
        
        # Check password strength using tool
        strength_result = check_password_strength(
            CheckPasswordStrengthInput(password=password)
        )
        
        # Determine verdict
        verdict = "PASS" if strength_result["strength"] in ["strong", "very_strong"] else "FAIL"
        
        test_results = {
            "password_tested": f"{password[:4]}{'*' * (len(password)-4)}",
            "strength": strength_result,
            "verdict": verdict,
            "recommendations": strength_result.get("recommendations", [])
        }
        context.test_results = test_results
        
        # Create handoff message
        message = AgentMessage(
            from_agent=self.role,
            to_agent=AgentRole.COORDINATOR,
            content=f"Validation complete. Verdict: {verdict}",
            metadata={"test_results": test_results}
        )
        context.add_message(message)
        
        self.log(f"Validation complete. Strength: {strength_result['strength']}, Verdict: {verdict}")
        return context
    
    def _get_mock_response(self) -> str:
        return "Validation complete."
