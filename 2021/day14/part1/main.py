from sys import stdin, stdout
import statistics
import collections

def main():
    stdout.write("Please enter input filename: \n")
    inputFileName = (str(stdin.readline())).replace("\n", "")
    inputText = (open(inputFileName, "r").read()).split("\n")
    polymerTemplateString = inputText[0]

    pairInsertionRules = {}
    #map(inputText[2:-1])
    for i in inputText[2:len(inputText)]:
        pairInsertionRules.update({i.split(" -> ")[0]: i.split(" -> ")[1]})
    #print(pairInsertionRules)
    for counter in range(10):
        #print(counter+1)
        polymerTemplate = []
        for i in range(len(polymerTemplateString)-1):
            polymerTemplate.append([polymerTemplateString[i], polymerTemplateString[i + 1]])
        for i in range(len(polymerTemplate)):
            currentPair = "".join(polymerTemplate[i])
            if currentPair in pairInsertionRules.keys():
                polymerTemplate[i].insert(1, pairInsertionRules[currentPair])
                #print(f"Beleraktam {currentPair}-be ezt: {pairInsertionRules[currentPair]}")
        for i in range(len(polymerTemplate)-1):
            polymerTemplate[i].pop()
        polymerTemplateString = "".join(map(lambda currentPair: "".join(currentPair), polymerTemplate))
    #print(polymerTemplateString)
    stdout.write(f"{collections.Counter(polymerTemplateString).most_common()[0][1] - collections.Counter(polymerTemplateString).most_common()[-1][1]}\n")
if __name__ == "__main__":
    main()