#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Move the files between directories using processes for calls of
`shutil.move` method."""

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
from multiprocessing import Pool, cpu_count


class MoverProcess(Mover):
    """
    A class for moving files between directories.

    Implements multiprocessing to make a process for each of the files
    being moved.

    Attributes
    ----------
    primary_directory : str
        The name of the primary directory with the files to be moved.
    secondary_directory : str
        The name of the directory where the files from the
        `primary_directory` should be moved.

    """

    @_time
    def move(self) -> None:
        """Move the files between directories.

        The default method to move the files from `primary_directory`
        to the `secondary_directory`. Uses process pool and
        `shutil.move` method to initialize a process for each
        move operation.

        """
        sys.stdout.write(
            "\033[1mMoving the files from `{primary_folder}` to "
            "`{secondary_folder}` using processing\033[0m\n".format(
                primary_folder=self.primary_directory,
                secondary_folder=self.secondary_directory
            )
        )

        files = os.listdir(self.primary_directory)

        pool = Pool(processes=cpu_count())

        for i, f in enumerate(files):
            pool.apply_async(self._move, (f,))
            progress_bar(i, len(files), prefix="Moving files:")

        pool.close()
        pool.join()

        sys.stdout.write("\n")
