from sys import stdin, stdout
from copy import deepcopy

def main():
    stdout.write("Please enter input filename: \n")
    inputFileName = (str(stdin.readline())).replace("\n", "")
    inputText = (open(inputFileName, "r").read()).split("\n")
    showAtlas = lambda atlas: [print(line) for line in atlas]

    atlas = list(map((lambda line: list(map(int, line))), inputText))
    dijkstra = list(map((lambda line: list(map((lambda char: 1000), line))), atlas))
    oldDijkstra = deepcopy(dijkstra)

    dijkstra[-1][-1] = atlas[-1][-1]

    while oldDijkstra != dijkstra:
        #print("iter")
        oldDijkstra = deepcopy(dijkstra)
        for i in range(len(atlas)-1, -1, -1):
            for j in range(len(atlas[0])-1, -1, -1):
                if i == len(atlas)-1 and j == len(atlas[0])-1:
                    continue
                if i < len(atlas)-1 and j < len(atlas[0])-1 and i > 0 and j > 0:
                    dijkstra[i][j] = min([dijkstra[i+1][j], dijkstra[i][j+1], dijkstra[i-1][j], dijkstra[i][j-1]]) + atlas[i][j]
                elif i == len(atlas)-1:
                    if j == 0:
                        dijkstra[i][j] = min([dijkstra[i][j+1], dijkstra[i-1][j]]) + atlas[i][j] 
                    else:
                        dijkstra[i][j] = min([dijkstra[i][j-1], dijkstra[i][j+1], dijkstra[i-1][j]]) + atlas[i][j]
                elif j == len(atlas[0])-1:
                    if i == 0:
                        dijkstra[i][j] = min([dijkstra[i+1][j], dijkstra[i][j-1]]) + atlas[i][j]
                    else:
                        dijkstra[i][j] = min([dijkstra[i-1][j], dijkstra[i+1][j], dijkstra[i][j-1]]) + atlas[i][j]
                elif i == 0:
                    if j == 0:
                        dijkstra[i][j] = min([dijkstra[i+1][j], dijkstra[i][j+1]]) + atlas[i][j]
                    else:
                        dijkstra[i][j] = min([dijkstra[i][j-1], dijkstra[i+1][j], dijkstra[i][j+1]]) + atlas[i][j]
                elif j == 0:
                    dijkstra[i][j] = min([dijkstra[i-1][j], dijkstra[i][j+1], dijkstra[i+1][j]]) + atlas[i][j]

    #showAtlas(dijkstra)
    stdout.write(f"{dijkstra[0][0] - atlas[0][0]}\n")
if __name__ == "__main__":
    main()