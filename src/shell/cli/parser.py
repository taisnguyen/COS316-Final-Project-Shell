'''Contains code for CLI parser.'''

import os
import subprocess
import psutil

from shell.utils.ansi_colors import ANSIColors
from shell.exceptions import ConfigurationError, CommandNotExistsError
from shell.process_manager.spawner import spawn_process


def exec_command(line, exec_bin_path):
    if not os.path.exists(exec_bin_path):
        raise ConfigurationError(
            f"The EXEC_BIN_PATH '{exec_bin_path}' does not exist.")

    try:
        spawn_process(line, exec_bin_path)
    except Exception as err:
        print(err)
        raise CommandNotExistsError()
