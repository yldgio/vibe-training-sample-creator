---
description: Basic One-Shot prompt for creating a password generator
---

# Password Generator

You are an expert web developer. Create a secure password generator web application using HTML, CSS, and JavaScript.
the HTML, CSS, and JavaScript should be in separate files.

**Requirements:**
1.  **UI:** Clean, modern interface with a dark theme.
2.  **Functionality:**
    *   Input for password length (default 12).
    *   Checkboxes for uppercase, lowercase, numbers, and symbols.
    *   "Generate" button.
    *   "Copy to Clipboard" button.
3.  **Security:** Use `crypto.getRandomValues()` for random number generation.
4. **File Structure:** Provide three separate files:
    *   `index.html` for HTML structure.
    *   `styles.css` for CSS styles.
    *   `script.js` for JavaScript functionality.
5. **Ensure Accessibility**: Use semantic HTML elements and ensure the application is accessible.

**Style Example:**
Please use a CSS style similar to this for the container:
```css
.container {
    max-width: 400px;
    margin: 2rem auto;
    padding: 2rem;
    background: #1a1a1a;
    border-radius: 12px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
    font-family: 'Inter', sans-serif;
    color: #ffffff;
}
```
