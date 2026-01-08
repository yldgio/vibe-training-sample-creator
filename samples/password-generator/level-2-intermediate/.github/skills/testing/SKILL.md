---
name: password-generator-testing
description: Guide for testing password generator functionality. Use when creating or running unit tests for password generation, validation, or strength checking.
---

# Password Generator Testing

## When to Use
Use this skill when you need to test password generation, validation, or strength-checking functionality.

## Testing Guidelines

1. **Unit Test Structure**
   - Test each password option independently (length, uppercase, lowercase, numbers, symbols)
   - Test edge cases: minimum length (1), maximum length, empty options
   - Test randomness: generate multiple passwords and verify they differ

2. **Test Cases to Include**
   - Password meets specified length
   - Password contains required character types
   - Password excludes disabled character types
   - Strength meter returns correct rating
   - Copy-to-clipboard functionality works

3. **Running Tests**
   ```bash
   # For JavaScript projects
   npm test
   
   # With coverage
   npm test -- --coverage
   ```

## Example Test
```javascript
test('generates password with correct length', () => {
  const password = generatePassword({ length: 16 });
  expect(password.length).toBe(16);
});
```
