# Level 3: Advanced - Multi-Agent Orchestration

This level showcases advanced prompting patterns for building a coordinated **multi-agent** workflow that plans, implements, and validates a secure password generator web app.

## Concept: Multi-Agent Collaboration

Instead of a single agent doing all the work, we orchestrate multiple specialized agents:

- **Planner Agent**: Strategy and architecture (WHAT and WHY)
- **Implementer Agent**: Execution and coding (HOW)
- **Tester Agent**: Validation and quality assurance (HOW WELL)
- **Coordinator Agent**: Orchestration and handoffs

## The Task

Create a secure password generator web app using a structured, multi-agent workflow with planning, execution, and validation phases.

## Folder Structure

```text
level-3-advanced/
├── .github/
│   ├── copilot-instructions.md           # Project overview
│   ├── agents/                           # Specialized agents
│   │   ├── coordinator.agent.md
│   │   ├── implementer.agent.md
│   │   ├── planner.agent.md
│   │   └── tester.agent.md
│   ├── instructions/                     # Domain instructions
│   │   ├── advanced-planning.instructions.md
│   │   ├── agent-orchestration.instructions.md
│   │   ├── performance-best-practices.instructions.md
│   │   └── security-best-practices.instructions.md
│   ├── prompts/                          # Task prompts
│   │   ├── architecture-decision.prompt.md
│   │   ├── dynamic-planning.prompt.md
│   │   ├── plan-execution.prompt.md
│   │   ├── review-feedback.prompt.md
│   │   ├── risk-assessment.prompt.md
│   │   └── subagent-handover.prompt.md
│   └── skills/                           # Specialized workflows with resources
│       ├── testing/
│       │   ├── SKILL.md
│       │   └── test-template.js
│       ├── security-validation/
│       │   ├── SKILL.md
│       │   └── security-checklist.md
│       └── deployment/
│           ├── SKILL.md
│           └── deploy-script.sh
└── README.md
```

## Agents

### Planner Agent
- Creates multi-stage implementation plans
- Makes architectural decisions
- Assesses risks and defines mitigations
- Hands off to Implementer

### Implementer Agent
- Executes plans phase by phase
- Follows domain instructions
- Documents deviations
- Hands off to Tester

### Tester Agent
- Reviews code against requirements
- Validates security and accessibility
- Provides structured feedback
- Approves or requests revisions

### Coordinator Agent
- Maintains global project view
- Manages handoffs between agents
- Resolves conflicts
- Drives project to completion

## Workflow

```text
                    ┌─────────────┐
                    │ Coordinator │
                    └──────┬──────┘
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼
        ┌─────────┐  ┌───────────┐  ┌────────┐
        │ Planner │──│Implementer│──│ Tester │
        └─────────┘  └───────────┘  └────────┘
              │            ▲            │
              │            │            │
              └────────────┴────────────┘
                    Feedback Loop
```

## Key Differences from Level 1 & 2

| Aspect | Level 1 | Level 2 | Level 3 (This) |
|--------|---------|---------|----------------|
| Agents | Single | Single | Multiple |
| Planning | Implicit | Minimal | Multi-stage |
| Workflow | Linear | Sequential | Iterative |
| Handoffs | None | None | Structured |
| Skills | None | Simple | With resources |
| Best For | Prototypes | Production | Complex projects |

## Agent Skills

Skills in Level 3 include additional resources (scripts, templates, examples) alongside instructions.

### Skills in This Level

| Skill | Resources | Purpose |
|-------|-----------|---------|
| `testing/` | `SKILL.md`, `test-template.js` | Comprehensive testing workflow with templates |
| `security-validation/` | `SKILL.md`, `security-checklist.md` | Security audit with checklist |
| `deployment/` | `SKILL.md`, `deploy-script.sh` | Deployment workflow with verification script |

### Progressive Disclosure

Skills use a three-level loading system:
1. **Discovery**: Copilot reads skill `name` and `description` from frontmatter
2. **Instructions**: When relevant, `SKILL.md` body is loaded into context
3. **Resources**: Additional files (scripts, templates) loaded only when referenced

### Skills vs Instructions

| Use Skills When | Use Instructions When |
|-----------------|----------------------|
| Need scripts or templates | Just need coding guidelines |
| Defining specialized workflows | Setting project standards |
| Want cross-platform portability | Applying rules to file types |
| Creating reusable capabilities | Defining language conventions |

## Learning Objectives

- Understand agent definition with tools and handoffs
- Learn multi-agent collaboration patterns
- See how to structure planning with self-review
- Practice risk assessment and mitigation
- Implement structured feedback loops

## Link utili (Copilot + prompt files)

- GitHub Copilot docs: https://docs.github.com/en/copilot
- GitHub Copilot (repository custom instructions): https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot
- VS Code Copilot Chat docs (prompt files / agent mode): https://code.visualstudio.com/docs/copilot/copilot-chat
- Esempi community (prompts/instructions):
      - https://github.com/github/awesome-copilot/tree/main/prompts
      - https://github.com/github/awesome-copilot/tree/main/instructions
- Agent Skills documentation:
      - https://docs.github.com/en/copilot/concepts/agents/about-agent-skills
      - https://code.visualstudio.com/docs/copilot/customization/agent-skills
      - https://agentskills.io (open standard)
- Esempi skills:
      - https://github.com/anthropics/skills
      - https://github.com/github/awesome-copilot

### Mini-cheatsheet: frontmatter (YAML)

**Prompt** (`.github/prompts/*.prompt.md`)

```yaml
---
description: "Cosa fa questo prompt"
mode: "agent" # oppure: "chat"
tools: ["editFiles", "runInTerminal"] # opzionale
---
```

**Instructions** (`.github/instructions/*.instructions.md`)

```yaml
---
description: "Regole riusabili (brevi)"
applyTo: "**/*.js"
---
```

**Agent** (`.github/agents/*.agent.md`)

```yaml
---
description: "Ruolo dell’agente"
tools: ["codebase", "editFiles"]
---
```

**Skill** (.github/skills/{skill-name}/SKILL.md)

```yaml
---
name: skill-name-lowercase-hyphens
description: "What the skill does and when Copilot should use it"
license: MIT  # optional
---

# Instructions
Step-by-step instructions, examples, and guidelines.

## Resources
Include scripts, templates, or examples in the same folder.
```
