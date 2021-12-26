from sys import stdin, stdout

class dumboOctopuses:
    def __init__(self, inputText):
        self.octopuses = inputText
        self.flashCounter = 0
        self.stepCounter = 0
    def flash(self, i, j):
        if self.didFlash[i][j]:
            return
        self.octopuses[i][j] = 0
        self.didFlash[i][j] = True
        self.flashCounter += 1
        adjacents = []
        if j > 0:
            # balra biztosan léphetünk, mert nem az első oszlopban vagyunk
            adjacents.append([i, j-1])
        if i > 0:
            # fentre biztosan léphetünk, mert nem az első sorban vagyunk
            adjacents.append([i-1, j])
        if i < len(self.octopuses) - 1:
            # lentre biztosan léphetünk, mert nem az utolsó sorban vagyunk
            adjacents.append([i+1, j])
        if j < len(self.octopuses[i]) - 1:
            # jobbra biztosan léphetünk, mert nem az utolsó oszlopban vagyunk
            adjacents.append([i, j+1])
        if j > 0 and i > 0:
            # balra és fentre biztosan léphetünk, mert nem az első oszlopban vagyunk
            adjacents.append([i-1, j-1])
        if j < len(self.octopuses[i])-1 and i > 0:
            # jobbra és fentre biztosan léphetünk, mert nem az első sorban vagyunk
            adjacents.append([i-1, j+1])
        if j > 0 and i < len(self.octopuses) - 1:
            # balra és lentre biztosan léphetünk, mert nem az első oszlopban vagyunk
            adjacents.append([i+1, j-1])
        if j < len(self.octopuses[i])-1 and i < len(self.octopuses) - 1:
            # jobbra és lentre biztosan léphetünk, mert nem az első sorban vagyunk
            adjacents.append([i+1, j+1])
        for adj in adjacents:
            adjI, adjJ = adj[0], adj[1]
            self.octopuses[adjI][adjJ] += 1 if not self.didFlash[adjI][adjJ] else 0
            if self.octopuses[adjI][adjJ] > 9:
                self.flash(adjI, adjJ)
    def takeAStep(self):
        self.stepCounter += 1
        self.didFlash = list(map((lambda line: list(map((lambda char: False), line))), self.octopuses))
        for i in range(len(self.octopuses)):
            for j in range(len(self.octopuses[i])):
                self.octopuses[i][j] += 1 if not self.didFlash[i][j] else 0
                if self.octopuses[i][j] > 9:
                    self.flash(i, j)
    def show(self):
        [print(line) for line in self.octopuses]
def main():
    formatText = lambda inputText: list(map(lambda line: list(map(int, list(line))), inputText))
    stdout.write("Please enter input filename: \n")
    inputFileName = (str(stdin.readline())).replace("\n", "")
    inputText = (open(inputFileName, "r").read()).split("\n")
    octopuses = dumboOctopuses(formatText(inputText))
    #octopuses.show()
    perfectList = list(map((lambda line: list(map((lambda char: 0), line))), octopuses.octopuses))
    while True:
        octopuses.takeAStep()
        #print(octopuses.stepCounter)
        #octopuses.show()
        if octopuses.octopuses == perfectList:
            break
        #print("\n"); octopuses.show(); print(octopuses.flashCounter)
    stdout.write(f"{octopuses.stepCounter}\n")
if __name__ == "__main__":
    main()