"""Spawns and manages processes."""

import os
import subprocess
import psutil
import glob


def spawn_process(args, exec_bin_path, stdout=None, stdin=None, run_in_background=False):
    """Spawns a process with the given arguments."""

    # Keep track of current subprocess.
    current_s_process = None

    try:
        # Expand tildes first
        for i in range(1, len(args)):
            args[i] = os.path.expanduser(args[i])
        
        # Copy the executable name
        modified_args = [args[0]]

        # Try to do globbing
        for i in range(1, len(args)):
            glob_args = glob.glob(args[i])

            # If globbing succeeded, add each file path to the args
            if len(glob_args) != 0:
                modified_args.extend(glob_args)
            # If failed, just leave it as is
            else:
                modified_args.append(args[i])
        
        args = modified_args

        # Try to start a process for each path to find the first valid one
        bin_paths = exec_bin_path.split(";")
        succeeded = False

        for path in bin_paths:
            try:
                current_s_process = subprocess.Popen(
                    [os.path.join(path, args[0]), *args[1:]], stdout=stdout, stdin=stdin)
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
        
        # Return the stdout to allow for piping
        return current_s_process.stdout

    except KeyboardInterrupt:
        psutil.Process(current_s_process.pid).suspend()
        print(
            f'Process [{current_s_process.pid}] suspended. To resume, run "prs {current_s_process.pid}".')
    except Exception:
        raise
