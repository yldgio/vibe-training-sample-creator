"""
Nanoagent Level 3: Multi-Agent Orchestrator

This orchestrator coordinates multiple specialized agents:
- Planner: Analyzes requirements and creates plans
- Implementer: Executes plans and generates passwords
- Tester: Validates results and reports quality

Usage:
    uv run orchestrator.py "Generate a very secure password for banking"
    uv run orchestrator.py --mock "Generate a password"
"""

import argparse
import asyncio

from agents import (
    AgentContext,
    PlannerAgent,
    ImplementerAgent,
    TesterAgent,
)


class Orchestrator:
    """
    Coordinates the multi-agent workflow.
    
    The orchestrator:
    1. Initializes all agents
    2. Manages the execution pipeline
    3. Handles handoffs between agents
    4. Aggregates final results
    """
    
    def __init__(self, mock: bool = False):
        self.mock = mock
        self.planner = PlannerAgent(mock=mock)
        self.implementer = ImplementerAgent(mock=mock)
        self.tester = TesterAgent(mock=mock)
    
    async def run(self, user_request: str) -> str:
        """
        Run the complete multi-agent workflow.
        
        Pipeline: User → Planner → Implementer → Tester → Response
        """
        print(f"\n{'='*60}")
        print("NANOAGENT LEVEL 3: Multi-Agent Orchestration")
        print(f"{'='*60}")
        print(f"\nUser Request: {user_request}")
        print(f"\n{'-'*60}")
        print("ORCHESTRATION PIPELINE")
        print(f"{'-'*60}\n")
        
        # Initialize context
        context = AgentContext(user_request=user_request)
        
        # Phase 1: Planning
        print("📋 PHASE 1: PLANNING")
        context = await self.planner.process(context)
        print()
        
        # Phase 2: Implementation
        print("🔧 PHASE 2: IMPLEMENTATION")
        context = await self.implementer.process(context)
        print()
        
        # Phase 3: Testing
        print("🧪 PHASE 3: TESTING")
        context = await self.tester.process(context)
        print()
        
        # Generate final response
        final_response = self._generate_final_response(context)
        context.final_response = final_response
        
        # Print message history
        print(f"{'-'*60}")
        print("MESSAGE HISTORY (Agent Handoffs)")
        print(f"{'-'*60}")
        for msg in context.history:
            print(f"  {msg}")
        print()
        
        # Print final response
        print(f"{'='*60}")
        print("FINAL RESPONSE")
        print(f"{'='*60}")
        print(final_response)
        print(f"\n{'='*60}\n")
        
        return final_response
    
    def _generate_final_response(self, context: AgentContext) -> str:
        """Generate the final user-facing response."""
        if not context.implementation or not context.test_results:
            return "Failed to generate password. Please try again."
        
        password = context.implementation["password"]
        strength = context.test_results["strength"]
        verdict = context.test_results["verdict"]
        
        response = f"""
🔐 **Generated Password**: `{password}`

**Validation Results**:
- Strength: {strength['strength'].upper()}
- Score: {strength['score']}
- Verdict: {'✅ ' + verdict if verdict == 'PASS' else '❌ ' + verdict}

**Security Checks**:
- Length ({len(password)} chars): {'✓' if strength['checks']['length_ok'] else '✗'}
- Uppercase: {'✓' if strength['checks']['has_uppercase'] else '✗'}
- Lowercase: {'✓' if strength['checks']['has_lowercase'] else '✗'}
- Numbers: {'✓' if strength['checks']['has_numbers'] else '✗'}
- Symbols: {'✓' if strength['checks']['has_symbols'] else '✗'}
"""
        
        if context.test_results.get("recommendations"):
            response += "\n**Recommendations**:\n"
            for rec in context.test_results["recommendations"]:
                response += f"- {rec}\n"
        
        return response.strip()


async def main_async(user_input: str, mock: bool = False) -> None:
    """Async entry point."""
    orchestrator = Orchestrator(mock=mock)
    await orchestrator.run(user_input)


def main():
    """Entry point for the orchestrator."""
    parser = argparse.ArgumentParser(
        description="Level 3 Nanoagent: Multi-agent orchestration"
    )
    parser.add_argument(
        "prompt",
        nargs="?",
        default="Generate a highly secure password for my banking application",
        help="The request to send to the multi-agent system"
    )
    parser.add_argument(
        "--mock",
        action="store_true",
        help="Run in mock mode without calling the LLM API"
    )
    
    args = parser.parse_args()
    
    asyncio.run(main_async(args.prompt, mock=args.mock))


if __name__ == "__main__":
    main()
