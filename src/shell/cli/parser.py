'''Contains code for CLI parser responsible for parsing commands/redirection/pipes and executing them.'''

import os
import asyncio
import re
import subprocess
import psutil

from shell.utils.ansi_colors import ANSIColors
from shell.exceptions import ConfigurationError, CommandNotExistsError
from shell.process_manager.spawner import spawn_process


def exec_command(line, exec_bin_path):
    # cmd_groups_to_process = line.split("|")

    try:
        spawn_process(line, exec_bin_path)
        # iterate through cmd_groups_to_process: pass in
        # Promises JS -> Futures Python
    except Exception as err:
        print(err)
        raise CommandNotExistsError()
