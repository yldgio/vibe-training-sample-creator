---
description: 'Generate the password generator UI component with proper HTML structure'
---

# Create Password Generator UI Component

Create the HTML structure for the password generator web application.

## Requirements

Follow the standards defined in:

- [CSS Standards](../instructions/css-standards.instructions.md)
- [Accessibility Rules](../instructions/accessibility-rules.instructions.md)

## Structure

Create a semantic HTML structure with the following elements:

1. **Main container** (`<main>`)
   - Heading: "Password Generator"
   - Form element containing all controls

2. **Password length control**
   - Label associated with input
   - Number input (min: 4, max: 128, default: 12)
   - Help text describing valid range
   - Use `data-testid="password-length-input"` for testing

3. **Character type checkboxes** (group with fieldset/legend)
   - Uppercase letters (A-Z) - checked by default
   - Lowercase letters (a-z) - checked by default
   - Numbers (0-9) - checked by default
   - Symbols (!@#$...) - checked by default
   - Each with proper label association
   - Use data-testid attributes for testing

4. **Password display area**
   - Text container showing generated password
   - Initially empty with placeholder text
   - ARIA attributes for screen reader support
   - Use `data-testid="password-output"`

5. **Action buttons**
   - Generate button (primary action)
   - Copy to Clipboard button (with icon + text)
   - Proper ARIA labels
   - Minimum 44x44px touch targets
   - Use data-testid attributes

6. **Feedback area** for messages
   - Success messages (password copied)
   - Error messages (validation failures)
   - Use `role="alert"` for announcements
   - Use `role="status"` for non-critical updates

## Output Format

Return valid HTML5 with:

- Proper semantic elements
- Associated labels for all inputs
- ARIA attributes where needed
- data-testid attributes for testing
- Unique IDs for all form controls
- Commented sections for clarity

Do NOT include CSS or JavaScript in this step.
