---
description: Multi-stage dynamic planning with self-review and refinement
---

# Prompt: Dynamic Planning for Password Generator

You are a **planning agent** responsible for creating a comprehensive implementation strategy for a secure password generator web app.

## Objectives

Your goal is to demonstrate **multi-stage planning** with explicit revision:

1. Create an initial plan based on requirements
2. Perform critical self-review
3. Refine the plan based on identified issues
4. Produce a final, robust implementation strategy

## Requirements

The password generator must:

- Use `crypto.getRandomValues()` for cryptographically secure randomness
- Support configurable password length (4-128 characters)
- Allow selection of character types: uppercase, lowercase, numbers, symbols
- Provide a copy-to-clipboard feature
- Be a single-page web application (HTML + CSS + JavaScript)
- Follow WCAG 2.1 AA accessibility standards
- Be testable and maintainable

## Planning Process

### Stage 1: Initial Planning (PLAN_V1)

Create a high-level implementation plan with these sections:

1. **Project Understanding**
   - Restate the goal in your own words
   - List key functional requirements
   - List key non-functional requirements (security, accessibility, UX)

2. **Architecture Overview**
   - Technology stack (HTML5, CSS3, modern JavaScript)
   - Code organization approach
   - Key components and their responsibilities

3. **Implementation Steps** (5-10 major steps)
   - Phase 1: Structure and markup
   - Phase 2: Styling and responsive design
   - Phase 3: Core logic and validation
   - Phase 4: Event handling and interactivity
   - Phase 5: Testing and refinement

4. **Security Considerations**
   - Cryptographic randomness requirements
   - Input validation needs
   - XSS prevention strategies

5. **Accessibility Considerations**
   - Semantic HTML requirements
   - ARIA attribute needs
   - Keyboard navigation support
   - Screen reader announcements

### Stage 2: Self-Review (PLAN_REVIEW)

Critically analyze PLAN_V1 by asking:

- **Completeness**: Are there missing steps or overlooked requirements?
- **Risks**: What could go wrong? What edge cases need handling?
- **Dependencies**: Are steps in the right order? Any circular dependencies?
- **Clarity**: Is each step specific enough for an implementer to follow?
- **Standards**: Does it align with best practices (from Level 2 instructions)?
- **Testability**: Can each component be tested independently?

Document issues found in these categories:

- Missing steps or requirements
- Potential risks or edge cases
- Ambiguous or unclear instructions
- Sequencing or dependency issues
- Gaps in accessibility or security considerations

### Stage 3: Refinement (PLAN_REFINED)

Based on the review, create an improved plan that:

- Addresses all issues identified in PLAN_REVIEW
- Adds missing details or steps
- Reorders or restructures as needed
- Includes risk mitigation strategies
- Provides more specific guidance where needed

## Output Format

Structure your response with these clearly labeled sections:

```markdown
## PLAN_V1: Initial Plan

[Your initial plan here - do not modify after review]

## PLAN_REVIEW: Self-Critique

[Document issues and insights from reviewing V1]

## PLAN_REFINED: Final Plan

[Your improved plan addressing review findings]

## SUMMARY: Key Changes

[Briefly list the main improvements from V1 to REFINED]
```

## Evaluation Criteria

A good dynamic plan demonstrates:

- Clear evolution from V1 to REFINED (shows learning)
- Specific, actionable steps (not vague generalities)
- Anticipation of edge cases and failure modes
- Consideration of multiple concerns (security, accessibility, testability)
- Appropriate level of detail (not too high-level, not too granular)
- Logical sequencing with clear dependencies

Return only the structured plan output described above.
