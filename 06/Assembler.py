#!/usr/bin/env python3
# Author: David Brenner
"""Assembler for Hack nand2tetris computer"""

import sys
import Parser
import Code
#import SymbolTable

class Assembler(object):
    """Assembler class"""

    def __init__(self, in_file):
        """Constructor"""
        self.in_file = in_file
        self.out_file = self._get_out_file(in_file)

    def assemble(self):
        """Assembles the code"""
        parser = Parser.Parser(self.in_file)
        outf = open( self.out_file, 'w')
        code = Code.Code()
        while(parser.has_more_commands()):
            parser.advance()
            if parser.command_type() == parser.A_COMMAND:
                outf.write(code.gen_a_code(self._get_address(parser.symbol()))
                        + '\n')
            elif parser.command_type() == parser.C_COMMAND:
                outf.write(code.gen_c_code(parser.comp(), parser.dest(),
                    parser.jump()) + '\n')
            elif parser.command_type == parser.L_COMMAND:
                pass
        outf.close()


    @staticmethod
    def _get_address(symbol):
        """Return symbol address (eventually lookup in SymbolTable)"""
        if symbol.isdigit():
            return symbol

    @staticmethod
    def _get_out_file(in_file):
        """translate file name to output filename"""
        if in_file.endswith('.asm'):
            return in_file.replace('.asm', '.hack')
        else:
            return in_file + '.hack'


def main():
    """Main method"""
    in_file = ""
    if len(sys.argv) !=2:
        print("Usage: Assembler.py file.asm")
    else:
        in_file = sys.argv[1]

    asm = Assembler(in_file)
    asm.assemble()

main()
