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
        countOf = (element, arr) -> if not arr.length then arr.length else 
            arr.reduce (acc, curr) ->
                acc + Boolean(curr is element)
        
        steps = 0
        firstSeen = 0
        while countOf(@banks.join(" "), @seenStates) < 2
            @seenStates.push @banks.join(" ")
            firstSeen = if countOf(@banks.join(" "), @seenStates) then steps else firstSeen
            steps++
            do @cycle
        #console.log @seenStates
        steps - firstSeen
main = -> 
    inputFilename = readlineSync.question "Enter input filename: "
    inputText = readFileSync(inputFilename, "utf8").replace("\n", "").split("\t")

    banks = new memoryBanks inputText.map Number

    console.log "#{do banks.calcStepsUntilSeenState}"

do main 