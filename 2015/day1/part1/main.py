from sys import stdin, stdout

def main():
    stdout.write("Please enter input filename: \n")
    inputFileName = (str(stdin.readline())).replace("\n", "")
    inputText = (open(inputFileName, "r").read()).split("\n")

    brackets = inputText[0]

    floor = sum(map((lambda bracket: 1 if bracket == "(" else -1), brackets))

    stdout.write(f"{floor}\n")
if __name__ == "__main__":
    main()