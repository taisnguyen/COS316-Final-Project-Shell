"""Base code for commands."""


class Command:
    """Base class for commands."""
    name = ""
    alias = ""
    description = ""

    @staticmethod
    def exec(args):
        """Executes command."""
        raise NotImplementedError
