#!/usr/bin/python3.5
# -*- coding: iso-8859-1 -*-

import sys
import os

path = os.path.dirname(__file__)
sys.path.extend([path])

import module1

NAME = '€‚ƒ„…†‡ˆ‰Š‹ŒŽ‘’“”•'

module1.print_my_char(NAME)
