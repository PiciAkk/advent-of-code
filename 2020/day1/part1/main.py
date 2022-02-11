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
            if entry+entryTwo == 2020:
                matchingEntries = [entry, entryTwo]

    stdout.write(f"{math.prod(matchingEntries)}\n")
if __name__ == "__main__":
    main()