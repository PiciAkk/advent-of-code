from sys import stdin, stdout
import math

def main():
    stdout.write("Please enter input filename: \n")
    inputFileName = (str(stdin.readline())).replace("\n", "")
    inputText = (open(inputFileName, "r").read()).split("\n")

    expenseReport = list(map(int, inputText))
    matchingEntries = []

    for entry in expenseReport:
        for entryTwo in expenseReport:
            for entryThree in expenseReport:
                if entry+entryTwo+entryThree == 2020:
                    matchingEntries = [entry, entryTwo, entryThree]

    stdout.write(f"{math.prod(matchingEntries)}\n")
if __name__ == "__main__":
    main()