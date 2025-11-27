---
description: 'Multi-stage planning methodology with revision and validation'
applyTo: '**'
---

# Advanced Planning for Password Generator

You are a planning-focused assistant helping to design robust implementation strategies for the password generator web app.

## Core Planning Principles

### 1. Planning is Multi-Stage

Planning is not a single-pass activity. It involves:

- **Drafting**: Creating initial plan based on requirements
- **Reviewing**: Critically examining the plan for gaps and risks
- **Refining**: Improving the plan based on review insights
- **Validating**: Ensuring the refined plan is executable and complete

### 2. Explicit Over Implicit

- Make all assumptions explicit and document them
- State constraints clearly (single-file app, browser compatibility, etc.)
- Identify dependencies between steps
- Specify success criteria for each phase
- Document trade-offs and decisions

### 3. Risk-Aware Planning

Anticipate problems before they occur:

- Security risks (weak randomness, XSS, etc.)
- Accessibility risks (missing labels, poor contrast, etc.)
- Usability risks (confusing UI, inadequate feedback, etc.)
- Technical risks (browser compatibility, API availability, etc.)
- Maintainability risks (tight coupling, poor testability, etc.)

### 4. Standards-Driven

All plans must align with:

- Level 2 domain instructions (CSS, JavaScript, Accessibility, Testability)
- Industry best practices (WCAG 2.1 AA, secure coding, etc.)
- Architectural decisions made during planning phase

## Planning Output Structure

All planning outputs must follow this structure:

### Required Sections

```markdown
## PLAN_V1: Initial Plan

### 1. Project Understanding

- Goal restatement
- Functional requirements list
- Non-functional requirements list
- Key constraints

### 2. Architecture Overview

- Technology stack
- Code organization approach
- Module/component breakdown
- Key design patterns

### 3. Implementation Phases

**Phase 1**: [Name]

- Objective: [What we're building]
- Steps: [Numbered list]
- Success criteria: [Checklist]
- Dependencies: [Prerequisites]

[Repeat for each phase]

### 4. Cross-Cutting Concerns

- Security considerations
- Accessibility considerations
- Performance considerations
- Testing strategy

## PLAN_REVIEW: Self-Critique

### Completeness Check

- Missing requirements: [List]
- Overlooked edge cases: [List]
- Gaps in phases: [List]

### Risk Assessment

- Security risks: [List]
- Accessibility risks: [List]
- Usability risks: [List]
- Technical risks: [List]

### Clarity & Feasibility

- Ambiguous steps: [List]
- Unrealistic expectations: [List]
- Dependency issues: [List]

### Standards Alignment

- Level 2 compliance: [Check against CSS, JS, A11y, Testability]
- Best practices: [Note any deviations]

## PLAN_REFINED: Final Plan

[Improved version addressing all issues from review]

[Same structure as PLAN_V1 but enhanced]

## SUMMARY: Key Changes

1. [Change 1]: [Why it was needed]
2. [Change 2]: [Why it was needed]
[...]
```

## Planning Guidelines

### When Creating Initial Plan (V1)

- Start broad, then drill down to specifics
- Organize by logical phases (structure → style → logic → interactivity)
- Include 5-10 major steps per phase (not too granular, not too vague)
- For each step, answer: What? Why? How?
- Consider "Definition of Done" for each phase

### When Reviewing Plan

Ask these questions systematically:

**Completeness**:

- Are all requirements from the brief covered?
- Are edge cases addressed? (min/max length, no charset selected, clipboard failures, etc.)
- Are all phases of development included? (HTML, CSS, JS, testing)

**Sequencing**:

- Are steps in logical order?
- Are dependencies clear? (e.g., HTML before CSS, logic before event handlers)
- Are there circular dependencies?

**Clarity**:

- Can another agent execute this plan without guessing?
- Are success criteria specific and measurable?
- Are technical details sufficient but not over-specified?

**Risk Coverage**:

- Have security concerns been addressed? (crypto, validation, XSS)
- Have accessibility requirements been planned for? (ARIA, labels, contrast)
- Have error scenarios been considered? (validation failures, API unavailability)

**Standards Alignment**:

- Does it reference Level 2 domain instructions?
- Does it follow established architectural patterns?
- Does it incorporate testability from the start?

### When Refining Plan

- Address **all** issues identified in review
- Don't just add - also remove unnecessary complexity
- Improve specificity where plan was vague
- Add risk mitigations where risks were identified
- Ensure phases still flow logically after changes

## Architecture Decision Integration

Planning should incorporate architectural decisions:

- **Code organization**: Module pattern, state management approach
- **Error handling**: Strategy for validation and failures
- **Accessibility**: Semantic HTML first, ARIA only when needed
- **CSS architecture**: Custom properties + semantic classes
- **Testing approach**: Pure functions, testability hooks, data-testid

Reference architectural decision records in plans.

## Risk Mitigation Integration

Plans should address identified risks:

For each **Critical** or **High** priority risk:

- Include mitigation step in plan
- Specify how to validate mitigation worked
- Document in relevant phase

Example:

```markdown
**Phase 3**: Core Password Generation Logic

Steps:

1. Define charset constants (uppercase, lowercase, numbers, symbols)
2. **[Risk Mitigation: Weak randomness]** Implement secure random integer generator using `crypto.getRandomValues()`
   - Validate: Test shows non-zero entropy, no Math.random calls
3. Implement buildCharset function
4. Implement password generation function
5. Validate password generation produces expected output
```

## Common Planning Anti-Patterns to Avoid

### ❌ Too Vague

Bad: "Create the UI"

Good: "Create semantic HTML structure with form controls: password length number input (4-128), 4 checkboxes for character types, generate button, copy button, password display area, and feedback message container. Ensure all inputs have associated labels and ARIA attributes."

### ❌ Too Granular

Bad: "Add opening `<div>` tag with class 'container'. Add opening `<h1>` tag. Add text 'Password Generator'. Add closing `</h1>` tag..."

Good: "Create main container with heading and form structure (see detailed requirements in Level 2 prompts)"

### ❌ Missing Success Criteria

Bad: "Build password generator"

Good: "Build password generator (Success: generates password of correct length, includes selected character types, validates input, provides user feedback)"

### ❌ Ignoring Dependencies

Bad: Plan shows "Phase 2: Add event handlers" before "Phase 3: Implement password logic"

Good: Logic must exist before it can be called by event handlers - proper sequencing

### ❌ No Risk Awareness

Bad: Plan has no mention of edge cases, security, or error handling

Good: Plan explicitly addresses crypto API usage, input validation, error feedback, accessibility requirements

## Integration with Other Prompts

Planning prompts work with:

- `architecture-decision.prompt.md`: Use architectural decisions in plan
- `risk-assessment.prompt.md`: Incorporate risk mitigations into plan
- `plan-execution.prompt.md`: Output becomes input for execution
- Level 2 prompts: Reference for implementation details

## Success Metrics

A high-quality plan demonstrates:

- **Clarity**: Another agent can execute without ambiguity
- **Completeness**: All requirements and risks addressed
- **Evolution**: Clear improvement from V1 to REFINED
- **Practicality**: Executable steps with realistic scope
- **Standards-alignment**: References and follows established patterns
- **Risk-awareness**: Proactively addresses potential issues

Use these guidelines with all planning-related prompts in Level 3.

