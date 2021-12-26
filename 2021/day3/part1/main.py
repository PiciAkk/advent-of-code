from sys import stdin, stdout
import solutionFinder

def main():
    stdout.write("Please enter input filename: \n")
    inputFileName = (str(stdin.readline())).replace("\n", "")
    inputText = (open(inputFileName, "r").read()).split("\n")
    gammaRate, epsilonRate = solutionFinder.solutionFinder(inputText)
    stdout.write(f"Solution: {int(gammaRate, 2) * int(epsilonRate, 2)}\n")
if __name__ == "__main__":
    main()