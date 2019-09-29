#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Package for different types of file movers."""

__version__ = '0.0.1'
__author__ = 'hharutyunyan'
__copyright__ = 'Copyright 2019, hharutyunyan'
__license__ = 'All Rights Reserved'
__maintainer__ = 'hharutyunyan'
__status__ = "Production"

from .move import Mover
from .move_thread import MoverThread
from .move_proc import MoverProcess
