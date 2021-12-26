#import sys
from sys import stdin, stdout

def findBinariesWithSpecifiedBitAt(bit, index, inputList):
    outputList = []
    for i in inputList:
        if int(list(i)[index]) == bit:
            outputList.append(i)
    return outputList
def findMostCommon(atIndex, bits):
    return int(bits[atIndex][1] >= bits[atIndex][0])
def findLeastCommon(atIndex, bits):
    return int(not bool(int(bits[atIndex][1] >= bits[atIndex][0])))
def generateBits(inputList):
    bits = []
    for i in range(len(list(inputList[0]))):
        bits.append({1: 0, 0: 0})
    for i in inputList:
        currentLine = list(i)
        # végigiterálunk az input szöveg minden sorának minden számán
        for j in range(len(currentLine)):
            # megnézzük, hogy a `bits` listában létezik-e már j. elem
            bits[j][int(currentLine[j])] += 1
    return bits
def main():
    stdout.write("Please enter input filename: \n")
    inputFileName = (str(stdin.readline())).replace("\n", "")
    inputText = (open(inputFileName, "r").read()).split("\n")
    co2List = inputText.copy(); oxygenList = co2List.copy()
    for i in range(len(list(inputText[0]))):
        co2Bits = generateBits(co2List)
        oxygenBits = generateBits(oxygenList)
        leastCommon = findLeastCommon(i, co2Bits)
        mostCommon = findMostCommon(i, oxygenBits)
        co2List = findBinariesWithSpecificBitAt(leastCommon, i, co2List)
        oxygenList = findBinariesWithSpecifiedBitAt(mostCommon, i, oxygenList)
        if len(oxygenList) == 1:
            break
        if len(co2List) == 1:
            break
    oxygen, co2 = list(map((lambda binary: int(binary, 2)), [oxygenList[0], co2List[0]]))
    stdout.write(f"Solution: {oxygen * co2}\n")
if __name__ == "__main__":
    main()
