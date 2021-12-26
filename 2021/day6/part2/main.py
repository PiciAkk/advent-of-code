from sys import stdin, stdout

class fishes:
    def __init__(self, fishes):
        self.fishes = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for fish in fishes:
            self.fishes[fish] += 1
    def increaseInternalTimer(self):
        fishes2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for fish in range(len(self.fishes)-1, -1, -1):
            if fish == 0:
                fishes2[8] = self.fishes[fish]
                fishes2[6] += self.fishes[fish]
            else:
                fishes2[fish-1] = self.fishes[fish]
        self.fishes = fishes2.copy()
    def simulate(self, timeInterval):
        for currentDay in range(timeInterval):
            self.increaseInternalTimer()
    def __getitem__(self, index):
        return self.fishes[index]
    def __str__(self):
        return(f"Fishes in the ocean: {self.fishes}")
    def __len__(self):
        return sum(self.fishes)
def formatInput(inputText):
    return list(map(int, inputText.split(",")))
def main():
    stdout.write("Please enter input filename:\n")
    inputFileName = (str(stdin.readline())).replace("\n", "")
    inputText = formatInput((open(inputFileName, "r")).read())
    lanternFishes = fishes(inputText)
    lanternFishes.simulate(256)
    stdout.write(f"Solution: {len(lanternFishes)}\n")

if __name__ == "__main__":
    main()