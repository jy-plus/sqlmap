#!/usr/bin/env python

"""
Copyright (c) 2006-2013 sqlmap developers (http://sqlmap.org/)
See the file 'doc/COPYING' for copying permission
"""

import binascii

from lib.core.common import isDBMSVersionAtLeast
from plugins.generic.syntax import Syntax as GenericSyntax

class Syntax(GenericSyntax):
    def __init__(self):
        GenericSyntax.__init__(self)

    @staticmethod
    def escape(expression, quote=True):
        def escaper(value):
            retVal = value
            if isDBMSVersionAtLeast('3'):
                retVal = "X'%s'" % binascii.hexlify(value)
            return retVal

        return Syntax._escape(expression, quote, escaper)
