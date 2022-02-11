from sys import stdin, stdout
from copy import deepcopy

class polymerTemplate:
    def __init__(self, template):
        self.getPairCounts = lambda: self.pairCounts
        self.getLength = lambda: sum(self.countCharacters().values())

        pairs = zip(template[:-1], template[1:])
        self.pairCounts = {}
        self.firstElement = template[0]
        for pair in pairs:
            if "".join(pair) not in self.pairCounts.keys():
                self.pairCounts.update({"".join(pair): 1})
            else:
                self.pairCounts["".join(pair)] += 1
    def doInsertions(self, pairInsertionRules):
        newPairCounts = deepcopy(self.pairCounts)
        for i in self.pairCounts.keys():
            if i in pairInsertionRules.keys() and self.pairCounts[i] > 0:
                newPairs = pairInsertionRules[i]
                newPairCounts[i] -= self.pairCounts[i]
                #print(f"{newPairs[0][1]} -> {i} = {newPairs}")
                #print(f"Destroy {i}")
                for newPair in newPairs:
                    if newPair not in newPairCounts.keys():
                        newPairCounts.update({newPair: self.pairCounts[i]})
                    else:
                        newPairCounts[newPair] += self.pairCounts[i]
        self.pairCounts = newPairCounts
    def doInsertionsNTimes(self, pairInsertionRules, n):
        for _ in [0]*n:
            self.doInsertions(pairInsertionRules)
            #print(self.pairCounts)
    def countCharacters(self):
        characterCounts = {self.firstElement: 1}
        for pair, quantity in self.pairCounts.items():
            if pair[1] not in characterCounts.keys():
                characterCounts.update({pair[1]: quantity})
            else:
                characterCounts[pair[1]] += quantity
        return characterCounts
def main():
    stdout.write("Please enter input filename: \n")
    inputFileName = (str(stdin.readline())).replace("\n", "")
    inputText = (open(inputFileName, "r").read()).split("\n")
    polymerTemplateString = inputText[0]
    polymer = polymerTemplate(polymerTemplateString)
    newRule = lambda adjacents, toInsert: {adjacents: [adjacents[0] + toInsert, toInsert + adjacents[1]]}

    pairInsertionRules = {}
    for rule in map((lambda line: line.split(" -> ")), inputText[2:len(inputText)]):
        pairInsertionRules.update(newRule(rule[0], rule[1]))

    #print(polymer.pairCounts)
    polymer.doInsertionsNTimes(pairInsertionRules, 40)
    #print(polymer.getLength())
    quantities = list(dict(sorted(polymer.countCharacters().items(), key=lambda item: item[1])).values())

    stdout.write(f"Solution: {quantities[-1] - quantities[0]}\n")
if __name__ == "__main__":
    main()