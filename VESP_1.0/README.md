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
  -d, --debug           enable debug info
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
MOV B 0x40 # '0x' means its an addr
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
## Debug example:
`-d` enables debug info, showing how VESPa modifies values before turning them into VESP instructions
```sh
❯ ./VESPa.py -p examples/test.vspa -d
+['LDA', 'A', '0']
++['LDA', '0000', '0000']
2000
0000
+['LDA', 'B', '0']
++['LDA', '0001', '0000']
2001
0000
+['LDA', '0x40', '0xa']
++['LDA', '0040', '000a']
2040
000a
+['LDA', '0x3F', '17']
++['LDA', '003F', '0011']
203F
0011
+['LDA', 'A', '8']
++['LDA', '0000', '0008']
2000
0008
+['MOV', 'B', '0x40']
++['MOV', '0001', '0040']
3001
0040
+['ADD']
++['ADD']
0000
+['HLT']
++['HLT']
7000
```