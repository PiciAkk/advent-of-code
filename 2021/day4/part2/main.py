from sys import stdin, stdout
import re

class table:
    def __init__(self, tableList):
        self.table = tableList
        self.won = False
    def drawNumber(self, number):
        for line in range(len(self.table)):
            for char in range(len(self.table[line])):
                self.table[line][char] = "*" if self.table[line][char] == number else self.table[line][char]
    def didWin(self):
        perfect = list(map((lambda char: "*"), self.table[0]))
        columns = list(map((lambda line: []), self.table))
        for line in range(len(self.table)):
            if self.table[line] == perfect:
                self.won = True
                return True
            for char in range(len(self.table[line])):
                columns[char].append(self.table[line][char])
        if perfect in columns:
            self.won = True
            return True
        return False
    def show(self):
        [print(line) for line in self.table]
def formatInput(inputText):
    drawnNumbers = list(map(int, inputText[0].split(","))) # az első sora az inputnak
    tables = list(map(lambda inputString: ((re.sub(" +", " ", inputString)).strip()), inputText[1:len(inputText)]))
    newTables = []
    for i in range(len(tables)):
        if tables[i] == "":
            newTables.append(tables[i+1:i+6])
    tables = newTables
    del newTables
    for i in range(len(tables)):
        for j in range(len(tables[i])):
            tables[i][j] = list(map(int, tables[i][j].split(" ")))
    return drawnNumbers, tables
def main():
    stdout.write("Please enter input filename: \n")
    inputFileName = (str(stdin.readline())).replace("\n", "")
    inputText = (open(inputFileName, "r").read()).split("\n")
    drawnNumbers, tables = formatInput(inputText)
    tableInstances = list(map(table, tables))
    winners = []
    for i in drawnNumbers:
        for j in tableInstances:
            if j.won:
                continue
            j.drawNumber(i)
            if j.didWin():
                winners.append(i*sum(map((lambda line: sum(map((lambda char: 0 if char == "*" else char), line))), j.table)))
    stdout.write(f"{winners[-1]}\n")
if __name__== "__main__":
    main()