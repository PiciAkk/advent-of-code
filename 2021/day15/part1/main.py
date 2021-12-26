from sys import stdin, stdout

def findRiskLevel(risk, x, y, atlas):
    global counter
    if x == len(atlas[0])-1 and y == len(atlas)-1:
        riskLevelOfBestRoute = atlas[y][x] + risk - atlas[0][0]
    else:
        if x < len(atlas[0])-1 and y < len(atlas)-1:
            riskLevelOfBestRoute = atlas[y][x] + min([findRiskLevel(risk, x+1, y, atlas), findRiskLevel(risk, x, y+1, atlas)])
        elif x >= len(atlas[0])-1:
            riskLevelOfBestRoute = atlas[y][x] + findRiskLevel(risk, x, y+1, atlas)
        elif y >= len(atlas)-1:
            riskLevelOfBestRoute = atlas[y][x] + findRiskLevel(risk, x+1, y, atlas)
    return riskLevelOfBestRoute
    
def main():
    stdout.write("Please enter input filename: \n")
    inputFileName = (str(stdin.readline())).replace("\n", "")
    inputText = (open(inputFileName, "r").read()).split("\n")
    showAtlas = lambda atlas: [print(line) for line in atlas]

    atlas = list(map((lambda line: list(map(int, line))), inputText))
    #showAtlas(atlas)
    print(findRiskLevel(0, 0, 0, atlas))
if __name__ == "__main__":
    main()