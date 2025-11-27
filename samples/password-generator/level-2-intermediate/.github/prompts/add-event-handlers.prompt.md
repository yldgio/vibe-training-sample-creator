---
description: 'Implement event handlers with proper validation and feedback'
---

# Add Event Handlers for Password Generator

Implement all event handlers for the password generator UI.

## Requirements

Follow standards defined in:

- [JavaScript Patterns](../instructions/javascript-patterns.instructions.md)
- [Accessibility Rules](../instructions/accessibility-rules.instructions.md)

## Event Handlers to Implement

### 1. Generate Button Click Handler

Create `handleGenerateClick()` function that:

- Reads current options from form inputs
- Validates options (try-catch for errors)
- Calls password generation function
- Updates password display
- Handles and displays errors in feedback area
- Announces result to screen readers (aria-live region)

### 2. Copy Button Click Handler

Create `handleCopyClick()` async function that:

- Gets current password from display
- Validates password exists
- Copies to clipboard using async clipboard API
- Provides fallback for older browsers
- Shows success feedback (visual + screen reader announcement)
- Handles errors gracefully with user-friendly message

### 3. Length Input Change Handler

Create `handleLengthChange()` function that:

- Validates input value (4-128 range)
- Updates AppState
- Provides immediate feedback for invalid values
- Enforces min/max constraints

### 4. Checkbox Change Handler

Create `handleCheckboxChange()` function that:

- Updates AppState when checkboxes change
- Validates at least one checkbox is selected
- Disables/enables generate button if no checkboxes selected
- Provides feedback if trying to uncheck last checkbox

## DOM Helper Functions

Create these utility functions:

### `getOptionsFromForm()`

- Reads values from all form inputs
- Returns options object
- Handles type conversions (string to number, etc.)

### `displayPassword(password)`

- Updates password display element
- Updates screen reader announcement
- Clears any previous error messages

### `showFeedback(message, type)`

- Shows feedback message (success/error)
- Updates aria-live region for screen readers
- Auto-clears after delay (3 seconds for success, persistent for errors)
- Uses appropriate role (alert/status)

### `showError(message)`

- Displays error in feedback area
- Uses role="alert" for immediate announcement
- Shows error icon + text

## Event Listener Attachment

In initialization function:

- Query DOM elements once and cache references
- Use `addEventListener` (not inline handlers)
- Attach all event listeners
- Set initial form state

## Output Format

Return JavaScript code that:

- Groups event handlers together
- Provides clear separation between handlers and helpers
- Includes error handling in all handlers
- Uses async/await for clipboard operations
- Provides comprehensive user feedback
- Announces changes to screen readers

Example structure:

```javascript
// ===== Event Handlers =====

function handleGenerateClick() {
  try {
    // Implementation
  } catch (error) {
    showError(error.message);
    console.error('Generation error:', error);
  }
}

async function handleCopyClick() {
  try {
    // Implementation
  } catch (error) {
    showError('Failed to copy password');
    console.error('Copy error:', error);
  }
}

// ===== Initialization =====

function initApp() {
  // Cache DOM references
  // Attach event listeners
  // Set initial state
}

// Start app when DOM is ready
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initApp);
} else {
  initApp();
}
```
