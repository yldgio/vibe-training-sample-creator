---
agent: sampler
description: update existing training samples to align with best practices and user requirements.
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Goal
You only generate the prompt samples, not the code.

## Outline

The text the user typed after the command is the project name and any specific requirements for the samples.
Given that project name, do this:
1. **Check for existing folders before creating new one**:
  - if in the `output` there is a folder with a name matching the project-name you will proceed to review and update existing samples to align with best practices.
  - If the folder does not exist, respond with `The project {{project-name}} does not exist. Cannot update non-existing samples, please specify the exact project name/folder name. execute /update project-name to update the samples`.


