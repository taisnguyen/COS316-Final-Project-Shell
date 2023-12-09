'''Contains code for CLI parser.'''

import os
import subprocess

from shell.exceptions import ConfigurationError, CommandNotExistsError


def exec_command(line, exec_bin_path):
    if not os.path.exists(exec_bin_path):
        raise ConfigurationError(
            f"The EXEC_BIN_PATH '{exec_bin_path}' does not exist.")

    try:
        cwd = os.getcwd()
        os.chdir(exec_bin_path)
        subprocess.Popen(line)
        os.chdir(cwd)
    except Exception:
        raise CommandNotExistsError()

    pass
