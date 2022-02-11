from sys import stdin, stdout

def main():
    stdout.write("Please enter input filename: \n")
    inputFileName = (str(stdin.readline())).replace("\n", "")
    inputText = (open(inputFileName, "r").read()).split("\n")

    sequence = list(map(int, inputText[0])) + [int(inputText[0][0])]
    sumOfMatchingDigits = 0

    for number in range(len(sequence)-1):
        if sequence[number] == sequence[number+1]:
            sumOfMatchingDigits += sequence[number]

    stdout.write(f"{sumOfMatchingDigits}\n")
if __name__ == "__main__":
    main()