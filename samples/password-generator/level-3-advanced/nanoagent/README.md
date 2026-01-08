# Nanoagent Level 3: Multi-Agent Orchestration

This advanced nanoagent demonstrates multi-agent collaboration with structured handoffs.

## What This Demonstrates

- **Multi-Agent Architecture**: Specialized agents with distinct roles
- **Agent Handoffs**: Structured message passing between agents
- **Shared Context**: Common state passed through the pipeline
- **Orchestration Pattern**: Coordinator manages the workflow

## Architecture

```
                    ┌──────────────┐
                    │ Orchestrator │
                    └──────┬───────┘
                           │
         ┌─────────────────┼─────────────────┐
         ▼                 ▼                 ▼
   ┌──────────┐     ┌─────────────┐    ┌──────────┐
   │ Planner  │────▶│ Implementer │───▶│  Tester  │
   │  Agent   │     │    Agent    │    │  Agent   │
   └──────────┘     └─────────────┘    └──────────┘
         │                 │                 │
         └─────────────────┴─────────────────┘
                           │
                    ┌──────▼──────┐
                    │   Shared    │
                    │   Context   │
                    └─────────────┘
```

## Execution Flow

```
1. User: "Generate a secure banking password"
2. Orchestrator: Creates shared context
3. Planner: Analyzes requirements → creates plan
4. Handoff: Planner → Implementer (with plan)
5. Implementer: Executes plan → generates password
6. Handoff: Implementer → Tester (with password)
7. Tester: Validates password → reports results
8. Orchestrator: Aggregates results → final response
```

## Setup

```bash
# Install dependencies with uv
uv sync

# Create a .env file (recommended)
# - edit .env next to orchestrator.py and set NANOAGENT_API_KEY / NANOAGENT_API_BASE
# - this repo ships a .env.template; keep real secrets out of source control
#
# Alternatively you can export environment variables:
#   OPENAI_API_KEY=...
#   OPENAI_API_BASE=...
```

## Usage

```bash
# Run with default prompt
uv run orchestrator.py

# Run with custom prompt
uv run orchestrator.py "Generate a 24-character password for server admin"

# Mock mode (no API key)
uv run orchestrator.py --mock "Generate a password"
```

## Code Structure

```
nanoagent/
├── orchestrator.py       # Main coordinator
├── agents/
│   ├── __init__.py       # Package exports
│   ├── base.py           # BaseAgent class, AgentContext, AgentMessage
│   ├── planner.py        # Planning agent
│   ├── implementer.py    # Implementation agent
│   └── tester.py         # Testing agent
├── tools/
│   ├── __init__.py       # Tool exports
│   └── shared_tools.py   # Tools used by agents
├── pyproject.toml        # uv configuration
└── README.md
```

## Key Concepts

### 1. Base Agent Class
```python
class BaseAgent(ABC):
    def __init__(self, role: AgentRole, mock: bool = False):
        self.role = role
        self.system_prompt = self._get_system_prompt()
    
    @abstractmethod
    async def process(self, context: AgentContext) -> AgentContext:
        pass
```

### 2. Shared Context
```python
@dataclass
class AgentContext:
    user_request: str
    plan: str | None = None
    implementation: dict | None = None
    test_results: dict | None = None
    history: list[AgentMessage] = field(default_factory=list)
```

### 3. Agent Messages (Handoffs)
```python
@dataclass
class AgentMessage:
    from_agent: AgentRole
    to_agent: AgentRole
    content: str
    metadata: dict = field(default_factory=dict)
```

### 4. Orchestration Pipeline
```python
async def run(self, user_request: str) -> str:
    context = AgentContext(user_request=user_request)
    context = await self.planner.process(context)      # Phase 1
    context = await self.implementer.process(context)  # Phase 2
    context = await self.tester.process(context)       # Phase 3
    return self._generate_final_response(context)
```

## Agent Roles

| Agent | Responsibility | Input | Output |
|-------|----------------|-------|--------|
| Planner | Analyze requirements | User request | Structured plan |
| Implementer | Execute plan | Plan | Generated password |
| Tester | Validate results | Password | Test results |

## Comparison with Previous Levels

| Aspect | Level 1 | Level 2 | Level 3 (This) |
|--------|---------|---------|----------------|
| Agents | 1 | 1 | 3 + Orchestrator |
| Communication | None | None | Message passing |
| State | None | Conversation | Shared context |
| Tools | None | Direct | Agent-owned |
| Workflow | Linear | Loop | Pipeline |

## Mock Mode Output

```
============================================================
NANOAGENT LEVEL 3: Multi-Agent Orchestration
============================================================

User Request: Generate a secure password

------------------------------------------------------------
ORCHESTRATION PIPELINE
------------------------------------------------------------

📋 PHASE 1: PLANNING
  [PLANNER] Analyzing user requirements...
  [PLANNER] Plan created. Handing off to Implementer.

🔧 PHASE 2: IMPLEMENTATION
  [IMPLEMENTER] Executing implementation plan...
  [IMPLEMENTER] Generating password with config: {...}
  [IMPLEMENTER] Password generated: Kj9#************
  [IMPLEMENTER] Handing off to Tester for validation.

🧪 PHASE 3: TESTING
  [TESTER] Validating generated password...
  [TESTER] Validation complete. Strength: very_strong, Verdict: PASS

------------------------------------------------------------
MESSAGE HISTORY (Agent Handoffs)
------------------------------------------------------------
  [planner → implementer]: Plan created. Handing off...
  [implementer → tester]: Password generated. Handing off...
  [tester → coordinator]: Validation complete. Verdict: PASS

============================================================
FINAL RESPONSE
============================================================
🔐 **Generated Password**: `Kj9#mPx2$vNq8&Lw`

**Validation Results**:
- Strength: VERY_STRONG
- Score: 5/5
- Verdict: ✅ PASS
```

## Extension Ideas

- Add retry logic when Tester returns FAIL
- Implement parallel agent execution
- Add memory/persistence between runs
- Implement agent-to-agent direct communication
- Add more specialized agents (Security Auditor, UX Writer, etc.)
