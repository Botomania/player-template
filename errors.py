"""
List of known errors, easier to manage
"""

import sys


class errors:
    """
    List of errors
    """

    SUBMISSION_IMPORT_ERROR = "Couldn't import submission"
    SUBMISSION_UNKNOWN_FORMAT = "Unknown format specified in submission"


def panic(error, exit_code=1):
    """
    Prints the error message and quits
    """
    print(error)
    sys.exit(exit_code)
