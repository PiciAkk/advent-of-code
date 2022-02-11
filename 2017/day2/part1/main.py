from sys import stdin, stdout

def main():
    stdout.write("Please enter input filename: \n")
    inputFileName = (str(stdin.readline())).replace("\n", "")
    inputText = (open(inputFileName, "r").read()).split("\n")

    spreadsheet = list(map((lambda row: list(map(int, row.replace(" ", "\t").split("\t")))), inputText))
    differences = list(map((lambda row: max(row) - min(row)), spreadsheet))

    stdout.write(f"{sum(differences)}\n")
if __name__ == "__main__":
    main()