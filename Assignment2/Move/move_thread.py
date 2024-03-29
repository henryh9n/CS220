#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""The runner of the project."""

__version__ = '1.0.0'
__author__ = 'hharutyunyan'
__copyright__ = 'Copyright 2019, hharutyunyan'
__license__ = 'All Rights Reserved'
__maintainer__ = 'hharutyunyan'
__status__ = "Development"

import os
import sys
from progress import progress_bar
from Move.move import Mover, _time
from concurrent.futures import ThreadPoolExecutor


class MoverThread(Mover):
    """
    A class for moving files between directories.

    Implements threading for each of the move operations.

    Attributes
    ----------
    primary_directory : str
        The name of the primary directory with the files to be moved.
    secondary_directory : str
        The name of the directory where the files from the
        `primary_directory` should be moved.

    """

    @_time
    def move(self):
        """Move the files between directories.

        The default method to move the files from `primary_directory`
        to the `secondary_directory`. Uses Thread Pool and
        `shutil.move` method to perform the move operations.

        """
        sys.stdout.write(
            "\033[1mMoving the files from `{primary_folder}` to "
            "`{secondary_folder}` using threading\033[0m\n".format(
                primary_folder=self.primary_directory,
                secondary_folder=self.secondary_directory
            )
        )

        files = os.listdir(self.primary_directory)

        with ThreadPoolExecutor(max_workers=4) as executor:
            for i, f in enumerate(files):
                progress_bar(i, len(files), prefix="Moving Files:")
                executor.submit(self._move, f)
        sys.stdout.write("\n")
