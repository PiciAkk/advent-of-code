from sys import stdin, stdout
from copy import deepcopy

def main():
    stdout.write("Please enter input filename: \n")
    inputFilename = (str(stdin.readline())).replace("\n", "")
    inputText = (open(inputFilename, "r").read()).split("\n")

    IntcodeProgram = list(map(int, inputText[0].split(",")))
    IntcodeProgram[1] = 12
    IntcodeProgram[2] = 2
    newProgram = deepcopy(IntcodeProgram)
    for i in range(0, len(newProgram), 4):
        if newProgram[i] == 99: break
        opcode, a, b, c = newProgram[i:i+4]
        if opcode == 1: newProgram[c] = newProgram[a] + newProgram[b] 
        elif opcode == 2: newProgram[c] = newProgram[a] * newProgram[b]

    stdout.write(f"{newProgram[0]}\n")
if __name__ == "__main__": 
    main()