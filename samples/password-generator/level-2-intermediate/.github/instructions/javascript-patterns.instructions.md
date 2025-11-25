---
description: JavaScript coding patterns and best practices for password generator
applyTo: '**/*.js, **/*.html'
---

# JavaScript Development Guidelines

Apply these patterns when generating or modifying JavaScript code for the password generator web app.

## Code Organization

- Use ES6+ features (const/let, arrow functions, template literals, destructuring)
- Organize code in logical sections: constants, state, utilities, event handlers, initialization
- Group related functions together
- Use comments to separate major sections

## Variable Declaration

- **ALWAYS** use `const` by default
- Use `let` only when reassignment is necessary
- **NEVER** use `var`
- Declare variables at the narrowest scope possible
- Initialize variables at declaration when possible

```javascript
// Good
const DEFAULT_LENGTH = 12;
const charsets = {
  uppercase: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
  lowercase: 'abcdefghijklmnopqrstuvwxyz',
  numbers: '0123456789',
  symbols: '!@#$%^&*()_+-=[]{}|;:,.<>?'
};

// Bad
var length = 12;  // Don't use var
let CHARSETS = { ... };  // Don't use let for constants
```

## Naming Conventions

- **camelCase** for variables and functions: `generatePassword`, `passwordLength`
- **UPPER_SNAKE_CASE** for constants: `DEFAULT_LENGTH`, `MIN_LENGTH`, `MAX_LENGTH`
- **PascalCase** for classes (if used): `PasswordGenerator`
- Use descriptive, intention-revealing names
- Avoid abbreviations unless universally understood (e.g., `btn` → `button`)

```javascript
// Good
const passwordLength = 12;
function generatePassword(options) { }

// Bad
const pwdLen = 12;  // Unclear abbreviation
function gen(opts) { }  // Too terse
```

## Function Design

- Keep functions small and focused (single responsibility)
- Prefer pure functions (no side effects) for utilities
- Return early to avoid deep nesting
- Use default parameters instead of manual checks
- Limit function parameters to 3-4 (use object parameter for more)

```javascript
// Good
function generatePassword({ length = 12, includeUpper = true, includeLower = true, includeNumbers = true, includeSymbols = true } = {}) {
  if (length < 4) {
    throw new Error('Password length must be at least 4');
  }
  // Implementation
}

// Bad
function generatePassword(length, upper, lower, nums, syms) {
  if (!length) length = 12;  // Use default parameters instead
  if (upper === undefined) upper = true;
  // Too many parameters
}
```

## Secure Random Generation

- **ALWAYS** use `crypto.getRandomValues()` for password generation
- **NEVER** use `Math.random()` for security-sensitive operations
- Handle browser compatibility gracefully

```javascript
// Good - Secure random generation
function getRandomInt(max) {
  const randomBuffer = new Uint32Array(1);
  crypto.getRandomValues(randomBuffer);
  return randomBuffer[0] % max;
}

// Bad - Insecure
function getRandomInt(max) {
  return Math.floor(Math.random() * max);  // NOT cryptographically secure
}
```

## Error Handling

- Validate input at function boundaries
- Throw descriptive errors for invalid input
- Use try-catch for operations that can fail
- Provide user-friendly error messages in UI
- Log errors to console for debugging

```javascript
// Good
function generatePassword(options) {
  const { length } = options;
  
  if (typeof length !== 'number' || length < 4 || length > 128) {
    throw new Error('Password length must be between 4 and 128');
  }
  
  if (!options.includeUpper && !options.includeLower && 
      !options.includeNumbers && !options.includeSymbols) {
    throw new Error('At least one character type must be selected');
  }
  
  // Implementation
}

// Handle errors in event handlers
button.addEventListener('click', () => {
  try {
    const password = generatePassword(getOptions());
    displayPassword(password);
  } catch (error) {
    showError(error.message);
    console.error('Password generation failed:', error);
  }
});
```

## Event Handling

- Use `addEventListener` (never inline onclick attributes)
- Delegate events when appropriate
- Remove event listeners if needed (store reference)
- Prevent default behavior explicitly when needed
- Use named functions for complex handlers (easier to debug)

```javascript
// Good
const generateButton = document.querySelector('#generate-btn');
generateButton.addEventListener('click', handleGenerateClick);

function handleGenerateClick(event) {
  event.preventDefault();
  // Handle click
}

// Bad
<button onclick="generate()">Generate</button>  // Avoid inline handlers
```

## DOM Manipulation

- Cache DOM references (don't query repeatedly)
- Use `querySelector`/`querySelectorAll` over older methods
- Batch DOM updates to minimize reflows
- Use `textContent` for text (not `innerHTML` unless HTML is needed)
- Sanitize any user input before rendering

```javascript
// Good - Cache references
const passwordDisplay = document.querySelector('#password-display');
const lengthInput = document.querySelector('#length-input');
const generateButton = document.querySelector('#generate-btn');

function displayPassword(password) {
  passwordDisplay.textContent = password;  // Secure for text content
}

// Bad - Repeated queries
function displayPassword(password) {
  document.querySelector('#password-display').innerHTML = password;  // XSS risk
}
```

## Async Patterns

- Use `async/await` for clipboard operations
- Handle promise rejections with try-catch
- Provide feedback for async operations (loading states)

```javascript
// Good
async function copyToClipboard(text) {
  try {
    await navigator.clipboard.writeText(text);
    showSuccess('Password copied to clipboard!');
  } catch (error) {
    console.error('Copy failed:', error);
    showError('Failed to copy password. Please copy manually.');
  }
}

// Alternative fallback for older browsers
function copyToClipboardFallback(text) {
  const textarea = document.createElement('textarea');
  textarea.value = text;
  textarea.style.position = 'fixed';
  textarea.style.opacity = '0';
  document.body.appendChild(textarea);
  textarea.select();
  
  try {
    document.execCommand('copy');
    showSuccess('Password copied!');
  } catch (error) {
    showError('Copy failed. Please copy manually.');
  } finally {
    document.body.removeChild(textarea);
  }
}
```

## State Management

- Keep state minimal and explicit
- Use single source of truth for each piece of state
- Update state immutably when possible
- Derive values from state rather than storing separately

```javascript
// Good
const state = {
  length: 12,
  options: {
    includeUpper: true,
    includeLower: true,
    includeNumbers: true,
    includeSymbols: true
  },
  generatedPassword: ''
};

function updateLength(newLength) {
  state.length = newLength;
  renderLengthDisplay();
}

// Bad - Redundant state
let length = 12;
let displayedLength = '12';  // Redundant - derive from length
```

## Code Comments

- Use comments to explain **why**, not **what**
- Document complex algorithms or non-obvious decisions
- Keep comments up-to-date with code changes
- Use JSDoc for function documentation when helpful

```javascript
/**
 * Generates a secure random password based on provided options.
 * Uses crypto.getRandomValues() for cryptographic randomness.
 * 
 * @param {Object} options - Password generation options
 * @param {number} options.length - Password length (4-128)
 * @param {boolean} options.includeUpper - Include uppercase letters
 * @param {boolean} options.includeLower - Include lowercase letters
 * @param {boolean} options.includeNumbers - Include numbers
 * @param {boolean} options.includeSymbols - Include symbols
 * @returns {string} Generated password
 * @throws {Error} If options are invalid
 */
function generatePassword(options) {
  // Implementation
}
```

## Performance

- Avoid premature optimization (prioritize readability)
- Cache computed values when appropriate
- Use event delegation for multiple similar elements
- Debounce/throttle high-frequency events if needed

## Browser Compatibility

- Target modern evergreen browsers (Chrome, Firefox, Safari, Edge)
- Use feature detection, not browser detection
- Provide graceful fallbacks for newer APIs (e.g., clipboard)

```javascript
// Good - Feature detection
if (navigator.clipboard && navigator.clipboard.writeText) {
  // Use modern clipboard API
} else {
  // Use fallback method
}

// Bad - Browser detection
if (navigator.userAgent.includes('Chrome')) { }  // Fragile
```

## Quality Checklist

Before finalizing JavaScript:

- [ ] All variables use const/let (no var)
- [ ] Cryptographic randomness used (crypto.getRandomValues)
- [ ] All user inputs validated
- [ ] Error handling implemented for all operations
- [ ] Event listeners properly attached
- [ ] DOM references cached
- [ ] Async operations handle errors
- [ ] Code is readable and well-commented
- [ ] Functions are small and focused
- [ ] No console.log statements in production code (only console.error for errors)
