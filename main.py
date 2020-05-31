"""
Main file
Manages and starts the submission depending on format
"""

import os

import helpers
from errors import errors, panic

try:
    import submission.config as conf
except ImportError as e:
    print(e)
    panic(errors.SUBMISSION_IMPORT_ERROR)

AVAILABLE_FORMATS = ["python", "executable"]

if conf.FORMAT not in AVAILABLE_FORMATS:
    panic(errors.SUBMISSION_UNKNOWN_FORMAT)

if conf.FORMAT == "python":
    from submission import solution
elif conf.FORMAT == "executable":
    solution = "submission/solution"

    os.chmod(solution, 0o755)

helpers.run(conf.FORMAT, solution)
