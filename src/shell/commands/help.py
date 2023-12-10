import psutil

from shell.commands.base import Command
from shell.commands.utils import commands_list
from shell.commands.utils import get_command_if_exists


class Help(Command):
    name = "help"
    alias = "?"
    description = "Prints out a man page for a specified command."
    usage = "help <command>"

    @staticmethod
    def exec(args):
        if len(args) == 0:
            print(Help.usage)
            return

        cmd = args[0]
        if cmd == "help":
            print(Help.description)
            return

        specified_cmd = get_command_if_exists(commands_list, cmd)
        if specified_cmd:
            print(specified_cmd.description)
        else:
            print(f"{cmd} : The term '{cmd}' is not recognized as a command. Please check the spelling or make sure that EXEC_BIN_PATH is set properly.\n")
        pass


def format_description(name, description, usage):
    pass
