---
name: "generate-styles"
description: "Create CSS styling following project standards"
---

# Prompt: Generate CSS Styles for Password Generator

Create the CSS styles for the password generator web application.

## Requirements

Follow all standards defined in:

- [CSS Standards](../instructions/css-standards.instructions.md)

## Style System

### 1. CSS Custom Properties (Variables)

Define in `:root`:

- Color palette (dark theme with WCAG AA contrast)
- Spacing scale (4px, 8px, 12px, 16px, 24px, 32px)
- Typography scale (font sizes, weights, line heights)
- Border radius values
- Transition durations

### 2. Reset & Base Styles

- Box-sizing reset
- Body defaults (font-family, background, color)
- Remove default margins/padding where needed

### 3. Layout Styles

- Main container: centered, max-width 400px, responsive padding
- Use CSS Grid or Flexbox for internal layout
- Responsive spacing that adapts to viewport

### 4. Component Styles

Style these components following CSS standards:

- **Headings**: Typography scale, proper hierarchy
- **Form controls**: Inputs, checkboxes with adequate sizing
- **Buttons**: Primary and secondary variants, hover/focus/active states
- **Password display**: Monospace font, clear visual boundary
- **Checkbox group**: Proper spacing, visual grouping
- **Error/success messages**: Color + icon, high visibility

### 5. Interactive States

For all interactive elements:

- Hover states (subtle color shift)
- Focus states (visible outline, 2px solid accent color, 2px offset)
- Active states (pressed appearance)
- Disabled states (reduced opacity, cursor: not-allowed)

### 6. Accessibility Features

- Focus indicators (never remove outline without replacement)
- Color contrast minimum 4.5:1 for text
- Touch targets minimum 44x44px
- `prefers-reduced-motion` support

### 7. Responsive Design

- Mobile-first approach
- Breakpoint at 640px for larger screens
- Fluid spacing and typography
- Test at 320px minimum width

## Output Format

Return CSS embedded in `<style>` tags with:

- Organized sections with comments
- CSS custom properties in `:root`
- Logical grouping (reset → variables → layout → components → utilities → media queries)
- BEM or semantic class naming
- No unused rules

The styles should create a modern, dark-themed interface that is accessible and visually appealing.
