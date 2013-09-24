#!/usr/bin/env python3
# Author: David Brenner
"""Assembler for Hack nand2tetris computer"""

import sys
#import Parser
#import Code
#import SymbolTable

class Assembler(object):
    """Assembler class"""

    def __init__(self):
        """Constructor"""
        pass

    def assemble(self, file):
        """Assembles the code"""
        pass

    def blah(self):
        """initialize"""
        pass

def main():
    """Main method"""
    in_file = ""
    if len(sys.argv) !=2:
        print("Usage: Assembler.py file.asm")
    else:
        in_file = sys.argv[1]

    asm = Assembler()
    asm.assemble(in_file)

main()
