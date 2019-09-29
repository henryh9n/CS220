#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Simple progress bar to show the progress in stdout."""

__version__ = '0.0.1'
__author__ = 'hharutyunyan'
__copyright__ = 'Copyright 2019, hharutyunyan'
__license__ = 'All Rights Reserved'
__maintainer__ = 'hharutyunyan'
__status__ = "Production"

import sys
import shutil


def progress_bar(iteration: int, total: int, prefix: str = '',
                 suffix: str = '') -> None:
    """Output simple progress bar to stdout.

    Takes as an input the total number of iterations and current
    iteration number and outputs a progress bar to the standard output
    evaluating the width of the window in use.

    Parameters
    ----------
    iteration : int
        The number of current iteration in progress.
        Should be a positive integer less that `total`.
    total : int
        The total number of iterations to be performed.
        Should be a positive integer.
    prefix: str, optional
        A string to append to the beginning of the progress bar.
    suffix : str, optional
        A string to append after the progress bar.

    Notes
    -----
    This is a very basic implementation and doesn't have checking for
    the passed parameters which is left for you to ensure the proper
    arguments.

    Examples
    --------
    >>> progress_bar(10, 100, prefix="Progress:", suffix="18s left")
    Progress: [====----------------------------------] 10.0% 18s left

    """
    columns, _ = shutil.get_terminal_size(fallback=(80, 24))
    bar_len = columns - (len(suffix) + 2) - (len(prefix) + 2) - 7
    percent = iteration / total
    fill_len = int(bar_len * percent) + 1
    bar = '=' * fill_len + '-' * (bar_len - fill_len)
    sys.stdout.write(
        '{prefix} [{bar}] {percent}% {suffix}\r'.format(
            prefix=prefix,
            bar=bar,
            percent=round(percent * 100, 1),
            suffix=suffix
        )
    )
    sys.stdout.flush()
