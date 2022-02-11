from sys import stdin, stdout

def main():
    stdout.write("Please enter input filename: \n")
    inputFileName = (str(stdin.readline())).replace("\n", "")
    inputText = (open(inputFileName, "r").read()).split("\n")

    brackets = inputText[0]
    currentFloor = 0
    solution = None
    
    for bracket in range(len(brackets)):
        currentFloor += 1 if brackets[bracket] == "(" else -1
        if currentFloor == -1:
            solution = bracket
            break
    
    stdout.write(f"{solution+1}\n")
if __name__ == "__main__":
    main()