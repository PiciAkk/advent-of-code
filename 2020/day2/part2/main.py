from sys import stdin, stdout

def main():
    stdout.write("Please enter input filename: \n")
    inputFilename = (str(stdin.readline())).replace("\n", "")
    inputText = (open(inputFilename, "r").read()).split("\n")

    passwordInfos = list(map((lambda passwordInfo: passwordInfo.replace("-", " ").replace(":", "").split()), inputText))
    # I can name this variable corruptedDB too
    isPasswordValid = map(
        (lambda passwordInfo: (passwordInfo[3][int(passwordInfo[0])-1] == passwordInfo[2]) != (passwordInfo[3][int(passwordInfo[1])-1] == passwordInfo[2])),
        passwordInfos
    )
    
    stdout.write(f"{sum(isPasswordValid)}\n")
if __name__ == "__main__": 
    main()