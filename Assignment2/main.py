#!/usr/bin/env python3

"""The runner of the project."""

__version__ = '1.0.0'
__author__ = 'hharutyunyan'
__copyright__ = 'Copyright 2019, hharutyunyan'
__license__ = 'All Rights Reserved'
__maintainer__ = 'hharutyunyan'
__status__ = "Development"

import os
import sys

from Move import Mover, MoverThread, MoverProcess
from progress import progress_bar


def main() -> None:
    """Move files between directories.

    Creates two directories and populating one with 1024 * 256
    arbitrary files of size 1MiB. Then using the Move package to move
    files between the directories using different methods.

    """
    if not os.path.exists('files'):
        os.mkdir('files')

        total_no_files = 1024 * 256
        sys.stdout.write(
            "\033[1mFolder with arbitrary files is not found.\033[0m\n"
            "Creating it.\n")
        for i in range(total_no_files):
            progress_bar(i, total_no_files, prefix='Creating Files:')
            with open(os.path.join('files', 'file.{}'.format(i)), 'wb') as f:
                f.seek(1024 * 1024)
                f.write(b"\0")

        sys.stdout.write('\n\n')

    if not os.path.exists('files_new'):
        os.mkdir('files_new')

    mover = Mover()
    mover.move()

    mover_process = MoverProcess()
    mover_process.move()

    mover_process = MoverThread()
    mover_process.move()


if __name__ == '__main__':
    main()
