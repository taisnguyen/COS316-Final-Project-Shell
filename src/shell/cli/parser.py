'''Contains code for CLI parser responsible for parsing commands/redirection/pipes and executing them.'''

import os
import subprocess
import shlex

from shell.utils.ansi_colors import ANSIColors
from shell.exceptions import CommandNotExistsError, RedirectionSyntaxError
from shell.process_manager.spawner import spawn_process


def exec_command(line, exec_bin_path):
    cmd_groups_to_process = line.split("|")
    cmd_groups_to_process = [shlex.split(cmd.strip()) for cmd in cmd_groups_to_process]

    try:
        background = False
        if cmd_groups_to_process[-1][-1] == "&":
            background = True
            cmd_groups_to_process[-1] = cmd_groups_to_process[-1][:-1]

        # If only one command, run it normally
        if len(cmd_groups_to_process) == 1:
            stdin, stdout, index_of_left_redirection = _handle_redirection(cmd_groups_to_process[0])

            spawn_process(
                args=cmd_groups_to_process[0][:index_of_left_redirection if index_of_left_redirection else None],
                exec_bin_path=exec_bin_path,
                stdin=stdin,
                stdout=stdout,
                run_in_background=background,
            )
            return

        # If there are multiple commands,
        # let us pipe stdout into stdin of next command.
        process_stdout = subprocess.PIPE
        for i in range(0, len(cmd_groups_to_process)):
            # Check for redirection.
            stdin, stdout, index_of_left_redirection = _handle_redirection(cmd_groups_to_process[i])

            process_stdout = spawn_process(
                args=cmd_groups_to_process[i][:index_of_left_redirection if index_of_left_redirection else None],
                exec_bin_path=exec_bin_path,
                stdin=stdin if stdin != subprocess.PIPE else process_stdout,
                stdout=stdout or subprocess.PIPE,
                run_in_background=background
            )

        # Read out last process stdout.
        if process_stdout:
            print( process_stdout.read().decode("utf-8"))

        # iterate through cmd_groups_to_process: pass in
        # Promises JS -> Futures Python
    except FileNotFoundError:
        raise
    except RedirectionSyntaxError:
        raise
    except Exception as err:
        print(err)
        raise CommandNotExistsError()

def _handle_redirection(cmd_group):
    process_stdout = None
    process_stdin = subprocess.PIPE

    index_of_left_redirection = None
    index_of_right_redirection = None

    # Handle left redirection.
    try:
        index_of_left_redirection = cmd_group.index("<")
        process_stdin = open(cmd_group[index_of_left_redirection+1], "r")
    except FileNotFoundError:
        raise
    except:
        pass

    # Handle right redirection.
    try:
        index_of_right_redirection = cmd_group.index(">")
        if index_of_left_redirection and index_of_right_redirection < index_of_left_redirection:
            raise RedirectionSyntaxError()
        process_stdout = open(cmd_group[index_of_right_redirection+1], "w+")
    except FileNotFoundError:
        raise
    except RedirectionSyntaxError:
        raise
    except:
        pass

    return process_stdin, process_stdout, index_of_left_redirection or index_of_right_redirection
