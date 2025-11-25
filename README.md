# Vibe Coding Training Sample Creator

This repository is a scaffold for generating **Vibe Coding** training samples using declarative AI agents. Instead of traditional source code, the core "logic" lives in **agent definitions, prompts, and instructions** that guide an AI agent to generate educational coding tasks at different complexity levels.

## Repository Purpose

The goal of this repo is to:

- Provide a **standard structure** for Vibe Coding training projects.
- Organize examples by **project** (e.g. `password-generator`) and by **difficulty level** (basic, intermediate, advanced).
- Make it easy to plug these prompts and instructions into an agent runner (such as GitHub Copilot agents) to automatically generate or regenerate training material.

## Project Structure

At a high level:

```text
output/
  {project-name}/
    level-1-basic/
      README.md              # Level overview & learning goals
      prompts/               # Level-specific reusable prompts
        *.prompt.md
    level-2-intermediate/
      README.md
      # Optional: instructions and prompts for more complex flows
    level-3-advanced/
      # Advanced, multi-step, tool-using agent flows

.github/
  copilot-instructions.md    # Global instructions for agents working in this repo
  # (Optional) .github/agents/*.agent.md and .github/prompts/*.prompt.md
```

In your current workspace, there is a single sample project:

```text
output/
  password-generator/
    level-1-basic/
      README.md
      prompts/
        password-generator-better.prompt.md
        password-generator-simple.prompt copy.md
    level-2-intermediate/
      README.md
      copilot-instructions.md
    level-3-advanced/
      # (empty for now)
```

### Levels Explained

Each `{project-name}` follows a three-level difficulty model:\r

1. **Level 1 – Basic**
   - One-shot prompts.
   - Simple tasks, often single-file outputs.
   - Great for introducing a concept (e.g. a basic password generator).

2. **Level 2 – Intermediate**
   - Few-shot prompting and/or explicit requirement breakdown.
   - May involve separate instruction files and multiple steps.
   - Encourages more structure and partial planning.

3. **Level 3 – Advanced**
   - Chain-of-thought style prompting.
   - Dynamic planning, tool usage, and sometimes sub-agents.
   - Best suited for complex, multi-file, or multi-phase coding exercises.

## How to Use This Repository

### 1. Exploring Existing Samples

To understand how a project is organized, start with its level README files, for example:

- `output/password-generator/level-1-basic/README.md`
- `output/password-generator/level-2-intermediate/README.md`

Then open the prompts under `prompts/` to see how the training tasks are phrased for an agent.

### 2. Creating a New Training Project

To add a new project (for example, `todo-app`):

1. Create the directory structure:

   ```text
   output/
     todo-app/
       level-1-basic/
         README.md
         prompts/
       level-2-intermediate/
         README.md
       level-3-advanced/
         README.md (optional, can be added later)
   ```

2. For each level:
   - Write a `README.md` describing the learning goals and the kind of code the learner should produce.
   - For Level 1, create one or more `*.prompt.md` files in `prompts/` that describe a simple, focused task.
   - For Levels 2 and 3, you can:
     - Add richer instructions under `.github/instructions/` for that project/level.
     - Reference or add `.github/prompts/*.prompt.md` for reusable prompt patterns.

3. (Optional) Define agents under `.github/agents/*.agent.md` if you want custom agent personas or tools.

### 3. Example Usage with an Agent Runner

How you *run* these prompts depends on your agent framework, but a typical workflow looks like this:

1. Configure your agent (e.g. GitHub Copilot agent, CLI agent runner, or a custom script) to:
   - Use `.github/copilot-instructions.md` as system-level context.
   - Load a level README as high-level task description.
   - Feed one of the `*.prompt.md` files as the user prompt.

2. Ask the agent to generate the target artifact. For example:
   - For `password-generator` level 1 basic, the agent might generate a single `password-generator.js` (or equivalent) file.
   - For intermediate or advanced levels, the agent may generate multiple files or a more structured implementation.

3. Iterate on the prompts or instructions as needed to refine the training sample quality.

> Note: This repository intentionally does **not** prescribe a specific execution engine. It is compatible with any system that can:
> - Read Markdown prompts and instructions, and
> - Use them as context for an AI coding assistant or agent.

## Local Development

Although this repo is mostly Markdown, you can still follow typical development hygiene:

- Use branches and pull requests when editing or adding training projects.
- Keep prompts and instructions **small, focused, and well-commented**.
- When adding a new project, make sure each level has a clear README and, if applicable, example prompts.

## Git & GitHub

This repository is intended to be version-controlled and shared publicly so others can:

- Review and iterate on training material.
- Reuse, fork, and adapt the sample structures.
- Contribute new projects and levels via pull requests.

The next sections of your workflow should:

1. Initialize a local git repository in this folder.
2. Create an initial commit containing the existing structure and this README.
3. Push it to a new public repository in your GitHub account.

If you would like, I can walk you through those git/GitHub steps interactively or help you tweak this README further.
