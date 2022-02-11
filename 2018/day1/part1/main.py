from sys import stdin, stdout

def main():
    stdout.write("Please enter input filename: \n")
    inputFileName = (str(stdin.readline())).replace("\n", "")
    inputText = (open(inputFileName, "r").read()).split("\n")

    frequencyChanges = list(map(int, inputText))
    resultFrequency = sum(frequencyChanges)

    stdout.write(f"{resultFrequency}\n")
if __name__ == "__main__":
    main()