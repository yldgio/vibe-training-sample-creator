---
description: Design for testability guidelines for password generator
applyTo: '**/*.js, **/*.html'
---

# Testability Guidelines

Apply these patterns to ensure code is easily testable for the password generator web app.

## Code Organization for Testability

### Separation of Concerns

- Separate **business logic** from **UI logic**
- Pure functions for core algorithms (password generation)
- UI handlers delegate to pure functions
- Makes unit testing easier without DOM

```javascript
// Good - Testable separation
// Pure business logic (easy to test)
function generatePassword({ length, includeUpper, includeLower, includeNumbers, includeSymbols }) {
  // No DOM dependencies
  // Pure logic only
  return password;
}

// UI handler (delegates to pure function)
function handleGenerateClick() {
  const options = getOptionsFromForm();
  const password = generatePassword(options);  // Call pure function
  displayPassword(password);
}

// Bad - Mixed concerns (hard to test)
function handleGenerateClick() {
  const length = document.querySelector('#length').value;
  // All logic mixed with DOM access
  // Hard to test without DOM
}
```

### Function Purity

- Write pure functions when possible (same input → same output)
- No side effects in pure functions
- Easier to test, reason about, and debug

```javascript
// Good - Pure function (deterministic given same random source)
function generatePasswordFromCharset(charset, length, randomFunc) {
  let password = '';
  for (let i = 0; i < length; i++) {
    const randomIndex = randomFunc(charset.length);
    password += charset[randomIndex];
  }
  return password;
}

// Testable with mocked random function
function testableGeneratePassword(options) {
  const charset = buildCharset(options);
  return generatePasswordFromCharset(charset, options.length, (max) => {
    const buffer = new Uint32Array(1);
    crypto.getRandomValues(buffer);
    return buffer[0] % max;
  });
}

// Bad - Impure, hard to test (relies on global crypto)
function generatePassword(length) {
  let password = '';
  const chars = 'ABC...';  // Global dependency
  for (let i = 0; i < length; i++) {
    const index = crypto.getRandomValues(new Uint32Array(1))[0] % chars.length;
    password += chars[index];
  }
  return password;  // Non-deterministic, hard to test
}
```

### Dependency Injection

- Pass dependencies as parameters (don't hardcode)
- Makes mocking/stubbing easy in tests
- Increases flexibility

```javascript
// Good - Dependencies injected
function buildCharset({ includeUpper, includeLower, includeNumbers, includeSymbols }, charsets) {
  let result = '';
  if (includeUpper) result += charsets.uppercase;
  if (includeLower) result += charsets.lowercase;
  if (includeNumbers) result += charsets.numbers;
  if (includeSymbols) result += charsets.symbols;
  return result;
}

// Usage
const DEFAULT_CHARSETS = {
  uppercase: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
  lowercase: 'abcdefghijklmnopqrstuvwxyz',
  numbers: '0123456789',
  symbols: '!@#$%^&*()_+-=[]{}|;:,.<>?'
};

const charset = buildCharset(options, DEFAULT_CHARSETS);

// In tests, can inject custom charsets
const testCharset = buildCharset(options, { uppercase: 'ABC', lowercase: 'abc' });
```

## Structuring Testable Code

### Module Pattern

- Group related functions into modules
- Export functions that need testing
- Keep internal helpers private

```javascript
// Good - Module with clear exports
const PasswordGenerator = (() => {
  // Constants
  const CHARSETS = {
    uppercase: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
    lowercase: 'abcdefghijklmnopqrstuvwxyz',
    numbers: '0123456789',
    symbols: '!@#$%^&*()_+-=[]{}|;:,.<>?'
  };

  // Private helper
  function getSecureRandomInt(max) {
    const buffer = new Uint32Array(1);
    crypto.getRandomValues(buffer);
    return buffer[0] % max;
  }

  // Public API (testable)
  function buildCharset(options) {
    let charset = '';
    if (options.includeUpper) charset += CHARSETS.uppercase;
    if (options.includeLower) charset += CHARSETS.lowercase;
    if (options.includeNumbers) charset += CHARSETS.numbers;
    if (options.includeSymbols) charset += CHARSETS.symbols;
    return charset;
  }

  function validateOptions(options) {
    if (options.length < 4 || options.length > 128) {
      throw new Error('Length must be between 4 and 128');
    }
    if (!options.includeUpper && !options.includeLower && 
        !options.includeNumbers && !options.includeSymbols) {
      throw new Error('At least one character type must be selected');
    }
  }

  function generate(options) {
    validateOptions(options);
    const charset = buildCharset(options);
    let password = '';
    for (let i = 0; i < options.length; i++) {
      password += charset[getSecureRandomInt(charset.length)];
    }
    return password;
  }

  // Export public API
  return {
    generate,
    buildCharset,
    validateOptions,
    CHARSETS  // Export for testing if needed
  };
})();

// For testing in Node/Jest environment
if (typeof module !== 'undefined' && module.exports) {
  module.exports = PasswordGenerator;
}
```

### Single Responsibility

- Each function does one thing
- Easy to test in isolation
- Clear test cases per function

```javascript
// Good - Single responsibility
function validatePasswordLength(length) {
  if (typeof length !== 'number') {
    throw new TypeError('Length must be a number');
  }
  if (length < 4 || length > 128) {
    throw new RangeError('Length must be between 4 and 128');
  }
  return true;
}

function validateCharsetOptions(options) {
  if (!options.includeUpper && !options.includeLower && 
      !options.includeNumbers && !options.includeSymbols) {
    throw new Error('At least one character type must be selected');
  }
  return true;
}

// Easy to test separately
// - Test validatePasswordLength with various inputs
// - Test validateCharsetOptions independently

// Bad - Multiple responsibilities
function validate(options) {
  // Length validation
  if (options.length < 4) throw new Error('Too short');
  // Charset validation
  if (!options.includeUpper && !options.includeLower) throw new Error('Need charsets');
  // Other validation...
  // Hard to test specific validation logic
}
```

## Test Data Attributes

- Add `data-testid` attributes for stable test selectors
- Don't rely on classes or IDs that may change
- Makes tests more resilient to refactoring

```html
<!-- Good - Test-specific attributes -->
<div class="password-generator">
  <input 
    type="number" 
    id="password-length"
    data-testid="password-length-input"
    value="12"
  >
  
  <div class="checkboxes">
    <label>
      <input 
        type="checkbox" 
        id="include-uppercase"
        data-testid="uppercase-checkbox"
        checked
      >
      Uppercase
    </label>
  </div>
  
  <button 
    type="button" 
    id="generate-btn"
    data-testid="generate-button"
  >
    Generate
  </button>
  
  <div 
    id="password-display"
    data-testid="password-output"
    role="textbox"
    aria-readonly="true"
  ></div>
</div>
```

## Error Handling for Testing

- Throw specific error types
- Include helpful error messages
- Makes testing error cases easier

```javascript
// Good - Specific errors with clear messages
class PasswordValidationError extends Error {
  constructor(message, code) {
    super(message);
    this.name = 'PasswordValidationError';
    this.code = code;
  }
}

function validateOptions(options) {
  if (options.length < 4) {
    throw new PasswordValidationError(
      'Password length must be at least 4 characters',
      'LENGTH_TOO_SHORT'
    );
  }
  
  if (options.length > 128) {
    throw new PasswordValidationError(
      'Password length cannot exceed 128 characters',
      'LENGTH_TOO_LONG'
    );
  }
  
  if (!hasAnyCharsetSelected(options)) {
    throw new PasswordValidationError(
      'At least one character type must be selected',
      'NO_CHARSET_SELECTED'
    );
  }
}

// Test example
test('throws error for length too short', () => {
  expect(() => validateOptions({ length: 2 }))
    .toThrow(PasswordValidationError);
  
  expect(() => validateOptions({ length: 2 }))
    .toThrow('Password length must be at least 4 characters');
});
```

## State Management for Testing

- Make state observable and controllable
- Avoid hidden/implicit state
- Initialize state explicitly

```javascript
// Good - Explicit, testable state
const AppState = {
  options: {
    length: 12,
    includeUpper: true,
    includeLower: true,
    includeNumbers: true,
    includeSymbols: true
  },
  generatedPassword: '',
  lastError: null
};

function getOptions() {
  return { ...AppState.options };  // Return copy
}

function setOptions(newOptions) {
  AppState.options = { ...AppState.options, ...newOptions };
}

function getPassword() {
  return AppState.generatedPassword;
}

function setPassword(password) {
  AppState.generatedPassword = password;
}

// In tests, can easily inspect and manipulate state
```

## Mock-Friendly Design

### Abstract external dependencies

```javascript
// Good - Abstracted clipboard API (can mock in tests)
const ClipboardService = {
  async copy(text) {
    if (navigator.clipboard && navigator.clipboard.writeText) {
      return await navigator.clipboard.writeText(text);
    } else {
      return this.fallbackCopy(text);
    }
  },
  
  fallbackCopy(text) {
    const textarea = document.createElement('textarea');
    textarea.value = text;
    document.body.appendChild(textarea);
    textarea.select();
    const success = document.execCommand('copy');
    document.body.removeChild(textarea);
    return success ? Promise.resolve() : Promise.reject(new Error('Copy failed'));
  }
};

// In tests, can mock ClipboardService
const mockClipboard = {
  copy: jest.fn().mockResolvedValue(undefined)
};
```

## Test Structure Hints

When writing code, consider these test categories:

### Unit Tests (for pure functions)

```javascript
// buildCharset function tests
describe('buildCharset', () => {
  test('includes uppercase when option is true', () => {
    const result = buildCharset({ includeUpper: true, includeLower: false, includeNumbers: false, includeSymbols: false });
    expect(result).toBe('ABCDEFGHIJKLMNOPQRSTUVWXYZ');
  });
  
  test('combines multiple charsets', () => {
    const result = buildCharset({ includeUpper: true, includeLower: true, includeNumbers: false, includeSymbols: false });
    expect(result).toContain('A');
    expect(result).toContain('a');
  });
  
  test('returns empty string when no options selected', () => {
    const result = buildCharset({ includeUpper: false, includeLower: false, includeNumbers: false, includeSymbols: false });
    expect(result).toBe('');
  });
});
```

### Integration Tests (for UI interactions)

```javascript
// Using Testing Library or similar
describe('Password Generator UI', () => {
  test('generates password when button clicked', () => {
    render(/* app HTML */);
    
    const generateButton = screen.getByTestId('generate-button');
    const passwordOutput = screen.getByTestId('password-output');
    
    fireEvent.click(generateButton);
    
    expect(passwordOutput.textContent).toHaveLength(12);  // Default length
  });
  
  test('shows error when no charset selected', () => {
    render(/* app HTML */);
    
    // Uncheck all checkboxes
    fireEvent.click(screen.getByTestId('uppercase-checkbox'));
    fireEvent.click(screen.getByTestId('lowercase-checkbox'));
    fireEvent.click(screen.getByTestId('numbers-checkbox'));
    fireEvent.click(screen.getByTestId('symbols-checkbox'));
    
    const generateButton = screen.getByTestId('generate-button');
    fireEvent.click(generateButton);
    
    expect(screen.getByRole('alert')).toHaveTextContent('at least one character type');
  });
});
```

### Edge Case Tests

```javascript
describe('Password generation edge cases', () => {
  test('handles minimum length', () => {
    const password = generatePassword({ length: 4, includeUpper: true, includeLower: true, includeNumbers: true, includeSymbols: true });
    expect(password).toHaveLength(4);
  });
  
  test('handles maximum length', () => {
    const password = generatePassword({ length: 128, includeUpper: true, includeLower: true, includeNumbers: true, includeSymbols: true });
    expect(password).toHaveLength(128);
  });
  
  test('throws on length below minimum', () => {
    expect(() => generatePassword({ length: 3 }))
      .toThrow('Length must be between 4 and 128');
  });
});
```

## Documentation for Testing

- Add JSDoc comments indicating expected behavior
- Document edge cases
- Include example usage

```javascript
/**
 * Generates a secure random password based on provided options.
 * 
 * @param {Object} options - Password generation options
 * @param {number} options.length - Password length (4-128 characters)
 * @param {boolean} options.includeUpper - Include uppercase letters (A-Z)
 * @param {boolean} options.includeLower - Include lowercase letters (a-z)
 * @param {boolean} options.includeNumbers - Include numbers (0-9)
 * @param {boolean} options.includeSymbols - Include symbols (!@#$...)
 * 
 * @returns {string} Generated password
 * 
 * @throws {PasswordValidationError} If length is out of range (4-128)
 * @throws {PasswordValidationError} If no character types are selected
 * 
 * @example
 * const password = generatePassword({
 *   length: 16,
 *   includeUpper: true,
 *   includeLower: true,
 *   includeNumbers: true,
 *   includeSymbols: false
 * });
 * // Returns: "aB3dEfGh1JkLmN9P" (example)
 */
function generatePassword(options) {
  // Implementation
}
```

## Quality Checklist for Testability

Before finalizing code:

- [ ] Business logic separated from UI logic
- [ ] Functions are pure when possible
- [ ] Dependencies injected, not hardcoded
- [ ] Specific error types with clear messages
- [ ] State is explicit and observable
- [ ] `data-testid` attributes on testable elements
- [ ] Functions have single responsibility
- [ ] External dependencies abstracted (can be mocked)
- [ ] Edge cases considered and documented
- [ ] JSDoc comments explain expected behavior
