# Password Generator - Level 3 Advanced

This project uses multi-agent orchestration for planning, implementation, and testing.

## Project Overview

Build a secure password generator using vanilla HTML, CSS, and JavaScript with a structured multi-agent workflow.

## Tech Stack

- HTML5 for structure (semantic elements, accessibility)
- CSS3 for styling (custom properties, responsive design)
- Vanilla JavaScript (ES6+) for functionality

## Multi-Agent Workflow

This level uses four specialized agents:

1. **Planner** (`agents/planner.agent.md`) - Strategic planning and architecture
2. **Implementer** (`agents/implementer.agent.md`) - Code execution
3. **Tester** (`agents/tester.agent.md`) - Quality validation
4. **Coordinator** (`agents/coordinator.agent.md`) - Workflow orchestration

## Workflow

1. Start with Coordinator to initiate planning
2. Planner creates multi-stage implementation plan
3. Implementer executes plan phase by phase
4. Tester reviews and validates implementation
5. Iterate through feedback loops until approved

## Key Features

- Dynamic planning with self-review and refinement
- Risk assessment and mitigation strategies
- Structured handoffs between agents
- Quality gates at each stage
- Comprehensive testing and validation

## Instructions

Domain-specific instructions in `.github/instructions/`:

- `advanced-planning.instructions.md` - Planning methodology
- `agent-orchestration.instructions.md` - Collaboration patterns
- `security-best-practices.instructions.md` - Security requirements
- `performance-best-practices.instructions.md` - Performance optimization

## Prompts

Task-specific prompts in `.github/prompts/`:

- `dynamic-planning.prompt.md` - Multi-stage planning
- `architecture-decision.prompt.md` - Technical decisions
- `plan-execution.prompt.md` - Implementation workflow
- `review-feedback.prompt.md` - Code review patterns
- `risk-assessment.prompt.md` - Risk analysis
- `subagent-handover.prompt.md` - Handoff protocols
