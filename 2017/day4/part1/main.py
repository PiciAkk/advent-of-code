from sys import stdin, stdout

def main():
    stdout.write("Please enter input filename: \n")
    inputFileName = (str(stdin.readline())).replace("\n", "")
    inputText = (open(inputFileName, "r").read()).split("\n")

    passphrases = list(map(str.split, inputText))
    quantitiesOfWordsInPassphrases = list(map((lambda passphrase: list(map(passphrase.count, passphrase))), passphrases))
    validPassphrases = list(filter((lambda passphrase: passphrase == [1]*len(passphrase)), quantitiesOfWordsInPassphrases))

    stdout.write(f"{len(validPassphrases)}\n")
if __name__ == "__main__":
    main()