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
    cmd_groups_to_process = line.split("|")
    cmd_groups_to_process = [cmd.strip() for cmd in cmd_groups_to_process]

    try:
        
        # current_s_process = subprocess.Popen(["/bin/ls", "-la"], stdout=subprocess.PIPE)
        # while current_s_process.poll() is None:
        #     pass

        # current_s_process = subprocess.Popen(["/bin/grep", "env"], stdout=subprocess.PIPE, stdin=current_s_process.stdout)
        # while current_s_process.poll() is None:
        #     pass

        # current_s_process = subprocess.Popen(["/bin/wc"], stdin=current_s_process.stdout)
        # while current_s_process.poll() is None:
        #     pass

        
        # If only one command, run it normally
        if len(cmd_groups_to_process) == 1:
            spawn_process(cmd_groups_to_process[0], exec_bin_path)
            return
        
        # If multiple commands,
        # Pipe stdout into pipe
        process_stdout = spawn_process(cmd_groups_to_process[0], exec_bin_path, subprocess.PIPE)

        # Receive stdin from pipe and pipe stdout into pipe
        for i in range(1, len(cmd_groups_to_process) - 1):
            process_stdout = spawn_process(cmd_groups_to_process[i], exec_bin_path, subprocess.PIPE, process_stdout)

        # Receive stdin from pipe
        spawn_process(cmd_groups_to_process[-1], exec_bin_path, stdin=process_stdout)



        # iterate through cmd_groups_to_process: pass in
        # Promises JS -> Futures Python
    except Exception as err:
        print(err)
        raise CommandNotExistsError()
