# VESPa 1.0
Assembler for the VESP 1.0 instruction set

VESPa supports comments, automatic converstion of hex and decimal values, etc. (see the example below)

__Note:__ VESPa currently (only) does the ADD, LDA, MOV, and HLT instructions.

## Usage:
```sh
❯ ./VESPa.py -h
usage: VESPa.py [-h] [-p PROGRAMFILE]

Assemble VESPa assembly to VESP instructions

options:
  -h, --help            show this help message and exit
  -p PROGRAMFILE, --program PROGRAMFILE
                        VESPa file to assemble
```

## Example:
```sh
❯ cat examples/test.vspa
# A = 8 + MEM[0x40]

# initializing A, B, MEM[0x40]
LDA A 0 # could load an 8 here
LDA B 0
LDA 0x40 0xa # hex case doesnt matter

# just for showing off
LDA 0x3F 17 # will do decimal -> hex :D

# doing 8 + MEM[0x40]
LDA A 8
MOV B 0x40 # '0x' means its a register
ADD

HLT

❯ ./VESPa.py -p examples/test.vspa | tee examples/test.vsp
2000
0000
2001
0000
2040
000a
203F
0011
2000
0008
3001
0040
0000
7000
```