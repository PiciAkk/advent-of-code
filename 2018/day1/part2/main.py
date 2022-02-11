import itertools
from sys import stdin, stdout

def main():
    stdout.write("Please enter input filename: \n")
    inputFileName = (str(stdin.readline())).replace("\n", "")
    inputText = (open(inputFileName, "r").read()).split("\n")

    frequencyChanges = list(map(int, inputText))
    frequency = 0
    firstFrequencyThatIsReachedTwice = None
    alreadyReachedFrequencies = []

    for frequencyChange in itertools.cycle(frequencyChanges):
        frequency += frequencyChange
        if frequency in alreadyReachedFrequencies:
            firstFrequencyThatIsReachedTwice = frequency
            break
        alreadyReachedFrequencies.append(frequency)

    stdout.write(f"{firstFrequencyThatIsReachedTwice}\n")
if __name__ == "__main__":
    main()