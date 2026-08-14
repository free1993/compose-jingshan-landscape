# Cross-Platform Distribution Design

## Goal

Make `compose-jingshan-landscape` easier to discover, install, and reuse without changing its visual grammar or image-generation behavior.

The release should support:

- exact-name discovery through GitHub repository search;
- native Agent Skills installation where the host supports the open format;
- a documented ZIP import path for Volcengine AgentKit and similar products;
- a self-contained prompt fallback for consumer AI products that cannot install Agent Skills;
- truthful compatibility claims that distinguish native installation from prompt-level reuse.

## Non-Goals

- Do not claim automatic listing in the Codex or ChatGPT Plugin Directory. Directory publication is separate from a public GitHub repository.
- Do not claim one-click Skill installation in the consumer Doubao app without an official supported import path.
- Do not alter the existing Lang Jingshan-inspired modes, routing, composition rules, author line, or comparison script behavior.
- Do not publish private source photographs, private test images, private paths, credentials, or generation history. Project-owned synthetic demonstration media may be published when labeled transparently.

## Repository Changes

### Discovery Metadata

Use the exact identifier `compose-jingshan-landscape` consistently in the repository title, README headings, installation examples, release name, and ZIP filename.

Set a concise bilingual-friendly GitHub description and add focused topics covering Agent Skills, Codex, pictorial photography, Lang Jingshan, Chinese aesthetics, image editing, TRAE, and Volcengine AgentKit. Topics improve GitHub discovery but must not be presented as marketplace publication.

### Documentation

Keep `README.md` as the primary Chinese document and add `README.en.md` for international discovery.

The Chinese README will include:

- the visual proposition and five supported modes;
- exact GitHub/Codex installation wording;
- clone-and-copy installation commands;
- a compatibility matrix that labels each host as native Skill, ZIP import, or portable-prompt fallback;
- links to the English README, portable prompt, installable Skill directory, and release ZIP;
- privacy, attribution, license, and historical homage notices.

The English README will carry the same factual claims and link back to Chinese.

### Portable Prompt

Add `PORTABLE_PROMPT.md` as a self-contained fallback for AI products without Agent Skills support. It will:

- preserve the Skill's core decision axes and visual constraints;
- support the single, layered, before/after, layered-comparison, and poetic-small-scene intents;
- avoid local paths and Codex-specific tool names;
- instruct the host to use its own image-editing capability when available;
- explain that deterministic comparison requires an external layout tool when Python execution is unavailable;
- remain a prompt compatibility layer, not a claim of native installation.

The authoritative implementation remains `compose-jingshan-landscape/SKILL.md`; the portable prompt is a compact interoperability surface, not a duplicate full specification.

## Compatibility Claims

Use three explicit levels:

1. **Native Agent Skill**: products that implement the Agent Skills format and can load a folder containing `SKILL.md`.
2. **ZIP Import**: products such as Volcengine AgentKit that accept a packaged Skill folder with `SKILL.md` at the folder root.
3. **Portable Prompt**: products such as the consumer Doubao app when no verified native Skill import is available.

List a product only when there is documentation or a reproducible install path. Use "expected to work with compatible Agent Skills hosts" for unverified implementations rather than promising official support.

## Release Package

Create `compose-jingshan-landscape-v1.0.0.zip` as a GitHub Release asset.

Required archive layout:

```text
compose-jingshan-landscape/
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── evaluation-cases.md
│   ├── layered-composite.md
│   └── visual-grammar.md
└── scripts/build_comparison.py
```

The archive must contain exactly one top-level Skill folder. Repository documentation and `.git` data must not be included in the archive.

## Validation

Before release:

- verify the six Skill source files match the installed/local authoritative copy unless an intentional Skill edit is made;
- parse the ZIP and confirm one top-level folder plus the required `SKILL.md`;
- validate frontmatter name and description constraints;
- verify all README links and installation paths;
- scan tracked files and release contents for unexpected images, temporary paths, credentials, and private data; allow only documented project-owned demonstration media in the repository and exclude it from the release ZIP;
- confirm the GitHub repository is public and searchable by the exact Skill name;
- download the published release asset and compare its SHA-256 hash to the local artifact;
- confirm local `main` and `origin/main` are synchronized.

## Success Criteria

- Searching GitHub for `compose-jingshan-landscape` returns the repository.
- A Codex user can install from `free1993/compose-jingshan-landscape` using the documented Skill path.
- An AgentKit user can import the release ZIP without restructuring it.
- A user of a non-Skill host can use `PORTABLE_PROMPT.md` without Codex-specific instructions.
- No documentation claims automatic Codex directory listing or native consumer Doubao Skill installation.
