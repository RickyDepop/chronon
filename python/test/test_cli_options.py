import click
from click.testing import CliRunner

from ai.chronon.cli.options import (
    CHRONON_REPO_PATH_ENVVAR,
    CHRONON_ROOT_ENVVAR,
    chronon_root_option,
    env_option,
    repo_root_option,
)


def test_chronon_root_option_reads_chronon_root_env():
    @click.command()
    @chronon_root_option()
    def command(chronon_root):
        click.echo(chronon_root)

    result = CliRunner().invoke(
        command,
        [],
        env={CHRONON_ROOT_ENVVAR: "/tmp/chronon-root"},
    )

    assert result.exit_code == 0
    assert result.output.strip() == "/tmp/chronon-root"


def test_repo_root_option_prefers_explicit_repo_over_chronon_root_env():
    @click.command()
    @repo_root_option()
    def command(repo):
        click.echo(repo)

    result = CliRunner().invoke(
        command,
        ["--repo", "/tmp/explicit-root"],
        env={CHRONON_ROOT_ENVVAR: "/tmp/env-root"},
    )

    assert result.exit_code == 0
    assert result.output.strip() == "/tmp/explicit-root"


def test_repo_root_option_supports_legacy_chronon_repo_path_fallback():
    @click.command()
    @repo_root_option(envvars=(CHRONON_ROOT_ENVVAR, CHRONON_REPO_PATH_ENVVAR))
    def command(repo):
        click.echo(repo)

    result = CliRunner().invoke(
        command,
        [],
        env={CHRONON_REPO_PATH_ENVVAR: "/tmp/legacy-root"},
    )

    assert result.exit_code == 0
    assert result.output.strip() == "/tmp/legacy-root"


def test_env_option_rejects_unknown_environment():
    @click.command()
    @env_option()
    def command(env):
        click.echo(env)

    result = CliRunner().invoke(command, ["--env", "staging"])

    assert result.exit_code == 2
    assert "Invalid value for '--env'" in result.output
