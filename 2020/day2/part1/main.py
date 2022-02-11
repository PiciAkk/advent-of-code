from sys import stdin, stdout

def main():
    stdout.write("Please enter input filename: \n")
    inputFilename = (str(stdin.readline())).replace("\n", "")
    inputText = (open(inputFilename, "r").read()).split("\n")

    passwordInfos = list(map((lambda passwordInfo: passwordInfo.replace("-", " ").replace(":", "").split()), inputText))
    # I can name this variable corruptedDB too
    isPasswordValid = map(
        (lambda passwordInfo: passwordInfo[3].count(passwordInfo[2]) >= int(passwordInfo[0]) and passwordInfo[3].count(passwordInfo[2]) <= int(passwordInfo[1])),
        passwordInfos
    )
    
    stdout.write(f"{sum(isPasswordValid)}\n")
if __name__ == "__main__": 
    main()