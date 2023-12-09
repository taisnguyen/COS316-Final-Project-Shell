'''Contains all application exceptions.'''


class ShellException(Exception):
    """Base Shell exception."""


class ConfigurationError(ShellException):
    """Configuration exception."""


class CommandNotExistsError(ShellException):
    """Command does not exist exception."""
