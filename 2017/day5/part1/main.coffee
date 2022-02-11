{readFileSync} = require "fs"
readlineSync = require 'readline-sync'

class message
    constructor: (@instructions) -> @position = 0
    jump: (fromIndex) -> 
        # we can also call this function takeAStep
        @position += @instructions[fromIndex]
        @instructions[fromIndex] += 1
    calcStepsUntilExit: ->
        steps = 0
        while @position < @instructions.length
            steps++
            @jump @position
        return steps

main = -> 
    inputFilename = readlineSync.question "Enter input filename: "
    inputText = readFileSync(inputFilename, "utf8").split("\n")

    jumpInstructions = new message inputText.map Number

    console.log "#{do jumpInstructions.calcStepsUntilExit}"

do main