import readline
import atexit
from pynput import keyboard
import subprocess
import os
import sys

history_file = os.path.expanduser("~/.cos316history")
history_file_length = 1000

# Load in history file and set max length
try:
    readline.read_history_file(history_file)
    readline.set_history_length(history_file_length)
except FileNotFoundError as e:
    print("Failed to open history file:", history_file)


# Write to the history file when closed
atexit.register(readline.write_history_file, history_file)


readline.parse_and_bind('tab: complete')

def execute_command(split_command):
    try:
        subprocess.run(split_command)
    except Exception as e:
        print(e)

while True:

    try:
        command = input("> ")
    except KeyboardInterrupt:
        print()
        sys.exit()
    
    split_command = command.split()
    
    if split_command[0] == "exit":
        break
    else:
        execute_command(split_command)