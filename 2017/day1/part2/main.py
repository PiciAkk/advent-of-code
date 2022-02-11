from sys import stdin, stdout

def main():
    stdout.write("Please enter input filename: \n")
    inputFileName = (str(stdin.readline())).replace("\n", "")
    inputText = (open(inputFileName, "r").read()).split("\n")

    sequence = list(map(int, inputText[0]))
    halfway = int(len(sequence)/2)
    extendedSequence = sequence + sequence[0:halfway+1]
    sumOfMatchingDigits = 0

    for number in range(len(sequence)-1):
        if sequence[number] == extendedSequence[number+halfway]:
            sumOfMatchingDigits += sequence[number]

    stdout.write(f"{sumOfMatchingDigits}\n")
if __name__ == "__main__":
    main()