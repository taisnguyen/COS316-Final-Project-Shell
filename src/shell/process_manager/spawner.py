"""Spawns and manages processes."""

import os
import subprocess
import psutil

# Keep track of current subprocess.
CURRENT_S_PROCESS = None

# Keep track of all alive processes.
# ALIVE_PROCESSES = []


def spawn_process(args, exec_bin_path):
    """Spawns a process with the given arguments."""

    try:
        run_in_background = False
        args = args.split(" ")

        # Run process in background.
        if args[-1] == "&":
            run_in_background = True
            args = args[:-1]

        CURRENT_S_PROCESS = subprocess.Popen(
            [os.path.join(exec_bin_path, args[0]), *args[1:]])

        # Stall until process is finished if not running in background.
        while not run_in_background and CURRENT_S_PROCESS.poll() is None:
            pass

    except KeyboardInterrupt:
        psutil.Process(CURRENT_S_PROCESS.pid).suspend()
        print(
            f'Process [{CURRENT_S_PROCESS.pid}] suspended. To resume, run "prs {CURRENT_S_PROCESS.pid}".')
    except:
        raise
