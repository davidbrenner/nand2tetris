// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/01/Not16.tst

load Nand16.hdl,
output-file Nand16.out,
compare-to Nand16.cmp,
output-list a%B1.16.1 b%B1.16.1 out%B1.16.1;

set a %B0000000000000000,
set b %B0000000000000000,
eval,
output;

set a %B1111111111111111,
set b %B0000000000000000,
eval,
output;

set a %B1111111111111111,
set b %B1111111111111111,
eval,
output;
