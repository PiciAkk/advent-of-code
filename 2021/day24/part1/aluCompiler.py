from sys import stdin, stdout
import math

class inputReader:
    def __init__(self, inputText):
        self.lineCounter = 0
        self.inputText = inputText
    def readLine(self):
        self.lineCounter += 1
        return str(self.inputText[self.lineCounter])

class ALUCompiler:
    def __init__(self, code):
        self.code = list(map((lambda instruction: instruction.split(" ")), code))
        self.variables = {"w": 0, "x": 0, "y": 0, "z": 0}
        self.instructions = {
            "inp": self.inp,
            "add": self.add,
            "mul": self.mul,
            "div": self.div,
            "mod": self.mod,
            "eql": self.eql
        }
    def isParamAVar(self, param):
        return param in self.variables.keys()
    def inp(self, a):
        self.variables[a] = self.inputText.readLine()
    def add(self, a, b):
        if self.isParamAVar(b):
            self.variables[a] = self.variables[b] + self.variables[a]
        else:
            self.variables[a] = int(b) + self.variables[a]
    def mul(self, a, b):
        if self.isParamAVar(b):
            self.variables[a] = self.variables[b] * self.variables[a]
        else:
            self.variables[a] = int(b) * self.variables[a]
    def div(self, a, b):
        if self.isParamAVar(b):
            self.variables[a] = math.ceil(self.variables[b] / self.variables[a])
        else:
            self.variables[a] = math.ceil(int(b) / self.variables[a])
    def mod(self, a, b):
        if self.isParamAVar(b):
            self.variables[a] = self.variables[b] % self.variables[a]
        else:
            self.variables[a] = int(b) % self.variables[a]
    def eql(self, a, b):
        if self.isParamAVar(b):
            self.variables[a] = int(self.variables[a] == self.variables[b])
        else:
            self.variables[a] = int(self.variables[a] == int(b))
    def run(self, inputList):
        self.inputText = inputReader(inputList)
        for line in self.code:
            if len(line) > 2:
                self.instructions[line[0]](line[1], line[2])
            else:
                self.instructions[line[0]](line[1])