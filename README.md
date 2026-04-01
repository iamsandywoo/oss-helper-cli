# oss-helper-cli

`oss-helper-cli` is a small command-line tool for solo open source contributors and maintainers.

It helps with common writing tasks around contribution workflows:

- draft a pull request body
- draft a friendly issue reply
- draft a short project pitch or application blurb

The goal is to stay lightweight, transparent, and easy to extend.

## Why this project exists

Open source work often includes a lot of repeated writing: PR descriptions, issue triage replies, and short project summaries. This tool turns those common tasks into reusable templates so contributors can move faster without sounding robotic.

## Install

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Usage

Show help:

```bash
oss-helper --help
```

Generate a PR template:

```bash
oss-helper pr-template \
  --title "Add glossary to command line reference docs" \
  --summary "Adds a glossary section for ambiguous terms used across the docs." \
  --issue 3077 \
  --test "./.venv/bin/sphinx-build -E -W -b dirhtml docs docs/_build/dirhtml"
```

Generate an issue reply:

```bash
oss-helper issue-reply \
  --tone warm \
  --status investigating \
  --next-step "I am reproducing this locally and will post an update once I confirm the root cause."
```

Generate a short project pitch:

```bash
oss-helper project-blurb \
  --name "oss-helper-cli" \
  --audience "solo maintainers and new contributors" \
  --problem "repetitive contribution writing work" \
  --solution "small CLI templates for PRs, issue replies, and project summaries"
```

## Roadmap

- add markdown output file support
- add reusable config profiles
- add release notes and changelog helpers
- add contributor onboarding templates
- add GitHub issue and PR metadata ingestion

## License

MIT

