import psutil
from shell.commands.base import Command


class ProcessList(Command):
    name = "process_list"
    alias = "pl"
    description = "Lists all running processes."
    usage = "process_list"

    @staticmethod
    def exec(args):
        for proc in psutil.process_iter(["pid", "name"]):
            print(proc.info)
