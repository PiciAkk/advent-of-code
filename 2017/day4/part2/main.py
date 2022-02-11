from sys import stdin, stdout

def doesNotContainAnagrams(passphrase):
    isAnagram = lambda word1, word2: sorted(word1) == sorted(word2)
    for word in range(len(passphrase)):
        for otherWord in range(len(passphrase)):
            if isAnagram(passphrase[word], passphrase[otherWord]) and word != otherWord:
                return False
    return True
def main():
    stdout.write("Please enter input filename: \n")
    inputFileName = (str(stdin.readline())).replace("\n", "")
    inputText = (open(inputFileName, "r").read()).split("\n")

    passphrases = list(map(str.split, inputText))
    validPassphrases = list(filter(doesNotContainAnagrams, passphrases))

    stdout.write(f"{len(validPassphrases)}\n")
if __name__ == "__main__":
    main()