import json
import os
from art import *
from functools import partial as p
import requests

clear = p(print, "\033[H\033[J")

languages = json.loads(requests.get("https://raw.githubusercontent.com/blakeembrey/language-map/main/languages.json").content)
filteredLanguages = {}
for key, value in languages.items():
    filteredLanguages.update({key: value} if "extensions" in value else {})

def renderLogo():
    clear()
    tprint("AOC", font = "bulbhead") 
    tprint("Search", font = "digital")
    print(r"""
      /\      
     /\*\     
    /\O\*\    
   /*/\/\/\   
  /\O\/\*\/\  
 /\*\/\*\/\/\ 
/\O\/\/*/\/O/\
      ||      
      ||      
      ||      
    """)
    print("\nAdvent Of Code Search is a command-line utility that allows me (and you) to search through my Advent Of Code solutions, files, and folders.\n")

def handleInput(dict, question):
    print(f"{question} ")

    dict[input("> ")]()

def existsYear(year):
    if not os.path.isdir(f"{year}"):
        raise Exception("Year does not exist.")
    return year

def existsDay(year, day):
    if not os.path.isdir(f"{year}/day{day}"):
        raise Exception("Day does not exist.")
    return day

def existsPart(year, day, part):
    if not os.path.isdir(f"{year}/day{day}/part{part}"):
        raise Exception("Part does not exist.")
    return part

getAvailableProgLangs = lambda year, day, part: (
    list(map(
        (lambda filename: 
            list(filter(
                (lambda language: 
                    filteredLanguages[language]["extensions"][0] == os.path.splitext(filename)[1]
                ), 
                filteredLanguages.keys()
            ))[0]
        ),
        os.listdir(f"{year}/day{day}/part{part}")
    ))
)

getFileExtensionFromLanguage = lambda language: languages[language]["extensions"][0]

def progLangSelector(year, day, part):
    availableProgLangs = getAvailableProgLangs(year, day, part)
    for i in range(0, len(availableProgLangs)):
        print(f"{i + 1}: {availableProgLangs[i]}")
    
    return getFileExtensionFromLanguage(availableProgLangs[int(input("> "))-1])

getFilename = lambda year, day, part, fileExtension: (
    list(filter(
        (lambda filename: os.path.splitext(filename)[1] == fileExtension),
        os.listdir(f"{year}/day{day}/part{part}")
    ))[0]
)

def runOrView(year, day, part, filename):
    if input("> ") == "r":
        os.system(f"python3 {year}/day{day}/part{part}/{filename}")
    else:
        os.system(f"pygmentize {year}/day{day}/part{part}/{filename} | less -r ")

renderLogo()

print("Enter year!")
year = existsYear(input("> "))
print("Enter day!")
day = existsDay(year, input("> "))
print("Enter part!")
part = existsPart(year, day, input("> "))
print("Select programming language!")
extension = progLangSelector(year, day, part)
filename = getFilename(year, day, part, extension)
print("Run or view? (r/v)")
runOrView(year, day, part, filename)


# bulbhead or chunky or digital