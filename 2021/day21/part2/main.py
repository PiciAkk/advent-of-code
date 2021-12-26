from sys import stdin, stdout

class player:
    def __init__(self, startingPosition, startingScore):
        self.player = {
            'position': startingPosition,
            'score': startingScore
        }
    def __getitem__(self, key):
        return self.player[key]
    def __setitem__(self, key, value):
        self.player[key] = value
class dice:
    def __init__(self, startingDiceState):
        self.diceState = startingDiceState
        self.rollCounter = 0
    def roll(self):
        self.diceState = ((self.diceState + 1) % 100) if self.diceState + 1 != 100 else 100
        self.rollCounter += 1
        #print(f"Dice state: {self.diceState}")
        return self.diceState
def main():
    stdout.write("Please enter input filename: \n")
    inputFileName = (str(stdin.readline())).replace("\n", "")
    inputText = (open(inputFileName, "r").read()).split("\n")

    players = []
    players.append(player(int(inputText[0].replace("Player 1 starting position: ", "")), 0))
    players.append(player(int(inputText[1].replace("Player 2 starting position: ", "")), 0))

    currentPlayer = 0
    d = dice(0)
    while players[0]["score"] < 1000 and players[1]["score"] < 1000:
        rolled = sum(map((lambda _: d.roll()), [0]*3))
        players[currentPlayer]["position"] = ((players[currentPlayer]["position"] + rolled) % 10) if (players[currentPlayer]["position"] + rolled) % 10 != 0 else 10
        players[currentPlayer]["score"] += players[currentPlayer]["position"]
        #print(f"Player {currentPlayer+1} rolls {rolled} and moves to space {players[currentPlayer]['position']} for a total score of {players[currentPlayer]['score']}.")
        currentPlayer = int(not currentPlayer)
    stdout.write(f"{players[currentPlayer]['score'] * d.rollCounter}\n")
if __name__ == "__main__":
    main()