import os

from shell.commands.base import Command
from shell.utils.ansi_colors import ANSIColors


class ChangeDirectory(Command):
    name = "change_directory"
    alias = "cd"
    description = "Change the current working directory."
    usage = "cd <directory>"

    @staticmethod
    def exec(args):
        if len(args) == 0:
            print(ChangeDirectory.usage)
            return

        directory = args[0]
        try:
            os.chdir(os.path.abspath(directory))
        except:
            print(
                f"{ANSIColors.FAIL}The path {directory} is not found.{ANSIColors.ENDC}\n")
