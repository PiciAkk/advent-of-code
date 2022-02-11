{readFileSync} = require "fs"
readlineSync = require 'readline-sync'

class city
    calcManhattanDistance: (a, b) -> Math.abs a.x + b.x - a.y + b.y
class position
    constructor: (@instructions) -> do @calcPosition
    calcDirection: (direction) ->
        if direction > 0 then direction else 360-direction
    calcPosition: ->
        @y = 0
        @x = 0
        direction = 0
        directions = 
            "R": (=> direction = @calcDirection(direction + 90)),
            "L": (=> direction = @calcDirection(direction - 90))

        @instructions.map (instruction) => 
            do directions[instruction[0]]
            step = Number instruction[1..-1]

            switch direction
                when 0 then @x += step
                when 90 then @y += step
                when 180 then @x -= step
                when 270 then @y -= step
                #else throw "Invalid direction"
main = -> 
    inputFilename = await readlineSync.question "Enter input filename: "
    inputText = readFileSync(inputFilename, "utf8").replace("\n", "").split(", ")

    distance = city.calcManhattanDistance {x: 0, y: 0}, new position inputText

    console.log "#{distance}"

do main 