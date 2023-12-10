import psutil

from shell.commands.base import Command


class ProcessSuspend(Command):
    name = "process_suspend"
    alias = "psp"
    description = "Suspends a process with the specified process id."
    usage = "process_suspend <pid>"

    @staticmethod
    def exec(args):
        if len(args) == 0:
            print(ProcessSuspend.usage)
            return

        pid = args[0]
        if not psutil.pid_exists(int(pid)):
            print(f"No such process exists with process id {pid}.")
            return

        process = psutil.Process(int(pid))
        if process.status() == psutil.STATUS_RUNNING:
            print(f'Process [{pid}] suspended. To resume, run "prs {pid}".')
            process.suspend()
        else:
            print(f"Process [{pid}] is not running.")
