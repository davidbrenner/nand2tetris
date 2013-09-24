#!/usr/bin/env python3
# Author: David Brenner
"""Code module for Hack nand2tetris computer"""

class Code(object):
    """Code class"""

    _dest_codes = ['', 'M', 'D', 'MD', 'A', 'AM', 'AD', 'AMD']
    _comp_codes = {
            '0':'0101010', '1':'0111111', '-1':'0111010', 'D':'0001100',
            'A':'0110000', '!D':'0001101', '!A':'0110001', '-D':'0001111',
            '-A':'0110011', 'D+1':'0011111','A+1':'0110111','D-1':'0001110',
            'A-1':'0110010','D+A':'0000010','D-A':'0010011','A-D':'0000111',
            'D&A':'0000000','D|A':'0010101',
            '':'xxxxxxx',
            'M':'1110000', '!M':'1110001', '-M':'1110011', 'M+1':'1110111',
            'M-1':'1110010','D+M':'1000010','D-M':'1010011','M-D':'1000111',
            'D&M':'1000000', 'D|M':'1010101' }
    _jump_codes = ['', 'JGT', 'JEQ', 'JGE', 'JLT', 'JNE', 'JLE', 'JMP']

    def __init__(self):
        """Code constructor"""
        pass

    def gen_a_code(self, address):
        """Returns the binary code for an a instruction"""
        return '0' + self._bits(address).zfill(15)

    def gen_c_code(self, comp, dest, jump):
        """Returns the binary code for a c instruction"""
        return '111' + self.comp(comp) + self.dest(dest) + self.jump(jump)

    def dest(self, mnemonic):
        """Returns the binary code of the dest mnemonic"""
        return self._bits(self._dest_codes.index(mnemonic)).zfill(3)

    def comp(self, mnemonic):
        """Returns the binary code of the comp mnemonic"""
        return self._comp_codes[mnemonic]

    def jump(self, mnemonic):
        """Returns the binary code of the jump mnemonic"""
        return self._bits(self._jump_codes.index(mnemonic)).zfill(3)

    @staticmethod
    def _bits(num):
        """Convert int n to binary"""
        return bin(int(num))[2:]
