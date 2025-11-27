---
description: Security best practices for password generator application
applyTo: '**/*.js,**/*.html'
---

# Security Best Practices

Apply these security standards when generating code for the password generator.

## Secure Randomness

- **ALWAYS** use `crypto.getRandomValues()` for password generation
- **NEVER** use `Math.random()` for security-sensitive operations
- Ensure sufficient entropy by using Uint32Array buffers

```javascript
// Good - Secure random
function getSecureRandomInt(max) {
  const buffer = new Uint32Array(1);
  crypto.getRandomValues(buffer);
  return buffer[0] % max;
}

// Bad - Insecure
const index = Math.floor(Math.random() * max);
```

## Input Validation

- Validate all user inputs on the client side
- Use type coercion carefully (`parseInt`, `Number`)
- Enforce minimum and maximum bounds
- Sanitize inputs before using in any operation

## XSS Prevention

- Use `textContent` instead of `innerHTML` for text updates
- Never interpolate user input into HTML strings
- Escape any dynamic content if HTML insertion is required

```javascript
// Good - Safe text update
element.textContent = password;

// Bad - XSS vulnerability
element.innerHTML = password;
```

## Error Handling

- Never expose stack traces to users
- Use generic error messages for display
- Log detailed errors only to console.error
- Don't leak sensitive information in error messages

## Clipboard Security

- Clear clipboard after a reasonable timeout (optional)
- Handle clipboard API failures gracefully
- Use the modern Clipboard API with async/await
