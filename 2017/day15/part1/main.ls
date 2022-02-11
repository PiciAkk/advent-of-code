{readFileSync} = require "fs"
readlineSync = require 'readline-sync'
_ = require 'underscore'

class judge
    (generator) -> @pairs = generator.pairs
    check: (pair) ->
        pair.map (el) ->
            /*
            or we can just do this:
            (el .>>>. 0).toString 2
            |> (.slice -16)
            */
            el % 2 ** 16 |> (.>>>. 0) |> (.toString 2)
        |> (.reduce (==))
    countMatches: -> @pairs.filter @check |> (.length)

class generators
    (@startsWith) -> 
    generateNextValue: (generatorFactor, lastValue) -> lastValue * generatorFactor % 2147483647
    generateNextPair: (lastPair) -> 
        [16807, 48271].map ~>
            @generateNextValue &0, lastPair[&1]
    generatePairs: (howMany) ->
        lastPair = @startsWith
        @pairs = Array.from(length: howMany).map (element, index, list) ~>
            if index then lastPair := @generateNextPair lastPair else @startsWith

function main 
    inputFilename = readlineSync.question "Enter input filename: "
    inputText = readFileSync(inputFilename, "utf8").split("\n")

    gens = new generators [0, 1].map (i) -> 
        inputText[i].replace "Generator #{['A', 'B'][i]} starts with ", "" |> Number
    
    gens.generatePairs 40000000

    new judge gens |> (.countMatches!) |> console.log

main!