"""Contains utility functions for CLI.."""

import os
import sys

from shell.utils.inputs import input_options
from shell.utils.ansi_colors import ANSIColors
from shell.exceptions import ConfigurationError

CONFIG_FILE_PATH = "shell.config"


def setup_config():
    """Sets up config file for CLI."""

    # Try to get the config file
    try:
        with open(CONFIG_FILE_PATH, "r") as config_file:
            # Config file already exists.
            return _parse_config_file(config_file)
    except FileNotFoundError:
        pass  # We are passing so we can prompt the user to create the file.
    except Exception as err:
        raise ConfigurationError(err)

    # Prompt to create a config file
    no_config_file_handler = lambda: sys.exit(f"{ANSIColors.FAIL}Terminating... No configuration file identified.{ANSIColors.ENDC}")
    input_options("It looks like there doesn't exist a configuration file for the Shell.\nWould you like to create one?", {
        "Y": None,
        "n": no_config_file_handler
    }, default_handler=no_config_file_handler)

    try:
        with open(CONFIG_FILE_PATH, "w") as config_file:
            print("# SHELL CONFIGURATION\n")
            config_file.write("# SHELL CONFIGURATION\n\n")

            # Directory for executable binaries.
            print("# Split paths with ';' for multiple paths.")
            config_file.write("# Split paths with ';' for multiple paths.\n")
            config_file.write(f"EXEC_BIN_PATH={input('EXEC_BIN_PATH=')}\n")

        with open(CONFIG_FILE_PATH, "r") as config_file:
            return _parse_config_file(config_file)

    except KeyboardInterrupt:
        os.remove(CONFIG_FILE_PATH)
        sys.exit(
            f"{ANSIColors.FAIL}\nTerminating... User aborted.{ANSIColors.ENDC}")
    except Exception as err:
        raise ConfigurationError(err)


def _parse_config_file(config_file):
    config_dict = {}
    for line in config_file:
        if line.startswith("#") or line.strip() == "":
            continue

        key, value = line.split("=")
        config_dict[key] = value.strip()

    return config_dict
