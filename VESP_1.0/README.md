# VESPa 1.0
Assembler for the VESP 1.0 instruction set

VESPa supports comments, automatic converstion of hex and decimal values, etc. (see the example below)

__Note:__ VESPa currently (only) does the ADD, LDA, MOV, and HLT instructions.
* Extra note: VESPa now has a `SUB` pseudo-instruction (`A = B - A`)

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
### VESPa program: 
(featuring `SUB` pseudo-instruction)
```sh
❯ cat examples/subtract.vspa
# Test program to show off subtraction
# MEM[0x30] = 0xAF - 16 # should be 0x9F

# set up
LDA A 0 # can do comments!
LDA B 0

# handles hex and decimal conversions for you!
LDA B 0xaf # hex case doesnt matter
LDA A 16

SUB # A = B - A (does 2's complement for you)

MOV 0x30 A # load answer into MEM[0x30]

HLT
```

### Generating VESP machine code:
```
❯ ./VESPa.py -p examples/subtract.vspa | tee examples/subtract.vsp
2000
0000
2001
0000
2001
00AF
2000
0010
1000
0001
2001
0001
0001
3030
0000
7001
```

### Debug Example:    
This shows the process the assember takes so you can sanity check it          
```sh
❯ ./VESPa.py -p examples/subtract.vspa -d
+['LDA', 'A', '0']
++['LDA', '0000', '0000']
2000
0000
+['LDA', 'B', '0']
++['LDA', '0001', '0000']
2001
0000
+['LDA', 'B', '0xaf']
++['LDA', '0001', '00AF']
2001
00AF
+['LDA', 'A', '16']
++['LDA', '0000', '0010']
2000
0010
+['SUB']
++['SUB']
1000
0001
2001
0001
0001
+['MOV', '0x30', 'A']
++['MOV', '0030', '0000']
3030
0000
+['HLT']
++['HLT']
7001
```