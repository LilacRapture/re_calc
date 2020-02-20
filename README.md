# ReCalc
![Python application](https://github.com/LilacRapture/ReCalc/workflows/Python%20application/badge.svg?branch=master)

Reimagined calculator.
Learning project.

This is an implementation of math expressions calculator.
It uses [Shunting-yard algorithm](https://en.wikipedia.org/wiki/Shunting-yard_algorithm) to convert expression from the infix form to [RPN](https://en.wikipedia.org/wiki/Reverse_Polish_notation). Then it calculates the result using [postfix evaluation](https://en.wikipedia.org/wiki/Reverse_Polish_notation#Postfix_evaluation_algorithm).

# Usage

`python src 1 + 2 - ( 1 / 6.5 )`

In current implementation it's expected that arguments are separated by the space character

## TODO
Implement
* separator independent expression parsing
* functions support
* unary operators support
