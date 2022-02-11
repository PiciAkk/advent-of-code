from sys import stdin, stdout

class registers:
    def __init__(self):
        self.registers = {}
    def doInstructions(self, instructions):
        for instruction in instructions:
            splittedInstruction = instruction.split()

            for registerIndex in [0, 4]:
                register = splittedInstruction[registerIndex]
                if register not in self.registers:
                    self.registers.update({register: 0})
                splittedInstruction[registerIndex] = f"self.registers['{register}']"

            exec(" ".join(splittedInstruction).replace("dec", "-=").replace("inc", "+=") + "else 0")
    def findLargestValue(self): return max(self.registers.values())       

def main():
    stdout.write("Enter input filename: \n")
    inputFilename = stdin.readline().replace("\n", "")
    inputText = open(inputFilename, "r").readlines()

    reg = registers()
    reg.doInstructions(inputText)
    largestValue = reg.findLargestValue()

    stdout.write(f"{largestValue}\n")

main()