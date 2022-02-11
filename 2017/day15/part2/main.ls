{readFileSync} = require "fs"
readlineSync = require 'readline-sync'
_ = require 'underscore'

class judge
    (generator) -> @pairs = generator.pairs
    check: (pair) ->
        pair.map (el) -> 
            el % 2 ** 16 |> (.>>>. 0) |> (.toString 2)
        |> (.reduce (==))
    countMatches: -> @pairs.filter @check |> (.length)

class generator
    (@startsWith, @factor, @multiplesOf) -> 
    generateNextValue: (generatorFactor, lastValue) -> lastValue * generatorFactor % 2147483647
    generateValues: (howMany) ->
        # generatedValues = [@startsWith]
        @values = [@startsWith]
        lastValue = @startsWith
        while @values.length < howMany
            currentValue = @generateNextValue @factor, lastValue
            if not currentValue % @multiplesOf
                @values.push currentValue
            lastValue = currentValue

function main 
    inputFilename = readlineSync.question "Enter input filename: "
    inputText = readFileSync(inputFilename, "utf8").split("\n")

    startsWith = [0, 1].map (i) -> 
        inputText[i].replace "Generator #{['A', 'B'][i]} starts with ", "" |> Number
    
    generatorA = new generator startsWith[0], 16807, 4 

    generatorB = new generator startsWith[1], 48271, 8
    
    pairs = [generatorA, generatorB].map (generator) ->
        generator.generateValues 5#000000
        generator.values
    |> _.zip

    console.log pairs

    #new judge pairs |> (.countMatches!) |> console.log

main!