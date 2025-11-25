---
name: "create-unit-tests"
description: "Generate comprehensive unit tests for password generator"
---

# Prompt: Create Unit Tests for Password Generator

Generate a comprehensive test suite for the password generator application.

## Requirements

Follow standards defined in:

- [Testability Guidelines](../instructions/testability-guidelines.instructions.md)

## Test Framework

Use vanilla JavaScript assertions or describe the test structure for Jest/Vitest.

## Test Suites to Create

### 1. Character Set Builder Tests

Test `buildCharset(options)`:

```javascript
describe('buildCharset', () => {
  // Test single charset selection
  test('includes only uppercase when selected')
  test('includes only lowercase when selected')
  test('includes only numbers when selected')
  test('includes only symbols when selected')
  
  // Test multiple charset combinations
  test('combines uppercase and lowercase')
  test('combines all four charset types')
  
  // Test edge cases
  test('returns empty string when no options selected')
});
```

### 2. Validation Tests

Test `validateOptions(options)`:

```javascript
describe('validateOptions', () => {
  // Valid cases
  test('accepts valid options')
  
  // Length validation
  test('throws error for length less than 4')
  test('throws error for length greater than 128')
  test('throws error for non-numeric length')
  test('throws error for negative length')
  
  // Charset validation
  test('throws error when no charsets selected')
  test('accepts when at least one charset selected')
  
  // Error messages
  test('provides clear error message for invalid length')
  test('provides clear error message for no charset')
});
```

### 3. Password Generation Tests

Test `generatePassword(options)`:

```javascript
describe('generatePassword', () => {
  // Basic functionality
  test('generates password of correct length')
  test('generates password with uppercase when selected')
  test('generates password with lowercase when selected')
  test('generates password with numbers when selected')
  test('generates password with symbols when selected')
  
  // Edge cases
  test('handles minimum length (4 characters)')
  test('handles maximum length (128 characters)')
  test('generates different passwords on multiple calls')
  
  // Error cases
  test('throws error for invalid options')
});
```

### 4. DOM Interaction Tests (Integration)

Test UI interactions:

```javascript
describe('Password Generator UI', () => {
  beforeEach(() => {
    // Setup: render HTML or use jsdom
  });
  
  // User interactions
  test('generates password when generate button clicked')
  test('updates display with generated password')
  test('copies password to clipboard when copy clicked')
  test('shows success message after copy')
  
  // Validation feedback
  test('shows error when length out of range')
  test('shows error when no charsets selected')
  test('disables generate button when invalid state')
  
  // Accessibility
  test('announces password generation to screen readers')
  test('announces errors to screen readers')
  test('maintains focus after button click')
});
```

### 5. Clipboard Tests

Test clipboard functionality:

```javascript
describe('Clipboard operations', () => {
  test('copies text using modern clipboard API')
  test('falls back to execCommand when clipboard API unavailable')
  test('handles clipboard write errors gracefully')
  test('shows success feedback after successful copy')
  test('shows error feedback when copy fails')
});
```

## Test Data

Provide sample test data:

```javascript
const validOptions = {
  length: 12,
  includeUpper: true,
  includeLower: true,
  includeNumbers: true,
  includeSymbols: true
};

const minLengthOptions = {
  length: 4,
  includeUpper: true,
  includeLower: false,
  includeNumbers: false,
  includeSymbols: false
};

const maxLengthOptions = {
  length: 128,
  includeUpper: true,
  includeLower: true,
  includeNumbers: true,
  includeSymbols: true
};

const invalidOptions = [
  { length: 3, includeUpper: true },  // Too short
  { length: 129, includeUpper: true }, // Too long
  { length: 12, includeUpper: false, includeLower: false, includeNumbers: false, includeSymbols: false }, // No charset
];
```

## Output Format

Return test code in this structure:

```javascript
// ===== Test Setup =====

// Import or define functions to test
// Setup test data

// ===== Unit Tests =====

describe('Module: Character Set Builder', () => {
  // Tests here
});

describe('Module: Validation', () => {
  // Tests here
});

describe('Module: Password Generation', () => {
  // Tests here
});

// ===== Integration Tests =====

describe('UI: User Interactions', () => {
  // Tests here
});

describe('UI: Error Handling', () => {
  // Tests here
});

// ===== Accessibility Tests =====

describe('Accessibility', () => {
  test('all inputs have labels')
  test('error messages announced')
  test('success messages announced')
  test('focus indicators visible')
  test('keyboard navigation works')
});
```

Include:

- Clear test descriptions
- Arrange-Act-Assert pattern
- Edge cases and error cases
- Accessibility tests
- Comments explaining complex assertions
