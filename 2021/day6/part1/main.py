from sys import stdin, stdout

class fishes:
    def __init__(self, fishes):
        self.fishes = fishes
        self.newFish = 8
    def increaseInternalTimer(self):
        for fish in range(len(self.fishes)):
            if self.fishes[fish]-1 < 0:
                self.fishes.append(self.newFish)
                self.fishes[fish] = 6
            else:
                self.fishes[fish] -= 1
    def simulate(self, timeInterval):
        for currentDay in range(timeInterval):
            self.increaseInternalTimer()
def formatInput(inputText):
    return list(map(int, inputText.split(",")))
def main():
    stdout.write("Please enter input filename:\n")
    inputFileName = (str(stdin.readline())).replace("\n", "")
    inputText = formatInput((open(inputFileName, "r")).read())
    lanternFishes = fishes(inputText)
    lanternFishes.simulate(80)
    stdout.write(f"Solution: {len(lanternFishes.fishes)}\n")

if __name__ == "__main__":
    main()