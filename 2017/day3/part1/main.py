from copy import deepcopy
from sys import stdin, stdout

class memoryGrid:
    def calcManhattanDistance(point1, point2):
        return abs(point1.position - point2.position)
class memorySquare:
    def __init__(self, location):
        self.location = location
        self.position = self.calcPosition()
    def calcPosition(self):
        # this is the sum of the Cartesisan coordinates of the square
        if self.location == 1: return 0
        corner = 0
        val = 1
        step = 0
        while val < self.location:
            step += 2 if not(corner % 4) else 0
            val += step
            corner += 1
        return int((step / 2) + abs((val - (step / 2)) - self.location))
def main():
    stdout.write("Please enter input number: \n")
    inputNumber = int(stdin.readline())

    manhattanDistance = memoryGrid.calcManhattanDistance(memorySquare(1), memorySquare(inputNumber))

    stdout.write(f"{manhattanDistance}\n")
if __name__ == "__main__":
    main()