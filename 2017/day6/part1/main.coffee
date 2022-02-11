{readFileSync} = require "fs"
readlineSync = require 'readline-sync'

class memoryBanks
    constructor: (@banks) -> @seenStates = []
    cycle: -> 
        indexOfBankWithMostBlocks = @banks.indexOf Math.max.apply Math, @banks
        currentBankIndex = indexOfBankWithMostBlocks

        while @banks[indexOfBankWithMostBlocks]
            currentBankIndex = (currentBankIndex) % @banks.length
            @banks[indexOfBankWithMostBlocks] -= 1
            @banks[currentBankIndex] += 1
            currentBankIndex++
    calcStepsUntilSeenState: ->
        steps = 0
        until @banks.join(" ") in @seenStates
            @seenStates.push @banks.join(" ")
            steps++
            do @cycle
        #console.log @seenStates
        steps
main = -> 
    inputFilename = readlineSync.question "Enter input filename: "
    inputText = readFileSync(inputFilename, "utf8").replace("\n", "").split("\t")

    banks = new memoryBanks inputText.map Number

    console.log "#{do banks.calcStepsUntilSeenState}"

do main 