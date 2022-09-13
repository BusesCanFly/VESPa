#!/usr/bin/env python3

# TODO: check if no HLT, add end of line comments, add debug mode

def assemble(programFile):
  def debug(fields, passNum: int):
    if args.debug:
      header = "+"*passNum
      try:
        comment = fields.index("#")
        print(f"{header}{fields[:comment]}")
      except ValueError: # no comments in line
        print(f"{header}{fields}") 

  filler = "000" # pattern to fill lower part of register (for ADD/HLT/etc.)
  with open(programFile, "r") as program:
    for line in program:
      if line[0] == "#" or line == "\n": # ignore comments or blank lines
        pass
      else:
        fields = line.strip("\n").split(" ")
        debug(fields, 1)
        for index, field in enumerate(fields):
          if "#" in field: # end of line comments
            break
          elif field == "A":
            fields[index] = "0000"
          elif field == "B":
            fields[index] = "0001"
          else:
            if index !=0: # TODO: this can be cleaned up
              if "0x" not in field:
                rawhex = hex(int(field))[2:]
                padded = "0"*(4-len(rawhex))+rawhex
                fields[index] = padded.upper()
              else:
                value = field[2:].upper()
                fields[index] = "0"*(4-len(value))+value
        debug(fields, 2)

        match fields[0]:
          case "ADD": # A = A + B
            print(f"0{filler}")
          case "SUB": #A = B - A
            print(f"1000\n0{filler}\n2001\n0001\n0{filler}") # TODO: make pseudo-instructions reference cases
          case "CMP": # A = ~A
            print(f"1{filler}")
          case "LDA": # M[IR[3:15] ] = M[MAR+1]
            print(f"2{fields[1][1:4]}\n{fields[2]}")
          case "MOV": # M[IR[3:15] ] = M[M[MAR+1][3:15]]
            print(f"3{fields[1][1:4]}\n{fields[2]}")
          case "JMP":
            pass
          case "JEZ":
            pass
          case "JPS":
            pass
          case "HLT":
            print(f"7{filler}", end="")

if __name__ == "__main__":
  import argparse
  parser = argparse.ArgumentParser(description='Assemble VESPa assembly to VESP instructions')
  parser.add_argument('-p', '--program', dest='programFile', help='VESPa file to assemble')
  parser.add_argument('-d', '--debug', dest='debug', action='store_true', help='enable debug info')
  args = parser.parse_args()

  assemble(args.programFile)