from sys import stdin, stdout

def main():
    stdout.write("Please enter input filename: \n")
    inputFileName = (str(stdin.readline())).replace("\n", "")
    inputText = (open(inputFileName, "r").read()).split("\n")
    inputText = list(map(int, inputText))
    counter = 0
    windows = []
    for i in range(len(inputText)):
        if i+2 <= len(inputText)-1:
            # létre tudunk hozni a mostani számból kiindulva egy hármas ablakot
            windows.append(inputText[i]+inputText[i+1]+inputText[i+2])
            # létrehozzuk a hármas ablakot, és az összegüket belerajuk a windows listába
            if i > 0:
                # megnézzük, hogy nem az első ablaknál járunk-e
                if windows[i] > windows[i-1]:
                    # ha nem, akkor megnézzük, hogy a mostani ablak összege nagyobb-e az előző ablakénál
                    counter += 1
                    # ha igen, akkor hozzáadunk egyet a counterhez
    stdout.write(f"\nCounter: {counter}\n")
    # kiírjuk a countert
if __name__ == '__main__':
    main()