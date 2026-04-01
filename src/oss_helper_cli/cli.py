from __future__ import annotations

import textwrap

import click


def _clean_block(value: str) -> str:
    return textwrap.dedent(value).strip()


@click.group()
def main() -> None:
    """Draft small text snippets for common open source workflows."""


@main.command("pr-template")
@click.option("--title", required=True, help="Short title of the change.")
@click.option("--summary", required=True, help="What the change does.")
@click.option("--issue", type=int, help="Related issue number.")
@click.option(
    "--test",
    "tests",
    multiple=True,
    help="Verification command. Pass more than once for multiple checks.",
)
def pr_template(title: str, summary: str, issue: int | None, tests: tuple[str, ...]) -> None:
    """Generate a lightweight pull request body."""
    summary_lines = [summary]

    if issue is not None:
        summary_lines.append(f"Closes #{issue}")

    test_lines = [f"- `{item}`" for item in tests] or ["- Not run"]
    body = "\n".join(
        [
            "## Title",
            "",
            title,
            "",
            "## Summary",
            "",
            *summary_lines,
            "",
            "## Testing",
            "",
            *test_lines,
        ]
    )
    click.echo(body)


@main.command("issue-reply")
@click.option(
    "--tone",
    type=click.Choice(["warm", "neutral", "direct"], case_sensitive=False),
    default="warm",
    show_default=True,
    help="Tone of the message.",
)
@click.option(
    "--status",
    type=click.Choice(
        ["investigating", "confirmed", "needs-info", "planned"], case_sensitive=False
    ),
    required=True,
    help="Current status you want to communicate.",
)
@click.option("--next-step", required=True, help="What happens next.")
def issue_reply(tone: str, status: str, next_step: str) -> None:
    """Generate a short issue triage response."""
    opening_by_tone = {
        "warm": "Thanks for the report.",
        "neutral": "Thanks for sharing this.",
        "direct": "Thanks, this is helpful.",
    }
    status_line = {
        "investigating": "I am looking into the behavior now.",
        "confirmed": "I was able to reproduce this on my side.",
        "needs-info": "I need a bit more detail before I can reproduce this reliably.",
        "planned": "This looks reasonable and I plan to work on it.",
    }

    reply = f"""
    {opening_by_tone[tone]}

    {status_line[status]}
    {next_step}
    """
    click.echo(_clean_block(reply))


@main.command("project-blurb")
@click.option("--name", required=True, help="Project name.")
@click.option("--audience", required=True, help="Who the project is for.")
@click.option("--problem", required=True, help="Problem the project solves.")
@click.option("--solution", required=True, help="How the project solves it.")
def project_blurb(name: str, audience: str, problem: str, solution: str) -> None:
    """Generate a short project introduction."""
    blurb = f"""
    {name} is an open source tool for {audience}. It helps with {problem} by
    providing {solution}. The project is designed to stay practical, easy to
    adopt, and friendly to contributors.
    """
    click.echo(_clean_block(blurb))


@main.command("changelog-entry")
@click.option("--version", required=True, help="Version number, such as 0.2.0.")
@click.option(
    "--change",
    "changes",
    multiple=True,
    required=True,
    help="A release highlight bullet. Pass more than once for multiple items.",
)
def changelog_entry(version: str, changes: tuple[str, ...]) -> None:
    """Generate a simple changelog section."""
    lines = [f"## {version}", ""]
    lines.extend(f"- {change}" for change in changes)
    click.echo("\n".join(lines))


@main.command("contributor-welcome")
@click.option("--name", help="Contributor name or handle.")
@click.option("--next-step", required=True, help="What they should do next.")
def contributor_welcome(name: str | None, next_step: str) -> None:
    """Generate a friendly first-response message for a contributor."""
    greeting = f"Thanks for the contribution, {name}." if name else "Thanks for the contribution."
    body = f"""
    {greeting}

    I appreciate you taking the time to help improve the project.
    {next_step}
    """
    click.echo(_clean_block(body))


if __name__ == "__main__":
    main()
