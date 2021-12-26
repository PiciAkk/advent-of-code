fs = require("fs")
readline = require('readline-sync')

main = -> (
    inputFileName = readline.question("Enter input filename: ")
    inputText = fs.readFileSync(inputFileName).toString().split(/\n/).map((number) -> parseInt(number))
    counter = 0
    for i in [0..inputText.length-1]
        counter += if inputText[i] > inputText[i-1] then 1 else 0
    console.log "Counter: #{counter}"
)
main()