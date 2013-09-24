#!/usr/bin/env python3
# Author: David Brenner
"""Parser module for Hack nand2tetris computer"""

# It would likely be more proper to write a proper lexer, but this will do.
class Parser(object):
    """Parser class"""

    A_COMMAND = 0
    C_COMMAND = 1
    L_COMMAND = 2

    def __init__(self, inFile):
        """Constructor"""
        pass

    def has_more_commands(self):
        """Returns true if more commands are in the input"""
        pass

    def advance(self):
        """Reads next command, makes it the current command"""
        pass

    def command_type(self):
        """Returns the type of the current command"""
        pass

    def symbol(self):
        """Returns the type of the current command"""
        pass

    def dest(self):
        """Returns the dest mnemonic in the current C-command"""
        pass

    def comp(self):
        """Returns the comp mnemonic in the current C-command"""
        pass

    def jump(self):
        """Returns the jump mnemonic in the current C-command"""
        pass
