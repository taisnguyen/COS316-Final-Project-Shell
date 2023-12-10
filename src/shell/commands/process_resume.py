import psutil

from shell.commands.base import Command


class ProcessResume(Command):
    name = "process_resume"
    alias = "prs"
    description = "Resumes a process with the specified process id."
    usage = "process_resume <pid>"

    @staticmethod
    def exec(args):
        if len(args) == 0:
            print(ProcessResume.usage)
            return

        pid = args[0]
        if not psutil.pid_exists(int(pid)):
            print(f"No such process exists with process id {pid}.")
            return

        process = psutil.Process(int(pid))
        if process.status() == psutil.STATUS_STOPPED:
            print(f"Process [{pid}] resumed.")
            process.resume()
        else:
            print(f"Process [{pid}] is not suspended.")
