---
description: CSS coding standards and best practices for password generator
applyTo: '**/*.css, **/*.html'
---

# CSS Development Standards

Apply these standards when generating or modifying CSS code for the password generator web app.

## Organization & Architecture

- Use embedded `<style>` tags in the HTML file for this single-page app
- Organize CSS in logical sections: reset, variables, layout, components, utilities
- Follow mobile-first approach with `min-width` media queries
- Use CSS custom properties (variables) for theming and consistency

## Naming Conventions

- Use kebab-case for class names (e.g., `.password-display`, `.generate-button`)
- Use semantic names based on purpose, not appearance (e.g., `.primary-action` not `.blue-button`)
- Prefix component-specific classes with component name (e.g., `.password-generator-container`)
- Use BEM methodology for complex components: `.block__element--modifier`

## Dark Theme Implementation

- Define color palette using CSS custom properties in `:root`
- Ensure minimum contrast ratio of 4.5:1 for normal text (WCAG AA)
- Ensure minimum contrast ratio of 7:1 for large text (WCAG AAA)
- Support `prefers-color-scheme: light` as fallback
- Example palette:

```css
:root {
  --bg-primary: #1a1a1a;
  --bg-secondary: #2d2d2d;
  --text-primary: #ffffff;
  --text-secondary: #b0b0b0;
  --accent-primary: #4a9eff;
  --accent-hover: #357abd;
  --error: #ff5555;
  --success: #50fa7b;
}
```

## Responsive Design

- Use relative units (rem, em, %) over fixed pixels
- Base font-size: 16px (1rem)
- Implement fluid typography with `clamp()` when appropriate
- Breakpoints:
  - Mobile: 320px - 639px (default, mobile-first)
  - Tablet: 640px - 1023px
  - Desktop: 1024px+
- Test at minimum viewport width of 320px

## Layout & Spacing

- Use CSS Grid or Flexbox for layout (prefer Grid for main structure)
- Implement consistent spacing scale (4px, 8px, 12px, 16px, 24px, 32px, 48px)
- Use CSS custom properties for spacing: `--space-xs: 0.25rem;` (4px)
- Maintain vertical rhythm with consistent line-height (1.5 for body, 1.2 for headings)

## Typography

- Use system font stack for performance:

```css
font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 
             'Helvetica Neue', Arial, sans-serif;
```

- Font sizes: `--font-sm: 0.875rem;` (14px), `--font-base: 1rem;` (16px), `--font-lg: 1.125rem;` (18px)
- Font weights: 400 (normal), 500 (medium), 700 (bold)
- Limit to 2-3 font weights maximum

## Component Styling

### Buttons

- Minimum touch target: 44x44px (WCAG 2.5.5)
- Visible focus indicator (outline or box-shadow)
- Hover and active states clearly distinguishable
- Disabled state with reduced opacity and cursor: not-allowed

### Inputs

- Clear visual boundary (border)
- Adequate padding (at least 0.5rem vertical, 0.75rem horizontal)
- Visible focus state
- Error states with color + icon/text (not color alone)

### Containers

- Border-radius: 8px-12px for modern look
- Box-shadow for depth: `0 4px 6px rgba(0, 0, 0, 0.3)` for dark theme
- Maximum width constraint for readability (400px-600px for forms)

## Accessibility

- Never rely solely on color to convey information
- Provide visible focus indicators for all interactive elements
- Use `outline-offset` for better focus visibility: `outline-offset: 2px;`
- Support keyboard navigation with :focus-visible
- Implement skip links if navigation is complex
- Ensure sufficient color contrast (use browser DevTools to verify)

## Performance

- Minimize selector specificity (avoid deep nesting)
- Avoid `!important` unless absolutely necessary
- Use shorthand properties: `margin`, `padding`, `border`
- Minimize use of expensive properties: `box-shadow`, `filter`, `transform` (use sparingly)
- Avoid layout thrashing with batch CSS changes

## Motion & Animation

- Respect `prefers-reduced-motion` media query:

```css
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

- Use subtle transitions for interactive feedback (200ms-300ms)
- Avoid animating layout properties (width, height) - prefer transform/opacity

## Browser Support

- Target evergreen browsers (Chrome, Firefox, Safari, Edge latest 2 versions)
- Use autoprefixer if needed (though modern CSS features are widely supported)
- Provide fallbacks for CSS custom properties if supporting older browsers

## Example Structure

```css
/* Reset & Base */
*, *::before, *::after { box-sizing: border-box; }
body { margin: 0; font-family: var(--font-family); }

/* CSS Variables */
:root { /* custom properties */ }

/* Layout */
.container { /* main container styles */ }

/* Components */
.password-display { /* component styles */ }
.generate-button { /* component styles */ }

/* Utilities */
.visually-hidden { /* accessibility helper */ }

/* Media Queries */
@media (min-width: 640px) { /* tablet styles */ }
```

## Quality Checklist

Before finalizing CSS:

- [ ] All colors meet WCAG contrast requirements
- [ ] All interactive elements have visible focus states
- [ ] Layout tested at 320px, 768px, 1024px widths
- [ ] `prefers-reduced-motion` respected
- [ ] No unused CSS rules
- [ ] Consistent spacing and typography scale applied
