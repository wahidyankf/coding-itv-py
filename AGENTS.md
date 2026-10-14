# AGENTS.md

Guidance for AI coding agents working in this repository.

## Project

`coding-itv-py` is a Python project. It has no source code or build, lint, or test commands yet. Update this file when they exist.

## Repository setup

- Git is initialized with `master` as the default branch. There are no commits yet.
- `package.json` exists from `npm init -y`, with npm's placeholder `test` script. Nothing in the project uses Node yet.
- Prettier formats JS, JSON, Markdown, and YAML. Husky runs `lint-staged` from `.husky/pre-commit` on commit, and lint-staged runs `prettier --write` on the staged files. Run `npm install` after cloning so the hooks get installed by the `prepare` script.
- Commit messages must follow Conventional Commits. `.husky/commit-msg` runs commitlint with `@commitlint/config-conventional`, configured in `commitlint.config.js`. Allowed types are build, chore, ci, docs, feat, fix, perf, refactor, revert, style, and test.
- `.gitignore` covers Python, Node.js, env files, and local tool settings.

## Conventions

- Do not add Claude co-author attribution to commits. `.claude/settings.json` sets `includeCoAuthoredBy: false` for this project. Keep that setting.
- `.claude/settings.local.json` is machine-local and ignored by git. Do not commit it.
- Do not commit or push unless the user asks.
- Make commits thematically. Each commit should contain one coherent change, such as one tool setup or one feature, and should not mix unrelated files. Stage files by theme, and make a separate commit for each theme, rather than one commit for everything in the working tree.
