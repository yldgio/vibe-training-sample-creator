---
description: 'Execute implementation plans with checkpoints and validation'
---

# Plan Execution with Validation Checkpoints

You are an **implementation coordinator** executing a detailed implementation plan for the password generator.

## Context

You have a refined implementation plan (from `dynamic-planning.prompt.md`) and architectural decisions (from `architecture-decision.prompt.md`). Now execute the plan with built-in checkpoints and validation.

## Execution Framework

### Before Starting

1. **Review Plan**: Read the complete PLAN_REFINED
2. **Identify Phases**: Break plan into logical checkpoints
3. **Define Success Criteria**: For each phase, specify "done" conditions
4. **Set Validation Points**: Where/when to verify correctness

### During Execution

For each phase of the plan:

#### 1. Pre-Phase Checklist

```markdown
### Phase: [Phase Name]

**Objective**: [What are we building in this phase?]

**Prerequisites**:

- [ ] Previous phase complete and validated
- [ ] Required context/dependencies available
- [ ] Success criteria clearly defined

**Plan Reference**: [Which steps from PLAN_REFINED does this cover?]
```

#### 2. Implementation

Execute the planned steps, generating code/content as specified.

#### 3. Checkpoint Validation

After implementing, validate against criteria:

```markdown
**Validation Checklist**:

Functional:

- [ ] [Specific functional requirement met]
- [ ] [Edge case handled]
- [ ] [...]

Quality:

- [ ] Code follows domain instructions (Level 2)
- [ ] Accessibility standards met
- [ ] Security best practices applied
- [ ] Error handling implemented

Testing:

- [ ] Manual verification steps completed
- [ ] Expected outputs verified
- [ ] Edge cases tested
```

#### 4. Issues Log

Document any deviations or problems:

```markdown
**Issues Encountered**:

- Issue: [What went wrong or needed adjustment]
- Resolution: [How it was addressed]
- Impact: [Effect on plan or timeline]
```

## Execution Phases

### Phase 1: Foundation (HTML Structure)

**Scope**: Create semantic HTML markup

**Success Criteria**:

- All form controls present (length input, checkboxes, buttons)
- Proper label associations
- ARIA attributes for accessibility
- data-testid attributes for testing
- Valid HTML5 (no errors)

**Validation**:

- Run HTML validator
- Check with screen reader
- Verify keyboard navigation

### Phase 2: Visual Design (CSS)

**Scope**: Implement styling system

**Success Criteria**:

- CSS variables defined for theme
- Responsive layout (mobile-first)
- All interactive states (hover, focus, active)
- WCAG AA contrast ratios met
- Touch targets minimum 44px

**Validation**:

- Test at 320px, 768px, 1024px widths
- Verify contrast with DevTools
- Check prefers-reduced-motion support

### Phase 3: Core Logic (JavaScript - Pure Functions)

**Scope**: Implement password generation algorithms

**Success Criteria**:

- Character set builder function
- Secure random number generator (crypto API)
- Validation functions with clear errors
- Password generation function
- All functions pure/testable

**Validation**:

- Unit test each function
- Verify crypto.getRandomValues used
- Test edge cases (min/max length, no charset)

### Phase 4: Interactivity (JavaScript - Event Handlers)

**Scope**: Wire up UI to core logic

**Success Criteria**:

- Generate button creates password
- Copy button uses clipboard API with fallback
- Input validation provides feedback
- Error/success messages displayed
- Screen reader announcements working

**Validation**:

- Test all user interactions
- Verify error handling
- Check screen reader feedback
- Test clipboard functionality

### Phase 5: Refinement (Polish & Testing)

**Scope**: Final improvements and comprehensive testing

**Success Criteria**:

- All acceptance criteria met
- No console errors
- Accessibility tested with real screen reader
- Cross-browser verification
- Performance acceptable

**Validation**:

- Complete end-to-end test scenarios
- Run accessibility audit
- Check browser compatibility

## Output Format

Structure execution report as:

```markdown
# Implementation Execution Report

## Executive Summary

- Plan executed: [PLAN_REFINED from dynamic planning]
- Phases completed: [X of Y]
- Overall status: [On track / Issues / Complete]

## Phase 1: [Phase Name]

[Pre-Phase Checklist]

### Implementation

[Generated code or description of what was built]

### Validation Results

[Completed validation checklist]

### Issues & Resolutions

[Any problems encountered and how they were resolved]

---

[Repeat for each phase]

## Final Validation

### All Phases Complete Checklist

- [ ] All functional requirements met
- [ ] All accessibility requirements met
- [ ] All security requirements met
- [ ] All tests passing
- [ ] No critical issues remaining

### Known Limitations

[Any accepted trade-offs or future enhancements]

### Handover Notes

[Information for next stage (e.g., deployment, review)]
```

## Integration with Other Prompts

This prompt should be used **after**:

- `dynamic-planning.prompt.md` (to have PLAN_REFINED)
- `architecture-decision.prompt.md` (to know technical decisions)

It can reference:

- Level 2 domain instructions (CSS, JavaScript, Accessibility, Testability)
- Risk mitigation strategies (from `risk-assessment.prompt.md`)

## Success Criteria

Good plan execution demonstrates:

- Systematic progress through phases
- Validation at each checkpoint
- Documentation of issues and resolutions
- Adherence to plan and standards
- Working, tested implementation
- Clear audit trail of what was built and why

Return structured execution report with all phases documented.
