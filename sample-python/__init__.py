"""
This file must be present in a python based submission

If the submission format is python,
    This file must expose a function named 'solution' with the signature

    def func(state):
        return newState

If the submission format is executable,
    There must be an executable named 'solution' which reads the state
    from stdin and writes it to stdout
"""
from . import config

if config.FORMAT == "python":
    from .solution import solution
