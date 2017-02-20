# -*- coding: utf-8 -*-

"""
These errors are produced when PyBEL cannot continue parsing, because of a technical problem, or unsalvagable
syntatic/semantic problem. These are logged at the CRITICAL level.
"""


class PyBelWarning(Exception):
    """PyBEL throws exceptions labeled PyBEL1xx for statements that cannot be fixed automatically"""

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return '{} - {}'.format(self.__class__.__name__, self.message)
