{readFileSync} = require "fs"
readlineSync = require 'readline-sync'
_ = require 'underscore'

class tower
    constructor: (inputText) -> 
        @programs = []
        subTowers = inputText.map (line) -> 
            splittedLine = line.split " -> "
            [
                splittedLine[0].split(" ")[0],
                if splittedLine[1]? then splittedLine[1].split(", ") else []
            ]
        @programs = [_.unzip(subTowers)[0]].concat [_.unzip(subTowers)[1].flat()]
        
    findTheBottomProgram: -> @programs[0].find (program) => program not in @programs[1]
main = -> 
    inputFilename = readlineSync.question "Enter input filename: "
    inputText = readFileSync(inputFilename, "utf8").split("\n")

    towers = new tower inputText

    console.log "#{do towers.findTheBottomProgram}"

do main