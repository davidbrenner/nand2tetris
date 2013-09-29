#!/usr/bin/env python3
# Author: David Brenner
"""CodeWrite module for VM translator"""

class CodeWrite(object):
    """CodeWrite class"""

    def __init__(self):
        """Opens the output stream and prepares it for writing"""
        pass

    def set_file_name(self, file_name):
        """Sets the translation that a new VM file is started"""
        pass

    def write_arithmetic(self, command):
        """Writes the assembly code translation of given arithmetic command"""
        pass

    def write_push_pop(self, command, segment, index):
        """Writes assembly code translation of current C_PUSH/C_POP command"""
        pass

    def close(self):
        """Closes output file"""
        pass
