from click.testing import CliRunner

from oss_helper_cli.cli import main


def test_pr_template() -> None:
    runner = CliRunner()
    result = runner.invoke(
        main,
        [
            "pr-template",
            "--title",
            "Add docs glossary",
            "--summary",
            "Adds shared terminology to the docs.",
            "--issue",
            "3077",
            "--test",
            "pytest",
        ],
    )

    assert result.exit_code == 0
    assert "## Title" in result.output
    assert "Closes #3077" in result.output
    assert "- `pytest`" in result.output


def test_issue_reply() -> None:
    runner = CliRunner()
    result = runner.invoke(
        main,
        [
            "issue-reply",
            "--status",
            "confirmed",
            "--next-step",
            "I will prepare a fix next.",
        ],
    )

    assert result.exit_code == 0
    assert "Thanks for the report." in result.output
    assert "I was able to reproduce this on my side." in result.output


def test_project_blurb() -> None:
    runner = CliRunner()
    result = runner.invoke(
        main,
        [
            "project-blurb",
            "--name",
            "oss-helper-cli",
            "--audience",
            "solo maintainers",
            "--problem",
            "repetitive writing work",
            "--solution",
            "small CLI templates",
        ],
    )

    assert result.exit_code == 0
    assert "oss-helper-cli is an open source tool for solo maintainers." in result.output


def test_changelog_entry() -> None:
    runner = CliRunner()
    result = runner.invoke(
        main,
        [
            "changelog-entry",
            "--version",
            "0.2.0",
            "--change",
            "Added CI",
            "--change",
            "Added new templates",
        ],
    )

    assert result.exit_code == 0
    assert "## 0.2.0" in result.output
    assert "- Added CI" in result.output
    assert "- Added new templates" in result.output


def test_contributor_welcome() -> None:
    runner = CliRunner()
    result = runner.invoke(
        main,
        [
            "contributor-welcome",
            "--name",
            "@newdev",
            "--next-step",
            "I will review this in the next round.",
        ],
    )

    assert result.exit_code == 0
    assert "Thanks for the contribution, @newdev." in result.output
    assert "I will review this in the next round." in result.output

