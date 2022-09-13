#!/usr/bin/env python3

# TODO: check if no HLT, add end of line comments, add debug mode

def assemble(programFile):
  filler = "000" # pattern to fill lower part of register (for ADD/HLT/etc.)
  with open(programFile, "r") as program:
    for line in program:
      if line[0] == "#" or line == "\n": # ignore comments or blank lines
        pass
      else:
        fields = line.strip("\n").split(" ")
        # print(fields)
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
                fields[index] = padded
              else:
                value = field[2:]
                fields[index] = "0"*(4-len(value))+value
        # print(fields)

        match fields[0]:
          case "ADD": # A = A + B
            print(f"0{filler}")
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
  args = parser.parse_args()

  assemble(args.programFile)