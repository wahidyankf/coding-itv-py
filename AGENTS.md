# AGENTS.md

Guidance for AI coding agents working in this repository.

## Project

`coding-itv-py` is a Python project. It has no source code or build, lint, or test commands yet. Update this file when they exist.

## Repository setup

- Git uses `main` as the default branch. It is pushed to `origin` at `git@github.com:wahidyankf/coding-itv-py.git`. Do not delete or use `master`; it is an old remote branch.
- `package.json` comes from `npm init -y`. Its `test` script is still npm's placeholder.
- Node is pinned to 24.21.0 (the current LTS) with Volta, in the `volta` field of `package.json`. `engines` requires `>=24.21.0`. Use Volta so the pinned version is used automatically.
- Prettier formats JS, JSON, Markdown, and YAML. Husky runs `lint-staged` from `.husky/pre-commit` on commit, and lint-staged runs `prettier --write` on the staged files. Run `npm install` after cloning so the hooks get installed by the `prepare` script.
- Commit messages must follow Conventional Commits. `.husky/commit-msg` runs commitlint with `@commitlint/config-conventional`, configured in `commitlint.config.js`. Allowed types are build, chore, ci, docs, feat, fix, perf, refactor, revert, style, and test.
- The repo is an Nx workspace using npm workspaces (`packages/*`). `nx.json` is the workspace config. No Nx plugins are installed, and no projects are defined yet. `apps/` and `libs/` exist at the root for future projects. Add `project.json` files for projects and use `nx:run-commands` for targets.
- `.gitignore` covers Python, Node.js, Nx cache (`.nx/`), env files, and local tool settings.

## Agent skills

- `grill-me` is in `.agents/skills/grill-me/SKILL.md`. Its copy in `.claude/skills/grill-me/SKILL.md` points to the `.agents` copy. It comes from `wahidyankf/ose-rules`. Use it before a material choice that has more than one reasonable answer.

## Conventions

- Do not add Claude co-author attribution to commits. `.claude/settings.json` sets `includeCoAuthoredBy: false` for this project. Keep that setting.
- `.claude/settings.local.json` is machine-local and ignored by git. Do not commit it.
- Do not commit or push unless the user asks.
- Make commits thematically. Each commit should contain one coherent change, such as one tool setup or one feature, and should not mix unrelated files. Stage files by theme, and make a separate commit for each theme, rather than one commit for everything in the working tree.

## Code style

- Keep comments, commit messages, and notes brief.
- Explain why the code is needed, not what it does.
- Use clear, simple, and natural English that is easy for non-native speakers to understand.

## Architecture

### Config & secrets

- Config is built once from `process.env`, at import time.
- The build function is also exported separately, for testing.
- In production, if a required security env var is missing or invalid, the app fails fast.
