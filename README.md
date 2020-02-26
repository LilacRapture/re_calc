# ReCalc
![test](https://github.com/LilacRapture/ReCalc/workflows/test/badge.svg?branch=master)

Reimagined calculator.
Learning project.

This is an implementation of math expressions calculator.
It uses [Shunting-yard algorithm](https://en.wikipedia.org/wiki/Shunting-yard_algorithm) to convert expression from the infix form to [RPN](https://en.wikipedia.org/wiki/Reverse_Polish_notation). Then it calculates the result using [postfix evaluation](https://en.wikipedia.org/wiki/Reverse_Polish_notation#Postfix_evaluation_algorithm).

# Usage

clone project, go to cloned directory

`$ cd ReCalc`

then

`$ python -m calculator 1+2-(1/6.5)`

or run it without entering project directory

`$ python -m ReCalc 1+2-(1/6.5)`

## TODO
Implement
* unary operators support
