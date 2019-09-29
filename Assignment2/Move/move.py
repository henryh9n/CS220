#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Move the files between directories using synchronous calls of
`shutil.move` method."""

__version__ = '1.0.0'
__author__ = 'hharutyunyan'
__copyright__ = 'Copyright 2019, hharutyunyan'
__license__ = 'All Rights Reserved'
__maintainer__ = 'hharutyunyan'
__status__ = "Development"

import os
import sys
import time
import shutil
from progress import progress_bar
from functools import wraps


def _time(func):
    """Print the performance time for the decorated function."""

    @wraps(func)
    def time_func(*args, **kwargs):
        start_time = time.perf_counter()

        res = func(*args, **kwargs)

        sys.stdout.write(
            "\nDuration of the process: \033[1m{duration}\033[0m\n\n".format(
                duration=time.perf_counter() - start_time
            )
        )

        return res

    return time_func


class Mover:
    """A class for moving files between directories.

    Attributes
    ----------
    primary_directory : str
        The name of the primary directory with the files to be moved.
    secondary_directory : str
        The name of the directory where the files from the
        `primary_directory` should be moved.

    """

    primary_directory = 'files'
    secondary_directory = 'files_new'

    def __init__(self) -> None:
        """Creating a mover object to do the job.

        It checks for the directories and determines the
        `primary_directory`, which is the directory populated with
        arbitrary files.

        """
        self._check_folder()

    @_time
    def move(self) -> None:
        """Move the files between directories.

        The default method to move the files from `primary_directory`
        to the `secondary_directory`. Uses `shutil.move` method to
        move files between the directories.

        """
        sys.stdout.write(
            "\033[1mMoving the files from `{primary_folder}` to "
            "`{secondary_folder}`\033[0m\n".format(
                primary_folder=self.primary_directory,
                secondary_folder=self.secondary_directory
            )
        )

        files = os.listdir(self.primary_directory)
        for i, f in enumerate(files):
            self._move(f)
            progress_bar(i, len(files), prefix="Moving Files:")
        sys.stdout.write("\n")

    def _move(self, file_name: str) -> None:
        """Move the given file.
        """
        shutil.move(os.path.join(self.primary_directory, file_name),
                    os.path.join(self.secondary_directory, file_name))

    def _check_folder(self) -> None:
        """check if the folders exist and are populated.
        """
        if os.listdir(self.secondary_directory):
            self.primary_directory, self.secondary_directory = \
                self.secondary_directory, self.primary_directory
        else:
            if not os.listdir(self.primary_directory):
                raise MoverException("No files to move")


class MoverException(Exception):
    """ Custom exception class for Mover objects.

    Parameters
    ----------
    msg : str
        Human readable string describing the exception.
    code : :obj:`int`, optional
        Numeric error code.

    Attributes
    ----------
    msg : str
        Human readable string describing the exception.
    code : int
        Numeric error code.

    """
    pass
