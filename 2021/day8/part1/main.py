from sys import stdin, stdout
import collections

def main():
    stdout.write("Please enter input filename: \n")
    inputFileName = (str(stdin.readline())).replace("\n", "")
    inputText = (open(inputFileName, "r").read()).split("\n")
    flatten = lambda t: [item for sublist in t for item in sublist]

    segmentPatterns = list(map((lambda line: list(map((lambda part: list(map((lambda number: [number, len(number)]), part.split(" ")))), line.split(" | ")))), inputText))

    segmentsOfNumbers = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    easySegments = list(map((lambda segment: segment[0]), filter((lambda segment: segment[1] == 1), collections.Counter(segmentsOfNumbers).most_common())))
    easyDigits = list(filter((lambda i: segmentsOfNumbers[i] in easySegments), range(len(segmentsOfNumbers))))

    solution = len(list(map((lambda outputValue: outputValue[1]), filter((lambda outputValue: outputValue[1] in easySegments), flatten(map((lambda line: line[1]), segmentPatterns))))))

    stdout.write(f"Solution: {solution}\n")
if __name__ == "__main__":
    main()