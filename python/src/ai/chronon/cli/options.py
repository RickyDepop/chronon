import click

from ai.chronon.cli.formatter import Format

CHRONON_ROOT_ENVVAR = "CHRONON_ROOT"
CHRONON_REPO_PATH_ENVVAR = "CHRONON_REPO_PATH"


def _envvar(envvars):
    envvars = tuple(envvars)
    return envvars[0] if len(envvars) == 1 else list(envvars)


def chronon_root_option(
    *,
    help="Path to the Chronon root (containing teams.py).",
    default=None,
    **kwargs,
):
    return click.option(
        "--chronon-root",
        default=default,
        envvar=CHRONON_ROOT_ENVVAR,
        help=help,
        **kwargs,
    )


def repo_root_option(
    *,
    help="Path to the Chronon repo root.",
    default=".",
    show_default=True,
    envvars=(CHRONON_ROOT_ENVVAR,),
    **kwargs,
):
    return click.option(
        "-r",
        "--repo",
        envvar=_envvar(envvars),
        help=help,
        default=default,
        show_default=show_default,
        **kwargs,
    )


def format_option():
    return click.option(
        "-f",
        "--format",
        help="Output format.",
        default=Format.TEXT,
        type=click.Choice(Format, case_sensitive=False),
        show_default=True,
    )


def hub_url_option():
    return click.option(
        "--hub-url",
        help="Zipline Hub address, e.g. http://localhost:3903",
        default=None,
    )


def use_auth_option():
    return click.option(
        "--use-auth/--no-use-auth",
        help="Use authentication when connecting to Zipline Hub",
        default=True,
    )


def force_option():
    return click.option(
        "--force",
        help="Force compile even if there are version changes to existing confs",
        is_flag=True,
    )


def cloud_provider_option(valid_clouds):
    return click.option(
        "--cloud",
        help="Cloud provider for the hub and related services",
        type=click.Choice(valid_clouds, case_sensitive=False),
        required=False,
        default=None,
    )


def customer_id_option():
    return click.option(
        "--customer-id",
        help="Customer ID for authentication. Required for Azure.",
        type=str,
        required=False,
        default=None,
    )


def env_option(
    *,
    help="Environment to run against",
    choices=("prod", "canary"),
    default="prod",
    show_default=True,
):
    return click.option(
        "--env",
        help=help,
        type=click.Choice(list(choices), case_sensitive=False),
        default=default,
        show_default=show_default,
    )
