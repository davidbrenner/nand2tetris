#!/usr/bin/env python3
# Author: David Brenner
"""Parser module handles parsing of a single .vm file"""

import re

# It would likely be more proper to write a proper lexer, but this will do.
# Very little to no error handling is done
class Parser(object):
    """Parser class"""

    C_ARITHMETIC = 0
    C_PUSH       = 1
    C_POP        = 2
    C_LABEL      = 3
    C_GOTO       = 4
    C_IF         = 5
    C_FUNCTION   = 6
    C_RETURN     = 7
    C_CALL       = 8

    _comment = re.compile(r'//.*$')

    def __init__(self, in_file):
        """Constructor - slurps entire file"""
        with open(in_file, 'r') as myf:
            self.lines = myf.readlines()
        self.command = ''
        self.cur_line = 0

    def has_more_commands(self):
        """Returns true if more commands are in the input"""
        if (self.cur_line + 1) < len(self.lines):
            return True
        else:
            return False

    def advance(self):
        """Reads next command, makes it the current command"""
        # strip comments
        self.cur_line += 1
        line = self.lines[self.cur_line]
        # Debug
        #print("cur line: ", line.rstrip())
        line = self._comment.sub('', line)
        if line == '\n':
            self.advance()
        else:
            self.command = line.strip()

    def command_type(self):
        """Returns the type of the current command"""
        pass

    def arg1(self):
        """Returns the first argument of the current command"""
        # In the case of C_ARITHMETIC, the command itself is returned
        # Should not be called if the current command is C_RETURN
        pass

    def arg2(self):
        """Returns the second argument of the current command"""
        # Should be called only if the current command is C_PUSH, C_POP,
        # C_FUNCTION, or C_CALL
        pass
