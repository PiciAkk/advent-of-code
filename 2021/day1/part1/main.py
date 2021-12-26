from sys import stdin, stdout

def main():
    stdout.write("Please enter input filename: \n")
    inputFileName = (str(stdin.readline())).replace("\n", "")
    inputText = (open(inputFileName, "r").read()).split("\n")
    counter = 0
    for i in range(1, len(inputText)):
        previousValue = int(inputText[i-1])
        currentValue = int(inputText[i])
        if currentValue > previousValue:
            counter += 1 # depth measurement increases, so we add 1 to the counter
    stdout.write(f"\nCounter: {counter}\n")
if __name__ == '__main__':
    main()