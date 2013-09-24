#!/usr/bin/env python3
# Author: David Brenner
"""SymbolTable module for Hack nand2tetris computer"""

class SymbolTable(object):
    """SymbolTable  class"""

    _symbols = {
            'SP': 0, 'LCL':1, 'ARG':2, 'THIS':3, 'THAT':4,
            'R0':0, 'R1':1, 'R2':2, 'R3':3, 'R4':4, 'R5':5, 'R6':6, 'R7':7,
            'R8':8, 'R9':9, 'R10':10, 'R11':11, 'R12':12, 'R13':13, 'R14':14,
            'R15':15, 'SCREEN':0x4000, 'KBD':0x600}

    def __init__(self):
        """Constructor"""
        pass

    def add_entry(self, symbol, address):
        """Adds the pair (symbol, address) to the table"""
        self._symbols[symbol] = address

    def contains(self, symbol):
        """Returns true if the symbol table contains the given symbol"""
        return symbol in self._symbols

    def get_address(self, symbol):
        """Returns the address associated with the symbol"""
        return self._symbols[symbol]
