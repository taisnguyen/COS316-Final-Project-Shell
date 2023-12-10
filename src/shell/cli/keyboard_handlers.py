"""Code to handle keyboard input in the Shell."""

import signal


def handler(signum, frame):
    print('Ctrl+Z pressed, but ignored')


# signal.signal(signal.T, handler)
