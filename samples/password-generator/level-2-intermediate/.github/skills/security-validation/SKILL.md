---
name: security-validation
description: Security validation for password generator applications. Use when reviewing or implementing security measures for password handling.
---

# Security Validation for Password Generators

## When to Use
Use this skill when implementing, reviewing, or auditing security measures for password generation and handling.

## Security Checklist

1. **Randomness**
   - Use cryptographically secure random number generation (`crypto.getRandomValues()`)
   - Never use `Math.random()` for password generation

2. **Memory Handling**
   - Avoid storing generated passwords in global variables
   - Clear password from memory after copy operation
   - Don't log passwords to console in production

3. **Client-Side Security**
   - Passwords should never be transmitted to a server
   - Use HTTPS if any network operations occur
   - Implement Content Security Policy headers

4. **Input Validation**
   - Validate password length is within acceptable bounds (1-128 characters)
   - Sanitize all user inputs
   - Prevent XSS in password display

## Validation Commands
```bash
# Check for console.log statements with sensitive data
grep -r "console.log.*password" src/

# Verify crypto API usage
grep -r "Math.random" src/  # Should return no results
```
