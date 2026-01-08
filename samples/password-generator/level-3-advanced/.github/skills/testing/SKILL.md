---
name: password-generator-testing
description: Comprehensive testing workflow for password generator applications. Use when creating, running, or debugging tests for password generation functionality.
license: MIT
---

# Password Generator Testing Workflow

## When to Use
Use this skill for comprehensive testing of password generator functionality including unit tests, integration tests, and e2e tests.

## Testing Strategy

### 1. Unit Tests
Test individual functions in isolation:
- `generatePassword()` - core generation logic
- `calculateStrength()` - password strength calculation
- `validateOptions()` - user input validation

### 2. Integration Tests
Test component interactions:
- UI updates when options change
- Password display updates on generation
- Strength meter reflects password quality

### 3. E2E Tests
Test complete user workflows:
- Generate password with default settings
- Customize all options and generate
- Copy password to clipboard

## Test Template
Use the [test template](./test-template.js) as a starting point for new tests.

## Running Tests

```bash
# Run all tests
npm test

# Run with coverage report
npm test -- --coverage

# Run specific test file
npm test -- password.test.js

# Watch mode for development
npm test -- --watch
```

## Debugging Failed Tests
1. Check test output for specific assertion failures
2. Use `console.log` to inspect intermediate values
3. Run single test in isolation with `.only`
4. Verify test fixtures match expected format
