from sys import stdin, stdout

class hydrothermalVents:
    def __init__(self, inputText):
        self.lines = []
        self.table = []
        maxX = 0
        maxY = 0
        for line in inputText:
            twoPoints = line.split(" -> ")
            startingPoint = list(map(int, twoPoints[0].split(",")))
            endingPoint = list(map(int, twoPoints[1].split(",")))
            self.lines.append([startingPoint, endingPoint])
        for i in self.lines:
            if i[0][0] > maxX:
                maxX = i[0][0]
            if i[1][0] > maxX:
                maxX = i[1][0]
            if i[0][1] > maxY:
                maxY = i[0][1]
            if i[1][1] > maxY:
                maxY = i[1][1]
        for i in range(maxX+1):
            self.table.append([])
            for j in range(maxY+1):
                self.table[i].append(0)
    def showLines(self):
        for line in self.lines:
            print(line)
    def showTable(self):
        for line in self.table:
            print(line)
    def doInstructions(self):
        for line in self.lines:
            #self.showTable(); print("\n")
            # vízszíntes mozgás
            if line[0][0] == line[1][0]:
                # jobbra mozgás
                if line[0][1] < line[1][1]:
                    for i in range(line[0][1], line[1][1]+1):
                        self.table[line[0][0]][i] += 1
                # balra mozgás
                else:
                    for i in range(line[0][1], line[1][1]-1, -1):
                        self.table[line[0][0]][i] += 1
            # függőleges mozgás
            elif line[0][1] == line[1][1]:
                # felfele mozgás
                if line[0][0] < line[1][0]:
                    for i in range(line[0][0], line[1][0]+1):
                        self.table[i][line[0][1]] += 1
                # lefele mozgás
                else:
                    for i in range(line[0][0], line[1][0]-1, -1):
                        self.table[i][line[0][1]] += 1
            # kétirányú mozgás
            else:
                # jobbra felfele mozgás
                if line[0][0] < line[1][0] and line[0][1] < line[1][1]:
                    for i in range(line[0][0], line[1][0]+1):
                        j = line[0][1] + (i-line[0][0])
                        self.table[i][j] += 1
                # jobbra lefele mozgás
                elif line[0][0] < line[1][0] and line[0][1] > line[1][1]:
                    for i in range(line[0][0], line[1][0]+1):
                        j = line[0][1] - (i - line[0][0])
                        self.table[i][j] += 1
                # balra felfele mozgás
                elif line[0][0] > line[1][0] and line[0][1] < line[1][1]:
                    for i in range(line[0][0], line[1][0]-1, -1):
                        j = line[0][1] + (line[0][0] - i)
                        print(f"i: {i}, j: {j}")
                        self.table[i][j] += 1
                # balra lefele mozgás
                elif line[0][0] > line[1][0] and line[0][1] > line[1][1]:
                    for i in range(line[0][0], line[1][0]-1, -1):
                        j = line[0][1] - (line[0][0] - i)
                        self.table[i][j] += 1
    def getResult(self):
        result = 0
        for line in self.table:
            for i in line:
                if i >= 2:
                    result += 1
        return result
def main():
    stdout.write("Please enter input filename: \n")
    inputFileName = (str(stdin.readline())).replace("\n", "")
    inputText = (open(inputFileName, "r").read()).split("\n")
    vents = hydrothermalVents(inputText)
    vents.doInstructions()
    result = vents.getResult()
    stdout.write(f"Result: {result}\n")
if __name__ == "__main__":
    main()