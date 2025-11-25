# Copilot Instructions: Level 3 Advanced Planning-Focused Workflow

This level demonstrates **advanced planning and agent orchestration** for building the password generator.

## Core Philosophy

Level 3 is fundamentally about **planning as a primary activity** rather than rushing to implementation:

- Plans are created, reviewed, and refined iteratively
- Multiple specialized agents collaborate with clear handover protocols
- Strategic thinking precedes tactical execution
- Quality emerges from systematic planning and validation

## Conceptual Progression

**Level 1 (Basic)**:

- Single one-shot prompt
- Immediate implementation
- No planning or structure

**Level 2 (Intermediate)**:

- Domain-specific instructions for predictability
- Task-specific prompts for repeatability
- Focus on consistent, standards-compliant output

**Level 3 (Advanced)**:

- Multi-stage planning with self-review
- Agent orchestration (Planner → Implementer → Reviewer)
- Strategic decision-making and risk assessment
- Continuous improvement through feedback loops

## The Planning-First Workflow

### Stage 1: Strategic Planning

**Goal**: Create robust implementation strategy before writing code

#### Prompt Sequence

1. **Dynamic Planning** (`dynamic-planning.prompt.md`)
   - Create PLAN_V1 (initial plan)
   - Perform PLAN_REVIEW (self-critique)
   - Produce PLAN_REFINED (improved plan)
   - Output: Complete implementation strategy with phases, checkpoints, success criteria

2. **Architecture Decisions** (`architecture-decision.prompt.md`)
   - Analyze options for code organization, state management, error handling, accessibility, CSS architecture
   - Evaluate trade-offs for each option
   - Make recommendations with clear rationale
   - Output: Decision records explaining key technical choices

3. **Risk Assessment** (`risk-assessment.prompt.md`)
   - Identify risks across security, accessibility, usability, reliability, maintainability
   - Rate impact and likelihood for each risk
   - Define mitigation strategies
   - Output: Prioritized risk matrix with mitigation roadmap

**Outcome of Stage 1**: Complete planning package ready for implementation

### Stage 2: Agent Orchestration Setup

**Goal**: Define how agents will collaborate

#### Prompt

4. **Multi-Agent Handover** (`subagent-handover.prompt.md`)
   - Define Planner, Implementer, Reviewer agent roles
   - Create handover protocols (what information passes between agents)
   - Design feedback loops for revisions
   - Output: Agent contracts and collaboration workflow

**Outcome of Stage 2**: Clear operating procedures for agent collaboration

### Stage 3: Systematic Execution

**Goal**: Implement plan with validation checkpoints

#### Prompt

5. **Plan Execution** (`plan-execution.prompt.md`)
   - Execute PLAN_REFINED phase by phase
   - Validate at each checkpoint
   - Document deviations and issues
   - Reference Level 2 domain instructions (CSS, JavaScript, Accessibility, Testability)
   - Output: Working implementation with execution report

**Outcome of Stage 3**: Implemented password generator following plan

### Stage 4: Quality Validation

**Goal**: Ensure implementation meets all requirements and standards

#### Prompt

6. **Review and Feedback** (`review-feedback.prompt.md`)
   - Validate against requirements, plan, and standards
   - Check all seven dimensions (Functional, Code Quality, Security, Accessibility, Performance, Maintainability, Standards)
   - Provide prioritized, actionable feedback
   - Output: Structured review with approval decision or revision requests

**Outcome of Stage 4**: Validated implementation or specific improvements needed

### Stage 5: Iteration (if needed)

**Goal**: Address feedback and improve quality

- Implementer reviews feedback
- Addresses Critical and High priority issues
- Re-tests and validates changes
- Resubmits for review
- Loop until approved

## Complete Workflow Example

### Scenario: Building Password Generator from Scratch

**User starts**: "Build a secure password generator web app"

#### Turn 1: Dynamic Planning

```
User → Planner Agent: "Create an implementation plan for a secure password generator"
Planner uses: dynamic-planning.prompt.md
Planner produces:
- PLAN_V1 (initial thoughts)
- PLAN_REVIEW (self-critique identifying 5 gaps and 3 risks)
- PLAN_REFINED (improved 5-phase plan with security/accessibility integrated)
```

#### Turn 2: Architecture Decisions

```
User → Planner Agent: "Make key architectural decisions for this project"
Planner uses: architecture-decision.prompt.md
Planner produces:
- Decision 1: Code Organization → Module Pattern (rationale: testability + single-file constraint)
- Decision 2: State Management → Explicit state object (rationale: debuggability)
- Decision 3: Error Handling → Throw + catch at handler level (rationale: clear error messages)
- Decision 4: Accessibility → Semantic HTML first (rationale: standards compliance)
- Decision 5: CSS → Custom properties + semantic classes (rationale: maintainability)
```

#### Turn 3: Risk Assessment

```
User → Planner Agent: "Assess risks for this implementation"
Planner uses: risk-assessment.prompt.md
Planner produces:
- 12 identified risks across 5 categories
- Priority matrix (3 Critical, 4 High, 3 Medium, 2 Low)
- Mitigation strategies for each
- Implementation roadmap (Phase 1: Critical risks, Phase 2: High priority, etc.)
```

#### Turn 4: Agent Orchestration Design

```
User → Meta Agent: "Define how Planner, Implementer, and Reviewer should collaborate"
Meta Agent uses: subagent-handover.prompt.md
Meta Agent produces:
- Planner role definition (responsibilities, inputs, outputs, quality criteria)
- Implementer role definition
- Reviewer role definition
- Handover protocols (4 handover types with templates)
- Workflow diagram and example scenario
```

#### Turn 5: Implementation

```
User → Implementer Agent: "Execute the refined plan"
Implementer has access to:
- PLAN_REFINED
- Architectural decisions
- Risk mitigations
- Level 2 domain instructions

Implementer uses: plan-execution.prompt.md
Implementer produces:
- Phase 1: HTML structure (validated)
- Phase 2: CSS styling (validated)
- Phase 3: Core logic (validated)
- Phase 4: Event handlers (validated)
- Phase 5: Testing and polish (validated)
- Execution report documenting process
```

#### Turn 6: Review

```
User → Reviewer Agent: "Review the implementation"
Reviewer has access to:
- Implementation code
- Original plan and requirements
- Level 2 standards

Reviewer uses: review-feedback.prompt.md
Reviewer produces:
- Overall assessment: "Requires Changes"
- 2 Critical issues (crypto API not used, missing aria-labels)
- 3 High priority issues (contrast too low, missing error handling, no keyboard trap management)
- 5 strengths recognized
- Specific recommendations for each issue
```

#### Turn 7: Revision

```
User → Implementer Agent: "Address reviewer feedback"
Implementer addresses:
- All Critical issues fixed (crypto API implemented, aria-labels added)
- All High priority issues fixed
- Re-tested and validated

Implementer resubmits with revision notes
```

#### Turn 8: Re-Review

```
User → Reviewer Agent: "Re-review the revised implementation"
Reviewer validates:
- All issues resolved
- Tests passing
- Standards met

Reviewer produces: "Approved - Ready for deployment"
```

## Key Differences from Level 2

| Aspect | Level 2 | Level 3 |
|--------|---------|---------|
| **Focus** | Predictable output through standards | Planning and orchestration |
| **Approach** | Task-specific prompts + domain instructions | Multi-stage planning + agent roles |
| **Iteration** | Minimal (get it right first time) | Expected (plan → review → refine) |
| **Agents** | Single agent with instructions | Multiple specialized agents |
| **Planning** | Implicit in prompts | Explicit, multi-stage, revisable |
| **Complexity** | Suitable for well-defined tasks | Suitable for complex, uncertain projects |

## When to Use Level 3

Use Level 3 planning-focused approach when:

- Requirements are complex or ambiguous
- Multiple concerns must be balanced (security, accessibility, performance, maintainability)
- Risk assessment is important
- Team collaboration needed (simulated by agent handovers)
- Learning architecture and planning is the goal (not just implementation)
- Quality requires iteration and refinement

Level 2 is better for:

- Well-defined, straightforward tasks
- When speed matters more than exploration
- When standards are clear and established
- Production code generation following known patterns

## Teaching Value

Level 3 teaches:

- **Strategic thinking**: Plan before coding
- **Risk awareness**: Anticipate problems early
- **Decision-making**: Analyze options and trade-offs
- **Collaboration**: How agents/people work together effectively
- **Quality processes**: Review, feedback, iteration
- **Meta-cognition**: Thinking about thinking (planning how to plan)

## Integration with Level 2

Level 3 **builds on** Level 2:

- Uses Level 2 domain instructions during implementation
- References Level 2 task prompts for implementation details
- Adds planning layer on top of Level 2's predictability

Example integration:

```
Level 3 Planning → Produces detailed plan
Level 3 Execution → Uses Level 2 prompts (create-ui-component, generate-styles, etc.)
                   → Follows Level 2 instructions (CSS standards, JS patterns, etc.)
Level 3 Review → Validates against Level 2 standards
```

## Getting Started

To use Level 3 workflow:

1. **Start with planning**: Run `dynamic-planning.prompt.md`
2. **Make decisions**: Run `architecture-decision.prompt.md`
3. **Assess risks**: Run `risk-assessment.prompt.md`
4. **Setup collaboration**: Run `subagent-handover.prompt.md` (optional, for learning)
5. **Execute systematically**: Run `plan-execution.prompt.md` with access to Level 2 resources
6. **Validate quality**: Run `review-feedback.prompt.md`
7. **Iterate if needed**: Address feedback and re-review

## Summary

Level 3 demonstrates that **planning is coding** - good code emerges from good planning. By treating planning as a first-class, multi-stage activity with explicit review and refinement, we create more robust, thoughtful implementations.

The agent orchestration model shows how to structure complex work through role separation, clear handovers, and feedback loops - patterns applicable to real-world team collaboration and AI agent coordination.
