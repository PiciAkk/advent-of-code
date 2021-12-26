from sys import stdin, stdout
from copy import deepcopy

def extendImage(inputImage):
    outputImage = inputImage.copy()
    width = len(outputImage[0])
    for counter in [0]*250:
        outputImage.insert(0, [0]*width)
        outputImage.append([0]*width)
    height = len(outputImage)
    for i in range(height):
        for counter in [0]*250:
            outputImage[i].insert(0, 0)
            outputImage[i].append(0)
    return outputImage
def main():
    stdout.write("Please enter input filename: \n")
    inputFileName = (str(stdin.readline())).replace("\n", "")
    inputText = (open(inputFileName, "r").read()).split("\n")

    formatLine = lambda line: list(map(int, line.replace("#", "1").replace(".", "0")))
    showImage = lambda image: [print("".join(map(str, line)).replace("1", "#").replace("0", ".")) for line in image]

    enhancementAlgorithm = formatLine(inputText[0])
    inputImage = extendImage(list(map(formatLine, inputText[2:len(inputText)])))
    #print(inputImage)
    newImage = deepcopy(inputImage)
    """
    newImage = []
    for i in range(len(inputImage)):
        newImage.append()
    """

    #print(enhancementAlgorithm)
    #print("\n\n")
    #showImage(inputImage)

    for counter in range(2):
        for i in range(len(inputImage)):
            line = inputImage[i]
            for j in range(len(line)):
                binaryOfAdjacents = ""
                #print("i:",i)
                #print("j:",j)
                for y in range(i-1, i+2):
                    #print(x)
                    for x in range(j-1, j+2):
                        #print(y)
                        if x >= 0 and y >= 0 and x < len(line) and y < len(inputImage):
                            #print("Adjacent:",inputImage[y][x],y,x)
                            binaryOfAdjacents += str(inputImage[y][x])
                        else:
                            #print("Adjacent: 0",y,x)
                            binaryOfAdjacents += "0"
                        #showImage(inputImage)
                #print(binaryOfAdjacents)
                newImage[i][j] = enhancementAlgorithm[int(binaryOfAdjacents, 2)]
        inputImage = deepcopy(newImage)
        print("Round:",counter)
    #print("\n\n")
    #showImage(newImage)
    counter = 0
    for i in newImage[125:-125]:
        line = i[125:-125]
        counter += line.count(1)
    stdout.write(f"{counter}\n")
if __name__ == "__main__":
    main()