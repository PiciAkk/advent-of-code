from sys import stdin, stdout

class area:
    def __init__(self, heightMap):
        self.heightMap = heightMap
    def findLowPoints(self):
        lowPoints = []
        for i in range(len(self.heightMap)):
            for j in range(len(self.heightMap[i])):
                adjacents = []
                if j > 0:
                    # balra biztosan léphetünk, mert nem az első oszlopban vagyunk
                    adjacents.append(self.heightMap[i][j-1])
                if i > 0:
                    # fentre biztosan léphetünk, mert nem az első sorban vagyunk
                    adjacents.append(self.heightMap[i-1][j])
                if i < len(self.heightMap) - 1:
                    # lentre biztosan léphetünk, mert nem az utolsó sorban vagyunk
                    adjacents.append(self.heightMap[i+1][j])
                if j < len(self.heightMap[i]) - 1:
                    # jobbra biztosan léphetünk, mert nem az utolsó oszlopban vagyunk
                    adjacents.append(self.heightMap[i][j+1])
                isItALowPoint = []
                for k in adjacents:
                    if k > self.heightMap[i][j]:
                        isItALowPoint.append(True)
                    else:
                        isItALowPoint.append(False)
                if False not in isItALowPoint and True in isItALowPoint:
                    isItALowPoint = True
                    # lowPoints.append(self.heightMap[i][j])
        return lowPoints
    def findRiskLevels(self):
        return list(map((lambda lowPoint: lowPoint+1), self.findLowPoints()))
    def showArea(self):
        for line in self.heightMap:
            print(line)
def formatInput(inputText):
    formattedInput = []
    for line in inputText:
        formattedInput.append(list(map(int, list(line))))
    return formattedInput
def main():
    stdout.write("Please enter input filename: \n")
    inputFileName = (str(stdin.readline())).replace("\n", "")
    inputText = (open(inputFileName, "r").read()).split("\n")
    smokeArea = area(formatInput(inputText))
    print(smokeArea.findLowPointOf(0, 0))
    """
    for i in range(len(smokeArea.heightMap)):
        for j in range(len(smokeArea.heightMap[i])):
            print(smokeArea.findLowPointOf(i, j))
    """
    #stdout.write(f"Solution: {sum(smokeArea.findRiskLevels())}\n")
if __name__ == "__main__":
    main()