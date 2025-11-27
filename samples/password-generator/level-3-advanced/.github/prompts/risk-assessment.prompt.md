---
description: 'Identify risks and create mitigation strategies'
---

# Risk Assessment for Password Generator

You are a **risk assessment specialist** evaluating potential issues in the password generator implementation.

## Context

Before implementing the password generator, perform a comprehensive risk assessment to identify potential problems and plan mitigation strategies.

## Risk Assessment Framework

For each risk category below:

1. **Identify risks**: List specific things that could go wrong
2. **Assess impact**: How severe would this issue be? (Critical/High/Medium/Low)
3. **Assess likelihood**: How likely is this to occur? (Very Likely/Likely/Possible/Unlikely)
4. **Prioritize**: Impact × Likelihood = Priority
5. **Mitigate**: What strategies can reduce or eliminate the risk?

## Risk Categories

### 1. Security Risks

**Context**: Password generator must be cryptographically secure

**Potential Risks**:

- Weak randomness source used
- Insufficient entropy in generated passwords
- Client-side vulnerabilities (XSS, injection)
- Password exposure in browser history/cache
- Clipboard security concerns

**For Each Risk**:

- Describe the threat
- Rate impact and likelihood
- Propose mitigation strategy
- Specify validation method (how to verify mitigation works)

### 2. Accessibility Risks

**Context**: Must meet WCAG 2.1 AA standards

**Potential Risks**:

- Missing labels or ARIA attributes
- Keyboard navigation issues
- Insufficient color contrast
- Screen reader incompatibility
- Focus management problems
- Dynamic content not announced

**For Each Risk**:

- Identify what could fail
- Describe user impact
- Rate severity
- Propose preventive measures
- Define testing approach

### 3. Usability Risks

**Context**: Users need clear, intuitive interface

**Potential Risks**:

- Confusing UI/unclear controls
- Inadequate error messages
- Missing feedback for actions
- Mobile usability issues
- Browser compatibility problems
- Edge case handling (e.g., minimum length, no charsets selected)

**For Each Risk**:

- Describe usability failure
- Identify affected users
- Rate impact
- Suggest UX improvements
- Define acceptance criteria

### 4. Reliability Risks

**Context**: Application must work consistently

**Potential Risks**:

- Unhandled exceptions crash app
- Invalid input causes errors
- Browser API unavailability (e.g., crypto, clipboard)
- Inconsistent state after errors
- Memory leaks or performance degradation

**For Each Risk**:

- Specify failure mode
- Describe consequences
- Rate probability
- Design error handling strategy
- Define recovery behavior

### 5. Maintainability Risks

**Context**: Code should be testable and modifiable

**Potential Risks**:

- Tight coupling between components
- Unclear code organization
- Insufficient documentation
- Missing tests for critical paths
- Hardcoded values and magic numbers
- Complex, difficult-to-test logic

**For Each Risk**:

- Identify maintainability issue
- Explain long-term impact
- Rate technical debt severity
- Recommend architectural patterns
- Suggest code quality measures

## Output Format

Use this structure for each risk category:

```markdown
## Risk Category: [Category Name]

### Risk: [Specific Risk Name]

**Description**: [What could go wrong?]

**Impact**: [Critical/High/Medium/Low]  
**Likelihood**: [Very Likely/Likely/Possible/Unlikely]  
**Priority**: [Impact × Likelihood score]

**Consequences**:

- [List specific negative outcomes]
- [...]

**Mitigation Strategy**:

1. [Preventive measure 1]
2. [Preventive measure 2]
3. [...]

**Validation**:

- How to test that mitigation is effective
- Acceptance criteria for "risk mitigated"

**Implementation Notes**:

- Where in the codebase this applies
- Dependencies or prerequisites
- Any trade-offs in mitigation approach

---

[Repeat for each risk in category]
```

## Prioritization Matrix

After analyzing all risks, create a summary matrix:

```markdown
## Risk Priority Matrix

| Risk | Category | Impact | Likelihood | Priority | Mitigation Status |
|------|----------|--------|------------|----------|-------------------|
| [Risk name] | Security | Critical | Likely | HIGH | Planned |
| [...] | [...] | [...] | [...] | [...] | [...] |

Sort by priority (highest first)
```

## Mitigation Roadmap

Create an ordered checklist of mitigations:

```markdown
## Mitigation Implementation Order

### Phase 1: Critical Risks (Must Have)

- [ ] [Mitigation for critical risk 1]
- [ ] [Mitigation for critical risk 2]

### Phase 2: High Priority (Should Have)

- [ ] [Mitigation for high-priority risk 1]
- [ ] [...]

### Phase 3: Medium Priority (Nice to Have)

- [ ] [Mitigation for medium risk 1]
- [ ] [...]
```

## Success Criteria

Effective risk assessment demonstrates:

- Comprehensive coverage (doesn't miss obvious risks)
- Realistic impact/likelihood ratings
- Specific, actionable mitigation strategies
- Testable validation criteria
- Prioritization based on actual project constraints
- Integration with implementation plan

Return complete risk assessment with all sections filled out.
