# Password Generator Development Guide

You are an expert web developer creating a secure password generator web application using HTML, CSS, and JavaScript.

## Architecture Overview
- **Single-page app**: HTML structure, embedded CSS, vanilla JavaScript
- **No build process**: Edit files directly, test in browser
- **Dark theme by default**: High contrast design meeting WCAG 2.1 AA standards
- **Responsive**: Mobile-first with breakpoints at 640px and 1024px

## Key Conventions & Standards

### Accessibility (WCAG 2.1 AA)
- Use semantic HTML: `<main>`, `<button>`, `<label>`, `<input>`
- Associate labels with `for` attribute: `<label for="length">Length:</label><input id="length">`
- Minimum 44x44px touch targets: `min-width: 44px; min-height: 44px;`
- Visible focus indicators: `button:focus-visible { outline: 2px solid #4a9eff; }`
- Color contrast 4.5:1 minimum: `--text-primary: #ffffff; --bg-primary: #1a1a1a;`
- Reference: `.github/instructions/accessibility-rules.instructions.md`

### CSS Standards
- CSS custom properties for theming: `:root { --bg-primary: #1a1a1a; --accent: #4a9eff; }`
- Kebab-case classes: `.password-display`, `.generate-button`
- Mobile-first responsive: default mobile, `@media (min-width: 640px)` for tablet+
- Spacing scale: `--space-sm: 0.5rem; --space-md: 1rem; --space-lg: 1.5rem;`
- Reference: `.github/instructions/css-standards.instructions.md`

### JavaScript Patterns
- ES6+ features: `const/let`, arrow functions, destructuring
- Pure functions for logic: `function generatePassword(options) { /* no DOM */ }`
- Secure randomness: `crypto.getRandomValues()` never `Math.random()`
- Error handling: `throw new Error('Password length must be 4-128')`
- Event delegation: `document.addEventListener('click', handleClick)`
- Reference: `.github/instructions/javascript-patterns.instructions.md`

### Testability Design
- Separate business logic from UI: pure functions for password generation
- Dependency injection: pass charsets as parameters
- `data-testid` attributes: `<button data-testid="generate-button">`
- Specific error types: `class PasswordValidationError extends Error`
- Reference: `.github/instructions/testability-guidelines.instructions.md`

## Development Workflow
- Edit `index.html` for structure, embedded `<style>` for CSS, `<script>` for JS
- Test in browser: open `index.html` directly or use Live Server extension
- Validate accessibility: Use browser dev tools contrast checker
- Debug JS: Console logging for errors, breakpoints for logic

## Specific Patterns

### Password Generation
```javascript
const charsets = {
  uppercase: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
  lowercase: 'abcdefghijklmnopqrstuvwxyz',
  numbers: '0123456789',
  symbols: '!@#$%^&*()_+-=[]{}|;:,.<>?'
};

function generatePassword({ length = 12, includeUpper = true, includeLower = true, includeNumbers = true, includeSymbols = true }) {
  let charset = '';
  if (includeUpper) charset += charsets.uppercase;
  if (includeLower) charset += charsets.lowercase;
  if (includeNumbers) charset += charsets.numbers;
  if (includeSymbols) charset += charsets.symbols;
  
  let password = '';
  for (let i = 0; i < length; i++) {
    const randomBuffer = new Uint32Array(1);
    crypto.getRandomValues(randomBuffer);
    password += charset[randomBuffer[0] % charset.length];
  }
  return password;
}
```

### Form Handling
```javascript
const form = document.querySelector('#password-form');
form.addEventListener('submit', (e) => {
  e.preventDefault();
  const options = {
    length: parseInt(document.querySelector('#length').value),
    includeUpper: document.querySelector('#upper').checked,
    // ... other options
  };
  try {
    const password = generatePassword(options);
    document.querySelector('#display').textContent = password;
  } catch (error) {
    showError(error.message);
  }
});
```

### Clipboard Copy
```javascript
async function copyToClipboard(text) {
  try {
    await navigator.clipboard.writeText(text);
    showSuccess('Copied!');
  } catch {
    // Fallback for older browsers
    const textarea = document.createElement('textarea');
    textarea.value = text;
    document.body.appendChild(textarea);
    textarea.select();
    document.execCommand('copy');
    document.body.removeChild(textarea);
    showSuccess('Copied!');
  }
}
```

## Quality Checks
- [ ] All interactive elements keyboard accessible
- [ ] Password uses `crypto.getRandomValues()` 
- [ ] Color contrast meets WCAG AA
- [ ] Touch targets minimum 44px
- [ ] Functions separated: UI vs business logic
- [ ] No `var`, only `const/let`
- [ ] Error cases handled with user feedback