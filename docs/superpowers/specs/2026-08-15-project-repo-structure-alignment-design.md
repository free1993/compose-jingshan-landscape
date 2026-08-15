# Project Repo Structure Alignment Design

Date: 2026-08-15

## Goal

Reshape the repository to follow a project-repo distribution model closer to Zeejay0's structure while keeping the installable Skill name `lang-jingshan-photo-skill` unchanged.

## Decision

- Keep the repository as the public project shell.
- Move the installable Skill into `skills/lang-jingshan-photo-skill/`.
- Use `README.md` and `README.en.md` as the main public entry points.
- Add `examples/` for public case presentation.
- Reserve `assets/brand/` for future public brand materials.
- Keep ZIP distribution as optional, but make repository-first installation the primary documented path.

## Why

- Repository name and Skill name no longer need to be tightly coupled.
- The project can later grow to include more than one installable Skill without another structural rewrite.
- Public examples, notes, and brand materials gain clear homes outside the installable Skill folder.
- The installable folder stays compact and easier to copy into `~/.codex/skills/`.

## Scope

- Update repository structure and install paths.
- Update README, English README, portable prompt links, and rename checklist references.
- Add lightweight `examples/`, `assets/brand/`, and `skills/` index files.

## Out of Scope

- Renaming the GitHub repository itself
- Rebuilding historical ZIP releases
- Rewriting historical design documents that intentionally record earlier naming
