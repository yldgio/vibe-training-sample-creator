# Vibe Coding Training Sample Creator

This repository generates **Vibe Coding** training samples using declarative AI agents. The core "logic" lives in **agent definitions, prompts, and instructions** that guide an AI agent to generate prompt engineering examples at different complexity levels.

## Repository Purpose

The goal of this repo is to:

- **Generate prompt samples** for Vibe Coding training projects.
- Organize outputs by **project** (e.g. `password-generator`) and by **difficulty level** (basic, intermediate, advanced).
- Produce ready-to-use prompt files that can be **copied into training projects**.

## Folder Structure

```text
output/                      # Generated prompt samples (ignored by git)
  {project-name}/            # e.g. password-generator
    level-1-basic/
      README.md
      .github/
        prompts/
          *.prompt.md
    level-2-intermediate/
      README.md
      .github/
        prompts/
        instructions/
      copilot-instructions.md
    level-3-advanced/
      README.md
      .github/
        agents/
        prompts/
        instructions/
      copilot-instructions.md

samples/                     # Reference example (checked into git)
  password-generator/        # Shows expected output structure
    level-1-basic/
    level-2-intermediate/
    level-3-advanced/
```

### Folders Explained

| Folder | Purpose | Git Status |
|--------|---------|------------|
| `output/` | Generated prompt samples for your training projects. Copy contents to your target project. | **Ignored** (`.gitignore`) |
| `samples/` | Reference example showing expected output structure. | **Tracked** |

## Complexity Levels

Each project follows a three-level difficulty model:

### Level 1 – Basic

- One-shot prompts.
- Simple tasks, often single-file outputs.
- Great for introducing a concept (e.g. a basic password generator).

### Level 2 – Intermediate

- Few-shot prompting with explicit instructions.
- Focus on **predictability** through domain-specific instructions (CSS, JavaScript, accessibility, etc.).
- Separate instruction files for repeatable patterns.

### Level 3 – Advanced

- Chain-of-thought prompting with dynamic planning.
- Multi-agent orchestration using sub-agents.
- Tool usage, task handover, and complex workflows.

## Available Commands

This repo provides two main prompts to interact with the Sampler agent:

| Command | Description | Usage |
|---------|-------------|-------|
| `/initialize` | Create new training samples for a project | `/initialize password-generator web app` |
| `/update` | Update existing samples with latest best practices | `/update password-generator` |

## Workflow

### Step 1: Initialize a New Project

Use the `/initialize` prompt to create training samples for a new project:

1. Open VS Code in this repository
2. Open GitHub Copilot Chat
3. Type: `/initialize <project-description>`

**Example:**

```text
/initialize create a password generator web app with HTML, CSS, and JavaScript
```

The agent will:

1. Generate a short project name (e.g., `password-generator`)
2. Ask clarifying questions about requirements
3. Research best practices for prompt engineering
4. Create the folder structure in `output/{project-name}/`

### Step 2: Review Generated Samples

After generation, review the output:

```text
output/
  password-generator/
    level-1-basic/
      README.md
      .github/prompts/password-generator.prompt.md
    level-2-intermediate/
      README.md
      .github/prompts/...
      .github/instructions/...
      copilot-instructions.md
    level-3-advanced/
      README.md
      .github/agents/...
      .github/prompts/...
      .github/instructions/...
      copilot-instructions.md
```

### Step 3: Update Existing Samples

Use the `/update` prompt to refresh existing samples:

```text
/update password-generator
```

The agent will review and update prompts to align with current best practices.

### Step 4: Copy to Training Project

Copy the generated content to your target training project:

```powershell
# Copy a specific level to your training project
Copy-Item -Recurse output/password-generator/level-1-basic/.github/* C:\path\to\training-project\.github\
```

## Agent Architecture

```text
.github/
  agents/
    sampler.agent.md     # Main agent that generates training samples
  prompts/
    initialize.prompt.md # Creates new project samples
    update.prompt.md     # Updates existing samples
  copilot-instructions.md # Global context for this repo
```

### Sampler Agent (`sampler.agent.md`)

The core agent that:

- Researches prompt engineering best practices
- Asks clarifying questions about project requirements
- Generates structured prompt samples across all three complexity levels
- Creates proper folder structure aligned with GitHub Copilot conventions

### Prompts

| Prompt | Purpose |
|--------|---------|
| `initialize.prompt.md` | Entry point for creating new training samples |
| `update.prompt.md` | Entry point for updating existing samples |

## File Naming Conventions

| Type | Location | Pattern |
|------|----------|---------|
| Prompts | `.github/prompts/` | `*.prompt.md` |
| Instructions | `.github/instructions/` | `*.instructions.md` |
| Agents | `.github/agents/` | `*.agent.md` |
| Global Config | Root or `.github/` | `copilot-instructions.md` |

## Reference Samples

Check the `samples/` folder for example output structure:

- `samples/password-generator/level-1-basic/` – One-shot prompt example
- `samples/password-generator/level-2-intermediate/` – Instructions + few-shot prompts
- `samples/password-generator/level-3-advanced/` – Multi-agent orchestration

## Contributing

- Use branches and pull requests when editing or adding training projects.
- Keep prompts and instructions **small, focused, and well-commented**.
- Update `samples/` with representative examples when adding new project types.
