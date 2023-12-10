"""Subpackage exposes all custom commands for the Shell."""

from shell.commands.utils import commands_list

from shell.commands.help import Help
commands_list = [*commands_list, Help]


def get_command_if_exists(cmd):
    """Returns command if it exists, otherwise None."""
    from shell.commands.utils import get_command_if_exists
    return get_command_if_exists(commands_list, cmd)
