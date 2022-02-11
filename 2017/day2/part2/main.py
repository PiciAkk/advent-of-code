from copy import deepcopy
from sys import stdin, stdout

class spreadsheet:
    def __init__(self, spreadsheetMatrix):
        self.spreadsheetMatrix = spreadsheetMatrix
    def getDivisionResultsSum(self):
        return int(sum(list(map(self.calcDivisionResult, range(len(self.spreadsheetMatrix))))))
    def calcDivisionResult(self, rowIndex):
        for number in self.spreadsheetMatrix[rowIndex]:
            for otherNumber in self.spreadsheetMatrix[rowIndex]:
                if number != otherNumber and number % otherNumber == 0:
                    return number / otherNumber
def main():
    stdout.write("Please enter input filename: \n")
    inputFileName = (str(stdin.readline())).replace("\n", "")
    inputText = (open(inputFileName, "r").read()).split("\n")

    originalSpreadsheet = spreadsheet(list(map((lambda row: list(map(int, row.replace(" ", "\t").split("\t")))), inputText)))

    stdout.write(f"{originalSpreadsheet.getDivisionResultsSum()}\n")
if __name__ == "__main__":
    main()