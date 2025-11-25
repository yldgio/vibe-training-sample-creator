# Level 2: Intermediate - Predictable Output with Domain Instructions

This level focuses on **predictability and consistency** by using domain-specific instructions and task-specific prompts.

Instead of flexible, general prompts, this level demonstrates how to:

- **Constrain outputs** using domain-specific instructions (CSS standards, JavaScript best practices, accessibility rules, testability patterns).
- **Create repeatable prompts** for common tasks (create UI component, add event handler, generate tests).
- **Ensure consistency** across multiple generations through few-shot examples and explicit coding standards.

The goal is still to create a secure password generator web app, but now with **predictable, standardized** code that follows established patterns.

## Concept

By separating **domain knowledge** (instructions) from **task execution** (prompts), we ensure:

- Consistent code style and structure
- Predictable adherence to best practices
- Reusable patterns for similar tasks
- Clear separation of concerns

## Files

### Domain-Specific Instructions (`.github/instructions/`)

These files apply automatically to matching file types and enforce standards:

- `css-standards.instructions.md`: CSS architecture, naming, responsive design, accessibility
- `javascript-patterns.instructions.md`: JavaScript/TypeScript patterns, error handling, async code
- `accessibility-rules.instructions.md`: WCAG compliance, semantic HTML, ARIA usage
- `testability-guidelines.instructions.md`: Test structure, coverage, patterns

### Task-Specific Prompts (`.github/prompts/`)

These prompts are designed for repeatable, predictable tasks:

- `create-ui-component.prompt.md`: Generate a UI component following established patterns
- `add-event-handler.prompt.md`: Add event handlers with proper validation and error handling
- `generate-styles.prompt.md`: Create CSS following project standards
- `create-unit-tests.prompt.md`: Generate tests with specific patterns and coverage

### Orchestration

## Concept: Predictability Through Separation

Instead of relying on the agent to remember best practices, we:

1. **Encode domain knowledge** in `.instructions.md` files that apply automatically to relevant file types
2. **Create task-specific prompts** for repeatable operations
3. **Enforce standards** through explicit references in prompts

This ensures every generation follows the same patterns and standards.

## Domain-Specific Instructions (Automatic Application)

These files in `.github/instructions/` automatically apply when working with matching file types:

- `css-standards.instructions.md` → Applies to all CSS/HTML files
- `javascript-patterns.instructions.md` → Applies to all JavaScript files  
- `accessibility-rules.instructions.md` → Applies across HTML/CSS/JS for WCAG compliance
- `testability-guidelines.instructions.md` → Applies to ensure code is testable

These instructions are **always active** when editing matching files, ensuring consistency.

## Task-Specific Prompts (Manual Invocation)

Use these prompts in `.github/prompts/` for specific, repeatable tasks:

### 1. Create UI Component

**Prompt:** `create-ui-component.prompt.md`

**Purpose:** Generate semantic HTML structure

**When to use:** Starting a new project or regenerating HTML

**References:** CSS Standards, Accessibility Rules

**Output:** Valid HTML5 with proper ARIA, labels, and test attributes

### 2. Generate Styles

**Prompt:** `generate-styles.prompt.md`

**Purpose:** Create CSS following project standards

**When to use:** After HTML is created or when updating styles

**References:** CSS Standards

**Output:** Complete CSS with variables, responsive design, accessibility features

### 3. Implement Password Logic

**Prompt:** `implement-password-logic.prompt.md`

**Purpose:** Create core password generation functions

**When to use:** Implementing business logic

**References:** JavaScript Patterns, Testability Guidelines

**Output:** Pure functions for password generation with proper validation

### 4. Add Event Handlers

**Prompt:** `add-event-handlers.prompt.md`

**Purpose:** Implement UI event handling

**When to use:** After HTML and logic are in place

**References:** JavaScript Patterns, Accessibility Rules

**Output:** Event handlers with validation, feedback, and screen reader support

### 5. Create Unit Tests

**Prompt:** `create-unit-tests.prompt.md`

**Purpose:** Generate comprehensive test suite

**When to use:** After implementation is complete

**References:** Testability Guidelines

**Output:** Test suites covering units, integration, edge cases, accessibility

## Recommended Workflow

### Step 1: Structure (HTML)

Run `create-ui-component.prompt.md` to generate semantic HTML with:

- Proper labels and ARIA attributes
- data-testid attributes for testing
- Accessible form controls

### Step 2: Appearance (CSS)

Run `generate-styles.prompt.md` to create styles that:

- Follow consistent color/spacing system
- Meet WCAG AA contrast requirements
- Provide responsive, mobile-first design
- Include all interactive states (hover, focus, active)

### Step 3: Core Logic (JavaScript - Part 1)

Run `implement-password-logic.prompt.md` to create:

- Pure functions for password generation
- Secure randomness using crypto API
- Validation logic with clear errors
- Testable, modular code structure

### Step 4: Interactivity (JavaScript - Part 2)

Run `add-event-handlers.prompt.md` to add:

- Event listeners for buttons and inputs
- Error handling and user feedback
- Clipboard functionality with fallbacks
- Screen reader announcements

### Step 5: Testing

Run `create-unit-tests.prompt.md` to generate:

- Unit tests for pure functions
- Integration tests for UI interactions
- Accessibility tests
- Edge case coverage

## Key Benefits of This Approach

### Consistency

Every time you run a prompt, it references the same instructions, ensuring:

- Same code style and patterns
- Same accessibility standards
- Same testing approach

### Predictability

You know exactly what output to expect because:

- Instructions are explicit and detailed
- Prompts have clear, focused scope
- References ensure alignment across prompts

### Reusability

The same prompts and instructions can be used for:

- Regenerating parts of the app
- Creating similar features
- Starting new projects with same standards

### Maintainability

When standards change:

- Update the instruction file once
- All future generations use new standards
- Clear documentation of current standards

## Tips for Best Results

1. **Run prompts in order** - Follow the recommended workflow for dependencies
2. **Reference instructions explicitly** - Each prompt links to relevant instruction files
3. **One concern per prompt** - Don't mix HTML generation with JavaScript logic
4. **Validate between steps** - Test HTML before adding JavaScript, test logic before UI handlers
5. **Iterate on instructions** - If outputs aren't quite right, refine the instruction files

## Example Usage

```markdown
# In VS Code with GitHub Copilot

1. Open new file: index.html
2. Open command palette (Ctrl+Shift+P)
3. Select "Prompts: Apply Prompt"
4. Choose: create-ui-component.prompt.md
5. Review generated HTML
6. Open command palette again
7. Choose: generate-styles.prompt.md
8. Review generated CSS
9. Continue with remaining prompts...
```

## Comparison with Level 1

**Level 1 (Basic):**

- Single one-shot prompt
- Everything in one go
- Flexible but unpredictable
- Good for quick prototypes

**Level 2 (Intermediate):**

- Multiple focused prompts
- Domain-specific instructions
- Predictable, consistent output
- Good for production code with standards

## Next: Level 3

Level 3 takes this further by adding:

- Dynamic planning with revision loops
- Tool integration and reasoning
- Multi-agent orchestration
- Complex workflow management

