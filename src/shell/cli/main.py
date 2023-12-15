"""Entry point for the shell application."""
import os
import sys
import cmd

from shell.cli.parser import exec_command
from shell.cli.utils import setup_config
from shell.utils.ansi_colors import ANSIColors
from shell.exceptions import ConfigurationError, CommandNotExistsError
from shell.commands import get_command_if_exists


class Shell(cmd.Cmd):
    prompt = f"{ANSIColors.OKGREEN}{os.getcwd()}{ANSIColors.ENDC} $ "

    def __init__(self, config):
        cmd.Cmd.__init__(self)
        self.config = config

    def precmd(self, line):
        if line == "EOF":
            raise KeyboardInterrupt
        elif line == "":
            return line

        cmd, _, _ = self.parseline(line)

        # Check if command exists in shell.commands subpackage.
        executable_cmd = get_command_if_exists(cmd)
        if executable_cmd:
            executable_cmd.exec(line.split(" ")[1:])
            return line

        # Check if command is implemented above as do_<command>.
        else:
            try:
                getattr(self, f"do_{cmd}")
                return line
            except AttributeError:
                pass

        # Otherwise, attempt to find binaries in provided EXEC_BIN_PATH.
        try:
            exec_command(line, self.config["EXEC_BIN_PATH"])
        # Could put a higher level, but this is fine for now.
        except ConfigurationError as err:
            sys.exit(f"{ANSIColors.FAIL}Terminating... {str(err)} \nPlease delete the current configuration file and rerun the Shell to recreate.{ANSIColors.ENDC}")
        except CommandNotExistsError:
            self._cmd_not_exists(line.split(" ")[0])

        return line

    def postcmd(self, stop, line):
        self.prompt = f"{ANSIColors.OKGREEN}{os.getcwd()}{ANSIColors.ENDC} $ "

    def _cmd_not_exists(self, cmd):
        print(
            f"{ANSIColors.FAIL}The term '{cmd}' is not recognized as a command. Please check the spelling or make sure that EXEC_BIN_PATH is set properly.{ANSIColors.ENDC}\n")

    def do_exit(self, line):
        sys.exit(0)

    # Here we are just overriding parent class default in favor of _cmd_not_exists.
    def default(self, line):
        pass

    # Similarly, in favor of help command in shell.commands.
    def do_help(self, line):
        pass


def main():
    config = setup_config()

    # Handle keyboard shortcuts.
    # import shell.cli.keyboard_handlers

    print("COS316 Shell 1.0.0 (by Tai Sanh Nguyen and Spencer Doyle).")
    print('Type "help" for more information.')

    shell = Shell(config)

    # Start Shell.
    while True:
        try:
            shell.cmdloop()
        except KeyboardInterrupt:
            print('\nIf you want to exit, type "exit".')
    # pass
