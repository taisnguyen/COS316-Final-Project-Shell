'''Utilities for the Shell commands.'''

# from shell.commands.help import Help
# We cannot import Help here because it would create a circular dependency.
# So we import it in the __init__ file instead.
from shell.commands.process_list import ProcessList
from shell.commands.process_suspend import ProcessSuspend
from shell.commands.process_resume import ProcessResume
from shell.commands.process_kill import ProcessKill

# Here, we populate commands_list with all commands other than the help command.
commands_list = [ProcessList, ProcessSuspend, ProcessResume, ProcessKill]


def get_command_if_exists(commands, cmd):
    """Returns command if it exists, otherwise None."""
    for command in commands:
        if command.name == cmd or command.alias == cmd:
            return command
    return None
