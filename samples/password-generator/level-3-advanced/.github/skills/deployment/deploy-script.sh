#!/bin/bash
# Deployment verification script for Password Generator
# Run after deployment to verify the application is working correctly

set -e

DEPLOY_URL="${1:-https://your-app-url.com}"

echo "🚀 Verifying deployment at: $DEPLOY_URL"

# Check if site is accessible
echo "📡 Checking site accessibility..."
HTTP_STATUS=$(curl -s -o /dev/null -w "%{http_code}" "$DEPLOY_URL")
if [ "$HTTP_STATUS" -eq 200 ]; then
    echo "✅ Site is accessible (HTTP $HTTP_STATUS)"
else
    echo "❌ Site returned HTTP $HTTP_STATUS"
    exit 1
fi

# Check for HTTPS
echo "🔒 Checking HTTPS..."
if [[ "$DEPLOY_URL" == https://* ]]; then
    echo "✅ HTTPS is enabled"
else
    echo "⚠️  Warning: Site is not using HTTPS"
fi

# Check for required files
echo "📁 Checking for required files..."
for FILE in "index.html" "styles.css" "script.js"; do
    STATUS=$(curl -s -o /dev/null -w "%{http_code}" "$DEPLOY_URL/$FILE")
    if [ "$STATUS" -eq 200 ]; then
        echo "✅ $FILE found"
    else
        echo "⚠️  $FILE not found (HTTP $STATUS)"
    fi
done

# Check Content-Security-Policy header
echo "🛡️  Checking security headers..."
CSP=$(curl -s -I "$DEPLOY_URL" | grep -i "content-security-policy" || true)
if [ -n "$CSP" ]; then
    echo "✅ Content-Security-Policy header present"
else
    echo "⚠️  Content-Security-Policy header not found"
fi

echo ""
echo "🎉 Deployment verification complete!"
