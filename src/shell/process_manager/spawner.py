"""Spawns and manages processes."""

import os
import asyncio
import subprocess
import psutil
import shlex


def spawn_process(args, exec_bin_path):
    """Spawns a process with the given arguments."""

    # Keep track of current subprocess.
    current_s_process = None
    print("args", args)

    try:
        run_in_background = False
        args = shlex.split(args)

        # Run process in background
        if args[-1] == "&":
            run_in_background = True
            args = args[:-1]

        # Try to start a process for each path to find the first valid one
        bin_paths = exec_bin_path.split(";")
        succeeded = False

        for path in bin_paths:
            try:
                current_s_process = subprocess.Popen(
                    [os.path.join(path, args[0]), *args[1:]])
                succeeded = True
                break
            except Exception as err:
                # Ignore the error since it is handled afterwards
                pass

        # Stop if no vaid paths were found
        if not succeeded:
            raise Exception()

        # Stall until process is finished if not running in background.
        while not run_in_background and current_s_process.poll() is None:
            pass

    except KeyboardInterrupt:
        psutil.Process(current_s_process.pid).suspend()
        print(
            f'Process [{current_s_process.pid}] suspended. To resume, run "prs {current_s_process.pid}".')
    except Exception:
        raise
