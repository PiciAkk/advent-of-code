from sys import stdin, stdout

def main():
    stdout.write("Please enter input filename: \n")
    inputFileName = (str(stdin.readline())).replace("\n", "")
    inputText = (open(inputFileName, "r").read()).split("\n")
    horizontalPosition = 0
    depth = 0
    aim = 0
    for i in inputText:
        command = i.split(" ")
        if command[0] == "forward":
            horizontalPosition += int(command[1])
            depth -= aim * int(command[1])
        elif command[0] == "up":
            aim += int(command[1])
        elif command[0] == "down":
            aim -= int(command[1])
    stdout.write(f"\nSolution: {horizontalPosition * depth}\n")
if __name__ == '__main__':
    main()