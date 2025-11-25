# Level 3: Advanced - Planning-Focused Agent Workflow

This level focuses on **advanced planning techniques** and **agent orchestration** for building the password generator.

While Level 2 emphasized predictable output through domain instructions, Level 3 demonstrates:

- **Multi-stage planning** with explicit revision and refinement loops
- **Strategic thinking** about architecture, risks, and trade-offs
- **Agent orchestration** with clear handover protocols between planner, implementer, and reviewer
- **Meta-cognitive processes** (planning how to plan, reviewing plans, adapting strategies)

This level teaches how to structure complex agent workflows where planning is the primary focus.

## Key Concepts

### Planning as a First-Class Activity

Rather than jumping into implementation, Level 3 treats planning as:

- A multi-turn process with drafting and revision
- An opportunity to anticipate issues before coding
- A way to decompose complex problems systematically
- A communication protocol between different agent roles

### Agent Roles and Handover

Work is divided between specialized agent personas:

- **Planner Agent**: Creates and refines implementation strategies
- **Implementer Agent**: Executes plans with domain expertise
- **Reviewer Agent**: Validates outputs against requirements and standards

Each agent has clear responsibilities, inputs, and outputs, with explicit handover protocols.

### Dynamic Adaptation

Plans are not static - they evolve through:

- Self-review and critique
- Feedback loops between agents
- Identification of risks and mitigation strategies
- Continuous refinement based on new insights

## Components

### Planning Prompts (`.github/prompts/`)

- `dynamic-planning.prompt.md`: Create and refine multi-stage implementation plans
- `architecture-decision.prompt.md`: Reason about technical decisions and trade-offs  
- `risk-assessment.prompt.md`: Identify and mitigate potential issues early

### Orchestration Prompts (`.github/prompts/`)

- `subagent-handover.prompt.md`: Define collaboration protocols between agent personas
- `plan-execution.prompt.md`: Execute plans with checkpoints and validation
- `review-feedback.prompt.md`: Provide structured feedback for plan/code improvements

### Instructions (`.github/instructions/`)

- `advanced-planning.instructions.md`: Multi-stage planning methodology
- `agent-orchestration.instructions.md`: Agent role definitions and collaboration patterns

### Orchestration Guide

- `copilot-instructions.md`: Complete workflow for orchestrating planning-focused development
