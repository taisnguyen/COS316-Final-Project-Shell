"""Provides ANSI color enums."""


class ANSIColors:
    # We are not using ANSI colors for now because there is a strange
    # behavior with calling subprocess.Popen() and subsequently using ANSI colors.
    HEADER = ""  # '\033[95m'
    OKBLUE = ""  # '\033[94m'
    OKCYAN = ""  # '\033[96m'
    OKGREEN = ""  # '\033[92m'
    WARNING = ""  # '\033[93m'
    FAIL = ""  # '\033[91m'
    ENDC = ""  # '\033[0m'
    BOLD = ""  # '\033[1m'
    UNDERLINE = ""  # '\033[4m'
