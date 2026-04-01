# oss-helper-cli

`oss-helper-cli` is a lightweight command-line tool for drafting common open source workflow text.

It is built for solo maintainers, first-time contributors, and small teams who want a faster way to write the repetitive parts of open source work without hiding everything behind a black box.

## What it does

The first version focuses on 3 common tasks:

- generate a pull request template
- generate a short issue triage reply
- generate a concise project blurb
- generate changelog entries
- generate friendly contributor follow-up messages

The project is intentionally small. The goal is to provide practical building blocks that can grow over time into a broader toolkit for open source maintenance.

## Why this exists

A lot of open source work is not coding. It is repeated writing:

- PR summaries
- issue replies
- project descriptions
- release notes
- contributor onboarding text

This project turns those repeated writing tasks into reusable CLI helpers that are transparent, scriptable, and easy to improve.

## Installation

For local development:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

Then run:

```bash
oss-helper --help
```

## Commands

### `pr-template`

Generate a lightweight pull request body.

```bash
oss-helper pr-template \
  --title "Add glossary to command line reference docs" \
  --summary "Adds a glossary section for ambiguous terms used across the docs." \
  --issue 3077 \
  --test "./.venv/bin/sphinx-build -E -W -b dirhtml docs docs/_build/dirhtml"
```

Example output:

```md
## Title

Add glossary to command line reference docs

## Summary

Adds a glossary section for ambiguous terms used across the docs.
Closes #3077

## Testing

- `./.venv/bin/sphinx-build -E -W -b dirhtml docs docs/_build/dirhtml`
```

### `issue-reply`

Generate a short issue triage response.

```bash
oss-helper issue-reply \
  --tone warm \
  --status investigating \
  --next-step "I am reproducing this locally and will share a concrete update once I confirm the root cause."
```

### `project-blurb`

Generate a short project introduction.

```bash
oss-helper project-blurb \
  --name "oss-helper-cli" \
  --audience "solo maintainers and new contributors" \
  --problem "repetitive contribution writing work" \
  --solution "small CLI templates for PRs, issue replies, and short project summaries"
```

### `changelog-entry`

Generate a short changelog section for a release.

```bash
oss-helper changelog-entry \
  --version "0.2.0" \
  --change "Added CI" \
  --change "Added release drafting support"
```

### `contributor-welcome`

Generate a friendly maintainer reply for a new contribution.

```bash
oss-helper contributor-welcome \
  --name "@newdev" \
  --next-step "I will review this in the next round."
```

## Project goals

- stay simple enough for one person to maintain
- produce output that is easy to copy into real workflows
- keep the generated text editable and human-readable
- grow through practical contributor use cases instead of feature bloat

## Roadmap

- write generated output to markdown files
- support reusable template profiles
- add changelog and release note helpers
- add contributor onboarding text generators
- add optional GitHub metadata input

## Contributing

Contributions are welcome. If you want to help, start here:

- [Contributing Guide](./CONTRIBUTING.md)

## Quality checks

The repository includes a GitHub Actions workflow that installs the package and runs the test suite on multiple Python versions.

## License

MIT
