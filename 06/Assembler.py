#!/usr/bin/env python3
# Author: David Brenner
"""Assembler for Hack nand2tetris computer"""
# Assembler.py Hack_file.asm
# Creates Hack_file.hack containing assembled machine code

import sys
import Parser
import Code
import SymbolTable

class Assembler(object):
    """Assembler class"""

    def __init__(self, in_file):
        """Constructor"""
        self.in_file = in_file
        self.out_file = self._get_out_file(in_file)
        self.symbol_table = SymbolTable.SymbolTable()
        self.symbol_address = 16 # symbol addresses start at 16

    def assemble(self):
        """Assembles the code"""
        self.first_pass()
        self.second_pass()


    def first_pass(self):
        """First pass to construct symbol table"""
        parser = Parser.Parser(self.in_file)
        cur_address = 0
        while parser.has_more_commands():
            parser.advance()
            if parser.command_type() == parser.A_COMMAND \
                    or parser.command_type() == parser.C_COMMAND:
                cur_address += 1
            elif parser.command_type() == parser.L_COMMAND:
                self.symbol_table.add_entry(parser.symbol(), cur_address)

    def second_pass(self):
        """Second pass does assembly"""
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


    def _get_address(self, symbol):
        """Return symbol address"""
        if symbol.isdigit():
            return symbol
        else:
            if not self.symbol_table.contains(symbol):
                self.symbol_table.add_entry(symbol, self.symbol_address)
                self.symbol_address += 1
            return self.symbol_table.get_address(symbol)

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
