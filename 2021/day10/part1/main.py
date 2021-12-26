from sys import stdin, stdout

def main():
    stdout.write("Please enter input filename: \n")
    inputFileName = (str(stdin.readline())).replace("\n", "")
    lines = (open(inputFileName, "r").read()).split("\n")
    score_map = {')': 3, ']': 57, '}': 1197, '>': 25137}
    invert = {')': '(', ']': '[', '}': '{', '>': '<'}
    result = 0
    for l in lines:
        stack = []
        for c in list(l):
            if c in invert.values():
                stack.append(c)
            else:
                poppedOutItem = stack[-1]
                del stack[-1]
                if invert[c] != poppedOutItem:
                    result += score_map[c]
                    break
    stdout.write(f"Solution: {result}\n")
if __name__ == "__main__":
    main()