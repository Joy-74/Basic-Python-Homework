#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 00:00:00 2020

@author: mjandr
"""

# This example has tutorial import i4 which itself imports tutorial.
# This example allows you to follow the exact order of imports, and
# it demonstrates the functionality of __name__ explicity.

# Run this file; running i4.py is less exciting.
# Refresh the console after each run.


print('1  :  tutorial.py is executing; ', '__name__ ==', __name__)
import i4
print('2  :  tutorial.py is executing; ', '__name__ ==', __name__)


if __name__ != '__main__':

    print('2.5:  tutorial.py is executing; ', '__name__ ==', __name__, '*** init v')
    v = 8  # Creates a variable called v in the namespace tutorial.

    # print('i4.v ==', i4.v)
    # Uncommenting this does NOT lead to an error.
    # Another v has already been added to i4's namespace.

    # print('i4.tutorial ==', i4.tutorial)
    # Uncommenting this DOES lead to an error.
    # tutorial is not added to i4's namespace until after
    # (tutorial.py with __name__ == 'tutorial') finishes executing.


if __name__ == '__main__':

    try:
        print('')
        print(v)

    except NameError:
        print('There is no v in __main__')
        print('')

    print('i4.tutorial.v ==', i4.tutorial.v)
    print('i4.tutorial.i4.tutorial.v ==', i4.tutorial.i4.tutorial.v)
    print('i4.tutorial.v is i4.tutorial.i4.tutorial.v ==', i4.tutorial.v is i4.tutorial.i4.tutorial.v)
    print('')

    print('i4.v ==', i4.v)
    print('i4.tutorial.i4.v ==', i4.tutorial.i4.v)
    print('i4.v is i4.tutorial.i4.v ==', i4.v is i4.tutorial.i4.v)
    print('')


print('3  :  tutorial.py is executing; ', '__name__ ==', __name__)