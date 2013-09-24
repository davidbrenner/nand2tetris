#!/usr/bin/env python3
# Author: David Brenner
"""Parser module for Hack nand2tetris computer"""

import re

# It would likely be more proper to write a proper lexer, but this will do.
# Very little to no error handling is done
class Parser(object):
    """Parser class"""

    A_COMMAND = 0
    C_COMMAND = 1
    L_COMMAND = 2
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
        if re.match(r'^@.*', self.command):
            return Parser.A_COMMAND
        elif re.match(r'^\(.*', self.command):
            return Parser.L_COMMAND
        else:
            return Parser.C_COMMAND

    def symbol(self):
        """Returns the symbol of the current command @Xxx or (Xxx)"""
        matching = re.match(r'^[@\(](.*?)\)?$', self.command)
        symbol = matching.group(1)
        return symbol

    def dest(self):
        """Returns the dest mnemonic in the current C-command"""
        # dest=comp;jump
        matching = re.match(r'^(.*?)=.*$', self.command)
        if not matching:
            dest = ''
        else:
            dest = matching.group(1)
        return dest

    def comp(self):
        """Returns the comp mnemonic in the current C-command"""
        # dest=comp;jump
        # remove dest and jump (if they exist) to get comp
        comp = re.sub(r'^.*?=', '', self.command) # remove dest
        comp = re.sub(r';\w+$', '', comp) # remove jump
        if not comp:
            print("No comp!")
            print(self.command)
        return comp.strip()

    def jump(self):
        """Returns the jump mnemonic in the current C-command"""
        # dest=comp;jump
        matching = re.match(r'^.*;(\w+)$', self.command)
        if not matching:
            jump = ''
        else:
            jump = matching.group(1)
        return jump
