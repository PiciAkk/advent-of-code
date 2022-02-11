from sys import stdin, stdout

def main():
    stdout.write("Please enter input filename: \n")
    inputFileName = (str(stdin.readline())).replace("\n", "")
    inputText = (open(inputFileName, "r").read()).split("\n")

    calculateFuel = lambda mass: mass // 3 - 2
    modules = list(map(int, inputText))
    sumOfFuelRequirements = 0

    for module in modules:
        fuelRequirementsForModule = [calculateFuel(module)]
        while fuelRequirementsForModule[-1] > 0:
            fuelRequirementsForModule.append(calculateFuel(fuelRequirementsForModule[-1]))
        sumOfFuelRequirements += sum(fuelRequirementsForModule[:-1])

    stdout.write(f"{sumOfFuelRequirements}\n")
if __name__ == "__main__":
    main()