import psutil

from shell.commands.base import Command


class ProcessKill(Command):
    name = "process_kill"
    alias = "pkl"
    description = "Kills a process with the specified process id."
    usage = "process_kill <pid>"

    @staticmethod
    def exec(args):
        if len(args) == 0:
            print(ProcessKill.usage)
            return

        pid = args[0]
        if not psutil.pid_exists(int(pid)):
            print(f"No such process exists with process id {pid}.")
            return

        try:
            process = psutil.Process(int(pid))
            process.kill()
        except Exception as err:
            print(err)
            print(f"Unable to kill process with Process [{pid}]: {str(err)}")
            return

        print(f"Process [{pid}] killed.")
