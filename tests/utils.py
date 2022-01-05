import os
import shlex
import subprocess
from contextlib import contextmanager
from typing import List


@contextmanager
def inside_dir(dirpath):
    """
    Execute code from inside the given directory
    :param dirpath: String, path of the directory the command is being run.
    """
    old_path = os.getcwd()
    try:
        os.chdir(dirpath)
        yield
    finally:
        os.chdir(old_path)


def run_command(command: str) -> int:
    return subprocess.check_call(shlex.split(command))
