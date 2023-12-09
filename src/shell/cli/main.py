"""Entry point for the shell application."""
import sys
import cmd

from shell.cli.parser import exec_command
from shell.cli.utils import setup_config
from shell.utils.ansi_colors import ANSIColors
from shell.exceptions import ConfigurationError, CommandNotExistsError


class Shell(cmd.Cmd):
    prompt = f"{ANSIColors.ENDC}>>> "

    def __init__(self, config):
        cmd.Cmd.__init__(self)
        self.config = config

    # Here we are just overriding parent class default in favor of cmd_not_exists.
    def default(self, line):
        pass

    def cmd_not_exists(self, cmd):
        print(
            f"{ANSIColors.FAIL}{cmd} : The term '{cmd}' is not recognized as a command. Please check the spelling or make sure that EXEC_BIN_PATH is set properly.{ANSIColors.ENDC}")
        pass

    def precmd(self, line):
        try:
            exec_command(line, self.config["EXEC_BIN_PATH"])
        except ConfigurationError as err:
            sys.exit(f"{ANSIColors.FAIL}Terminating... {str(err)} \nPlease delete the current configuration file and rerun the Shell to recreate.{ANSIColors.ENDC}")
        except CommandNotExistsError:
            self.cmd_not_exists(line.split(" ")[0])

        return super().precmd(line)


def main():
    config = setup_config()

    # Start Shell.
    print("COS316 Shell 1.0.0 (by Tai Sanh Nguyen and Spencer Doyle).")
    print('Type "help" for more information.')
    Shell(config).cmdloop()
