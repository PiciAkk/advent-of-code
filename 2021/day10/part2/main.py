from sys import stdin, stdout
from statistics import median

def main():
    stdout.write("Please enter input filename: \n")
    inputFileName = (str(stdin.readline())).replace("\n", "")
    lines = (open(inputFileName, "r").read()).split("\n")
    notCorruptLines = lines.copy()
    score_map = {')': 1, ']': 2, '}': 3, '>': 4}
    invert = {')': '(', ']': '[', '}': '{', '>': '<'}
    invert2 = {'(': ')', '[': ']', '{': '}', '<': '>'}
    result = 0
    for line in lines:
        stack = []
        for character in list(line):
            if character in invert.values():
                stack.append(character)
            else:
                poppedOutItem = stack[-1]
                del stack[-1]
                if invert[character] != poppedOutItem:
                    del notCorruptLines[notCorruptLines.index(line)]
                    result += score_map[character]
                    break
    scores = []
    for line in notCorruptLines:
        score = 0
        stack = []
        for character in list(line):
            if character in invert.values():
                stack.append(character)
            else:
                poppedOutItem = stack[-1]
                del stack[-1]
        stack.reverse()
        for item in stack:
            score = score*5 + score_map[invert2[item]]
        scores.append(score)
    result = median(scores)
    stdout.write(f"Solution: {result}\n")
if __name__ == "__main__":
    main()