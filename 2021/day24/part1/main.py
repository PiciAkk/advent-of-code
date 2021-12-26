from sys import stdin, stdout
from aluCompiler import *

def main():
    stdout.write("Please enter input filename: \n")
    inputFileName = (str(stdin.readline())).replace("\n", "")
    inputText = (open(inputFileName, "r").read()).split("\n")
    compiler = ALUCompiler(inputText)
    accepted = []
    for i in range(10000000000000, 10000000000000):
        compiler.run(list(str(i)))
        if compiler.variables["z"] == 0:
            accepted.append(int(i))
    print(accepted)
    print(max(accepted))
if __name__ == "__main__":
    main()