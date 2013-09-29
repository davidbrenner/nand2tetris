#!/usr/bin/env python3
# Author: David Brenner
"""VM Translator (translates VM code to Hack)"""
# VMtranslator.py File.vm
# Creates File.asm containing translated VM code

import sys

class VMtranslator(object):
    """VMtranslator class"""

    def __init__(self, in_file):
        """Constructor"""
        self.in_file = in_file
        self.out_file = self._get_out_file(in_file)

    def translate(self):
        """Translate .vm to .asm"""
        pass

    @staticmethod
    def _get_out_file(in_file):
        """translate file name to output filename"""
        if in_file.endswith('.vm'):
            return in_file.replace('.vm', '.asm')
        else:
            return in_file + '.asm'

def main():
    """Main method"""
    in_file = ""
    if len(sys.argv) !=2:
        print("Usage: VMtranslator.py file.asm")
    else:
        in_file = sys.argv[1]

    vmt = VMtranslator(in_file)
    vmt.translate()

main()
