# Copilot Instructions for Vibe Coding Training Sample Creator

This repository is dedicated to creating training samples for "Vibe Coding" using declarative AI agents. The core logic resides in agent definitions that generate prompt engineering examples across different complexity levels.

## 🏗 Project Architecture

- **Agent-Driven Generation**: The primary "code" in this repo consists of agent definitions (e.g., `.github/agents/sampler.agent.md`). These agents are designed to generate content.
- **Output Structure**: Generated samples are organized by project and complexity level:
  ```
  output/
    {{project-name}}/
      level-1-basic/
      level-2-intermediate/
      level-3-advanced/
  ```
- **Component Types**:
  - **Agents**: `.github/agents/*.agent.md` - Defines the AI agent persona, tools, and behavior.
  - **Prompts**: `.github/prompts/*.prompt.md` - Reusable prompt templates.
  - **Instructions**: `.github/instructions/*.instructions.md` - System-level instructions for agents.

## 📝 Conventions & Patterns

### Agent Definitions
- **Location**: `.github/agents/`
- **Format**: Markdown with YAML frontmatter.
- **Required Frontmatter**: `description`, `tools`.
- **Code Block**: Use ` ```chatagent ` to wrap the agent definition body if embedding in documentation, or just standard markdown for the file itself.

### Sample Generation Levels
When creating or analyzing training samples, strictly adhere to the three-level complexity framework:
1.  **Level 1 (Basic)**: One-shot prompting, simple tasks, single-file outputs.
2.  **Level 2 (Intermediate)**: Few-shot prompting, requirement analysis, separate instruction files.
3.  **Level 3 (Advanced)**: Chain of thought, dynamic planning, tool usage, sub-agents.

### File Naming & Locations
- **Prompts**: Must be placed in `.github/prompts/` within the relevant project/level folder. Use `*.prompt.md`.
- **Instructions**: Must be placed in `.github/instructions/` within the relevant project/level folder. Use `*.instructions.md`.
- **Documentation**: Each level directory must contain a `README.md` explaining the concept and task.

## 🛠 Workflows

- **Creating New Agents**: Start by defining the `tools` list in the frontmatter. Ensure `runSubagent` is included if the agent needs to perform research or complex multi-step tasks.
- **Generating Samples**: When asked to generate samples manually:
    1.  Create the directory structure first.
    2.  Draft the `README.md` for the level.
    3.  Create the `.github/prompts` and `.github/instructions` folders.
    4.  Add the specific `.prompt.md` or `.instructions.md` files.

## 🔍 Contextual Awareness
- This project focuses on **meta-programming** (writing prompts for agents to write code).
- When writing prompts, focus on **clarity**, **context**, and **constraints**.
- Use the `sampler.agent.md` as the reference implementation for how agents should be structured.
