---
description: 'Implement password generation logic following JavaScript best practices'
---

# Implement Password Generation Logic

Create the JavaScript logic for secure password generation.

## Requirements

Follow all standards defined in:

- [JavaScript Patterns](../instructions/javascript-patterns.instructions.md)
- [Testability Guidelines](../instructions/testability-guidelines.instructions.md)

## Core Functions to Implement

### 1. Character Set Builder

Create a pure function `buildCharset(options)` that:

- Takes options object with boolean flags (includeUpper, includeLower, includeNumbers, includeSymbols)
- Returns concatenated string of selected character sets
- Uses predefined charset constants
- Returns empty string if no options selected

### 2. Secure Random Integer Generator

Create a function `getSecureRandomInt(max)` that:

- Uses `crypto.getRandomValues()` (NOT Math.random)
- Returns random integer between 0 and max-1
- Handles Uint32Array buffer correctly

### 3. Options Validator

Create a function `validateOptions(options)` that:

- Checks length is between 4 and 128
- Ensures at least one character type is selected
- Throws descriptive errors with specific error types
- Returns true if valid

### 4. Password Generator

Create a function `generatePassword(options)` that:

- Validates options first
- Builds charset from options
- Generates password using secure random
- Returns generated password string
- Is pure/deterministic given same random seed (testable)

## State Management

Create an explicit state object:

```javascript
const AppState = {
  options: {
    length: 12,
    includeUpper: true,
    includeLower: true,
    includeNumbers: true,
    includeSymbols: true
  },
  generatedPassword: ''
};
```

## Module Organization

Structure code in this order:

1. **Constants** (character sets, min/max length, defaults)
2. **State** (AppState object)
3. **Utility Functions** (pure functions for logic)
4. **Validation Functions**
5. **Core Generation Function**
6. **DOM Helper Functions** (get/set values)
7. **Event Handlers** (delegate to pure functions)
8. **Initialization** (attach event listeners, set defaults)

## Output Format

Return JavaScript embedded in `<script>` tags with:

- Clear section comments
- JSDoc comments for public functions
- Use const/let (never var)
- Descriptive variable names
- Single responsibility per function
- Error handling with try-catch
- No console.log (use console.error only for errors)

The code should be testable, readable, and follow all security best practices.
