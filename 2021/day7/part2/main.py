from sys import stdin, stdout

def avg(lst):
    return sum(lst) / len(lst)

def main():
    stdout.write("Please enter input filename: \n")
    inputFileName = (str(stdin.readline())).replace("\n", "")
    inputText = (open(inputFileName, "r").read()).split(",")
    crabs = list(map(int, inputText))
    averageDifferences = []
    calculateFuel = lambda positionOne, positionTwo: sum(list(range(1, abs(positionOne-positionTwo)+1)))
    for i in crabs:
        differences = []
        for j in crabs:
            differences.append(calculateFuel(i, j))
        averageDifferences.append(avg(differences))
    # averageDifferences stores the average fuel needed between each pair of locations
    alignTo = crabs[averageDifferences.index(min(averageDifferences))]
    print(alignTo)
    differences = list(map(lambda crab: calculateFuel(crab, alignTo), crabs))
    minimalFuel = sum(differences)
    stdout.write(f"Solution: {minimalFuel} \n")
if __name__ == "__main__":
    main()