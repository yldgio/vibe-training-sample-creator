# Password Generator - Level 2 Intermediate

This project uses domain-specific instructions for predictable, consistent code generation.

## Project Overview

Build a secure password generator using vanilla HTML, CSS, and JavaScript following established patterns and best practices.

## Tech Stack

- HTML5 for structure (semantic elements, accessibility)
- CSS3 for styling (custom properties, responsive design)
- Vanilla JavaScript (ES6+) for functionality

## Instructions

Domain-specific instructions are in `.github/instructions/`:

- **css-standards.instructions.md**: CSS architecture and styling patterns
- **javascript-patterns.instructions.md**: JavaScript coding standards
- **accessibility-rules.instructions.md**: WCAG 2.1 AA compliance
- **testability-guidelines.instructions.md**: Testing patterns and practices
- **security-best-practices.instructions.md**: Security requirements
- **performance-best-practices.instructions.md**: Performance optimization

## Workflow

1. Run `create-ui-component.prompt.md` for HTML structure
2. Run `generate-styles.prompt.md` for CSS styling
3. Run `implement-password-logic.prompt.md` for core logic
4. Run `add-event-handlers.prompt.md` for interactivity
5. Run `create-unit-tests.prompt.md` for test suite

## Key Requirements

- Use `crypto.getRandomValues()` for secure random number generation
- Follow WCAG 2.1 AA accessibility standards
- Ensure code is testable with clear separation of concerns
- Use data-testid attributes for testing hooks
