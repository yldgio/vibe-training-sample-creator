---
name: deployment
description: Deployment workflow for password generator web applications. Use when deploying, configuring CI/CD, or preparing the application for production.
license: MIT
---

# Deployment Workflow

## When to Use
Use this skill when deploying the password generator application, setting up CI/CD pipelines, or preparing for production release.

## Pre-Deployment Checklist

1. **Build Verification**
   ```bash
   npm run build
   npm test
   npm run lint
   ```

2. **Security Audit**
   ```bash
   npm audit --audit-level=moderate
   ```

3. **Performance Check**
   - Bundle size under 50KB (gzipped)
   - Lighthouse score > 90

## Deployment Options

### Static Hosting (Recommended)
Password generators are client-side only - use static hosting:
- GitHub Pages
- Netlify
- Vercel
- Cloudflare Pages

### GitHub Pages Deployment
```bash
npm run build
npx gh-pages -d dist
```

### Netlify/Vercel
Connect repository and configure:
- Build command: `npm run build`
- Publish directory: `dist`

## Post-Deployment Verification
See [deploy script](./deploy-script.sh) for automated verification.

1. Verify application loads correctly
2. Test password generation works
3. Verify copy-to-clipboard works
4. Check browser console for errors
5. Validate HTTPS is enforced
