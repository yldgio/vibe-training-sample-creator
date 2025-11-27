---
description: Performance optimization best practices for password generator
applyTo: '**/*.js,**/*.css,**/*.html'
---

# Performance Best Practices

Apply these performance patterns when generating code for the password generator.

## DOM Optimization

- Cache DOM references at initialization
- Avoid querying DOM inside loops
- Batch DOM updates when possible
- Use `requestAnimationFrame` for visual updates if needed

```javascript
// Good - Cached reference
const passwordDisplay = document.querySelector('#password-display');
function updatePassword(pwd) {
  passwordDisplay.textContent = pwd;
}

// Bad - Repeated queries
function updatePassword(pwd) {
  document.querySelector('#password-display').textContent = pwd;
}
```

## Event Handling

- Use event delegation for multiple similar elements
- Debounce or throttle high-frequency events
- Remove event listeners when no longer needed
- Avoid attaching handlers in loops

## CSS Performance

- Avoid expensive CSS properties in animations (use transform/opacity)
- Minimize reflows by grouping style changes
- Use CSS custom properties for dynamic values
- Avoid universal selectors at root level

```css
/* Good - GPU-accelerated animation */
.button:hover {
  transform: scale(1.05);
}

/* Bad - Causes layout reflow */
.button:hover {
  width: 105%;
}
```

## JavaScript Efficiency

- Use `const` and `let` (block-scoped, better optimization)
- Avoid creating functions inside loops
- Prefer native methods over manual iteration
- Keep functions small and focused

## Asset Loading

- Inline critical CSS for small apps
- Defer non-critical JavaScript
- Minimize external dependencies (prefer vanilla JS)
