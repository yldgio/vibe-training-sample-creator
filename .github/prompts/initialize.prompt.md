---
agent: sampler
description: generates training samples: basic, intermediate, and advanced.
argument-hint: define the project name and requirements for the training samples.

---
## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Goal

You only generate the prompt samples, not the code.
Alway write a README.md for each level explaining the concept and task. 

## Outline

The text the user typed after the command is the project name and any specific requirements for the samples.
Given that project name, do this:
1. **Generate a concise short name** (2-4 words) for the project-name:
   - Analyze the feature description and extract the most meaningful keywords
   - Create a 2-4 word short name that captures the essence of the project
   - Preserve technical terms and acronyms (OAuth2, API, JWT, etc.)
   - Keep it concise but descriptive enough to understand the project at a glance
   - Examples:
     - "I want to add user authentication" → "user-auth"
     - "Implement OAuth2 integration for the API" → "oauth2-api-integration"
     - "Create a dashboard for analytics" → "analytics-dashboard"
     - "create a password generator web app" → "password-generator"

2. **Check for existing folders before creating new one**:
   - If `output/{{project-name}}/level-1-basic/` or `output/{{project-name}}/level-2-intermediate/` or `output/{{project-name}}/level-3-advanced/` already exists, do not create new samples. Instead, review and update existing samples to align with best practices.
   - If the folder does not exist, proceed to create the full folder structure and samples as described below.
3. **Create the folder structure**

