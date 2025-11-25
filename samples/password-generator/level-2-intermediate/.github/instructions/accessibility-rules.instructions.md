---
description: Accessibility standards (WCAG 2.1 AA) for password generator
applyTo: '**/*.html, **/*.css, **/*.js'
---

# Accessibility Standards (WCAG 2.1 AA)

Apply these accessibility rules when generating or modifying any code for the password generator web app.

## Perceivable - Information must be presentable to users in ways they can perceive

### Semantic HTML

- **ALWAYS** use semantic HTML elements over generic divs
- Use `<main>` for main content area
- Use `<button>` for interactive actions (not `<div>` or `<a>` without href)
- Use `<input>` with proper type attribute
- Use `<label>` elements associated with form controls

```html
<!-- Good -->
<main>
  <h1>Password Generator</h1>
  <form id="password-form">
    <label for="password-length">Password Length:</label>
    <input type="number" id="password-length" min="4" max="128" value="12">
    
    <button type="button" id="generate-btn">Generate Password</button>
  </form>
</main>

<!-- Bad -->
<div class="main">
  <span class="title">Password Generator</span>
  <div class="form">
    Password Length: <input type="text" id="length">
    <div onclick="generate()">Generate</div>  <!-- Not keyboard accessible -->
  </div>
</div>
```

### Text Alternatives

- Provide alt text for all informative images
- Use `aria-label` for icon-only buttons
- Use `aria-describedby` to associate help text with inputs
- Use visually-hidden text for screen readers when needed

```html
<!-- Good -->
<button id="copy-btn" aria-label="Copy password to clipboard">
  <svg aria-hidden="true"><!-- icon --></svg>
</button>

<input 
  type="number" 
  id="password-length"
  aria-describedby="length-help"
>
<span id="length-help">Choose between 4 and 128 characters</span>

<!-- Bad -->
<button id="copy-btn">
  <img src="copy.png">  <!-- Missing alt text or aria-label -->
</button>
```

### Color Contrast

- **Text**: Minimum 4.5:1 contrast ratio (WCAG AA)
- **Large text** (18pt/24px+): Minimum 3:1 contrast ratio
- **Interactive elements**: Minimum 3:1 contrast for focus indicators
- **Never** rely on color alone to convey information

```css
/* Good - Dark theme with sufficient contrast */
:root {
  --bg-primary: #1a1a1a;      /* Background */
  --text-primary: #ffffff;     /* White on dark: 17.9:1 ✓ */
  --text-secondary: #b0b0b0;   /* Light gray on dark: 7.8:1 ✓ */
  --accent: #4a9eff;           /* Blue on dark: 5.6:1 ✓ */
  --error: #ff6b6b;            /* Red on dark: 4.7:1 ✓ */
  --success: #51cf66;          /* Green on dark: 5.2:1 ✓ */
}

/* Bad - Insufficient contrast */
.text {
  color: #808080;  /* Gray on dark background: 2.5:1 ✗ */
}
```

### Visual Information

- Provide text labels in addition to icons
- Use icons + text for better comprehension
- Ensure error states use more than just color (icon + text)

```html
<!-- Good - Error state with icon + text + color -->
<div class="error-message" role="alert">
  <svg aria-hidden="true"><!-- error icon --></svg>
  <span>Please select at least one character type</span>
</div>

<!-- Bad - Color only -->
<div style="color: red;">Error</div>  <!-- Color alone not sufficient -->
```

## Operable - Interface components must be operable

### Keyboard Navigation

- **ALL** interactive elements must be keyboard accessible
- Ensure logical tab order (use tabindex="0" only when needed)
- Never use `tabindex` values greater than 0
- Provide visible focus indicators for all focusable elements
- Support standard keyboard shortcuts (Enter, Space for buttons)

```css
/* Good - Visible focus indicator */
button:focus-visible,
input:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

/* Alternative with box-shadow */
button:focus-visible {
  outline: none;  /* Only if providing alternative */
  box-shadow: 0 0 0 3px var(--accent);
}

/* Bad - No focus indicator */
button:focus {
  outline: none;  /* Never remove without replacement */
}
```

### Focus Management

- Maintain logical focus order (top to bottom, left to right)
- Don't trap focus unless in a modal (then manage it properly)
- Return focus to trigger element when closing overlays
- Skip links for keyboard users (if navigation is complex)

```javascript
// Good - Focus management for modal/dialog
function openDialog() {
  const dialog = document.querySelector('#dialog');
  const firstFocusable = dialog.querySelector('button, input, [tabindex="0"]');
  
  dialog.showModal();  // Native dialog handles focus trap
  firstFocusable?.focus();
}

function closeDialog() {
  const dialog = document.querySelector('#dialog');
  const triggerButton = document.querySelector('#open-dialog-btn');
  
  dialog.close();
  triggerButton.focus();  // Return focus
}
```

### Touch Targets

- Minimum touch target size: **44x44 pixels** (WCAG 2.5.5)
- Ensure adequate spacing between interactive elements
- Avoid requiring precise gestures

```css
/* Good - Adequate touch targets */
button,
input[type="checkbox"] {
  min-width: 44px;
  min-height: 44px;
  padding: 0.75rem 1.5rem;
}

/* Increase checkbox click area with padding on label */
label {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem;
  cursor: pointer;
}
```

### Timing

- Don't use time limits unless absolutely necessary
- If timed, provide option to extend or disable
- For this password generator: no timing concerns

## Understandable - Information and operation must be understandable

### Form Labels & Instructions

- Provide clear, descriptive labels for all form inputs
- Associate labels with inputs using `for` attribute
- Provide help text for complex inputs
- Mark required fields (visually and programmatically)

```html
<!-- Good -->
<div class="form-field">
  <label for="password-length">
    Password Length <span aria-label="required">*</span>
  </label>
  <input 
    type="number" 
    id="password-length" 
    min="4" 
    max="128" 
    value="12"
    required
    aria-describedby="length-help"
  >
  <small id="length-help">Choose between 4 and 128 characters</small>
</div>

<!-- Bad -->
<div>
  Length: <input type="number">  <!-- No label association -->
</div>
```

### Error Identification & Recovery

- Identify errors clearly (text + location)
- Provide suggestions for fixing errors
- Use `role="alert"` for important messages
- Don't rely only on color to indicate errors

```html
<!-- Good - Error with clear identification and suggestion -->
<div class="form-field error">
  <label for="password-length">Password Length</label>
  <input 
    type="number" 
    id="password-length" 
    value="2"
    aria-invalid="true"
    aria-describedby="length-error"
  >
  <div id="length-error" role="alert" class="error-message">
    <svg aria-hidden="true"><!-- error icon --></svg>
    <span>Password length must be at least 4 characters. Please enter a value between 4 and 128.</span>
  </div>
</div>
```

### Predictable Behavior

- Navigation and functionality should be consistent
- Don't trigger actions on focus alone (use click/submit)
- Provide clear feedback for user actions
- Buttons should clearly indicate their purpose

```html
<!-- Good - Clear button labels -->
<button type="button" id="generate-btn">Generate Password</button>
<button type="button" id="copy-btn" aria-label="Copy password to clipboard">
  <svg aria-hidden="true"><!-- copy icon --></svg>
  <span>Copy</span>
</button>

<!-- Bad - Unclear labels -->
<button>Go</button>
<button>OK</button>
```

## Robust - Content must be robust enough for various user agents

### Valid HTML

- Use valid HTML5 (no unclosed tags, proper nesting)
- Ensure unique IDs
- Use ARIA attributes correctly
- Validate with W3C validator

```html
<!-- Good -->
<div class="checkbox-group" role="group" aria-labelledby="charset-legend">
  <span id="charset-legend">Character Types</span>
  
  <label for="include-uppercase">
    <input type="checkbox" id="include-uppercase" checked>
    Uppercase Letters (A-Z)
  </label>
  
  <label for="include-lowercase">
    <input type="checkbox" id="include-lowercase" checked>
    Lowercase Letters (a-z)
  </label>
</div>
```

### ARIA Usage

- Use ARIA to enhance, not replace, semantic HTML
- Only use ARIA when no native HTML alternative exists
- Test with screen readers (NVDA, JAWS, VoiceOver)
- Common ARIA patterns:

```html
<!-- Live regions for dynamic updates -->
<div role="status" aria-live="polite" aria-atomic="true">
  Password generated successfully
</div>

<div role="alert" aria-live="assertive">
  Error: Please select at least one character type
</div>

<!-- Disabled state -->
<button disabled aria-disabled="true">Generate Password</button>

<!-- Hidden from screen readers -->
<svg aria-hidden="true"><!-- decorative icon --></svg>
```

### Screen Reader Support

- Provide text alternatives for visual information
- Use `aria-label` or `aria-labelledby` for non-text content
- Announce dynamic content changes with `aria-live`
- Test with actual screen readers

```javascript
// Good - Announce password generation to screen readers
function displayPassword(password) {
  const display = document.querySelector('#password-display');
  const announcement = document.querySelector('#sr-announcement');
  
  display.textContent = password;
  
  // Announce to screen readers
  announcement.textContent = `New password generated: ${password}`;
  
  // Clear announcement after delay
  setTimeout(() => {
    announcement.textContent = '';
  }, 1000);
}
```

```html
<div id="sr-announcement" role="status" aria-live="polite" class="visually-hidden"></div>
```

## Utility Classes for Accessibility

```css
/* Visually hidden but available to screen readers */
.visually-hidden {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  padding: 0;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}

/* Skip to main content link */
.skip-link {
  position: absolute;
  top: -40px;
  left: 0;
  background: var(--bg-primary);
  color: var(--text-primary);
  padding: 0.5rem 1rem;
  text-decoration: none;
  z-index: 100;
}

.skip-link:focus {
  top: 0;
}
```

## Testing Checklist

Before finalizing code, verify:

- [ ] All interactive elements keyboard accessible
- [ ] All form inputs have associated labels
- [ ] Color contrast meets WCAG AA (4.5:1)
- [ ] Focus indicators visible on all interactive elements
- [ ] Touch targets minimum 44x44px
- [ ] Error messages clear and helpful
- [ ] Dynamic content announced to screen readers
- [ ] Valid HTML (no errors in validator)
- [ ] Tested with keyboard only (no mouse)
- [ ] Tested with screen reader (NVDA/JAWS/VoiceOver)
- [ ] All icons have text alternatives or aria-labels
- [ ] No reliance on color alone for information
