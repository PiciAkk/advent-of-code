from sys import stdin, stdout

def main():
    stdout.write("Please enter input filename: \n")
    inputFileName = (str(stdin.readline())).replace("\n", "")
    inputText = (open(inputFileName, "r").read()).split("\n")

    calculateFuel = lambda mass: mass // 3 - 2
    modules = list(map(int, inputText))
    sumOfFuelRequirements = sum(map(calculateFuel, modules))

    stdout.write(f"{sumOfFuelRequirements}\n")
if __name__ == "__main__":
    main()