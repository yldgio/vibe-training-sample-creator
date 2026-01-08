---
name: security-validation
description: Comprehensive security validation for password generator applications. Use when auditing, implementing, or reviewing security measures for password handling and generation.
license: MIT
---

# Security Validation for Password Generators

## When to Use
Use this skill for comprehensive security audits, implementing security measures, or reviewing code for security vulnerabilities in password generation applications.

## Security Audit Process

### 1. Randomness Audit
Verify cryptographically secure random number generation:
- ✅ Use `crypto.getRandomValues()` (Web) or `crypto.randomBytes()` (Node.js)
- ❌ Never use `Math.random()` - it's predictable

### 2. Memory Security
- Clear passwords from memory after use
- Avoid storing in global/window scope
- Don't persist passwords to localStorage/sessionStorage

### 3. XSS Prevention
- Escape all user inputs before display
- Use textContent instead of innerHTML for password display
- Implement Content Security Policy

### 4. Dependency Audit
```bash
npm audit
npm audit fix
```

## Security Checklist
See the [security checklist](./security-checklist.md) for a complete validation list.

## Automated Validation
```bash
# Check for insecure random usage
grep -rn "Math.random" src/

# Check for console.log with passwords
grep -rn "console.log.*password" src/

# Check for innerHTML usage
grep -rn "innerHTML" src/

# Run security audit
npm audit --audit-level=moderate
```

## Reporting
Document any security findings with:
1. Severity (Critical/High/Medium/Low)
2. Location (file and line number)
3. Description of vulnerability
4. Recommended fix
