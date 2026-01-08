# Security Checklist for Password Generator

## Randomness
- [ ] Uses `crypto.getRandomValues()` or `crypto.randomBytes()`
- [ ] No usage of `Math.random()` for security-sensitive operations
- [ ] Entropy source is cryptographically secure

## Memory Handling
- [ ] Generated passwords not stored in global variables
- [ ] Passwords cleared from memory after copy operation
- [ ] No passwords in localStorage/sessionStorage
- [ ] No passwords logged to console in production

## Input Validation
- [ ] Password length validated (min: 1, max: 128)
- [ ] Character type options validated
- [ ] All user inputs sanitized

## XSS Prevention
- [ ] Password displayed using textContent (not innerHTML)
- [ ] User inputs escaped before rendering
- [ ] Content Security Policy implemented

## Network Security
- [ ] No password transmission to external servers
- [ ] HTTPS enforced if any network operations
- [ ] No third-party analytics tracking passwords

## Dependency Security
- [ ] `npm audit` shows no critical vulnerabilities
- [ ] Dependencies are up to date
- [ ] No unnecessary dependencies included

## Production Readiness
- [ ] Console.log statements removed or guarded
- [ ] Error messages don't expose sensitive info
- [ ] Source maps disabled in production
