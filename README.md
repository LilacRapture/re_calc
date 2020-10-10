# re_calc
![test](https://github.com/LilacRapture/re_calc/workflows/test/badge.svg?branch=master)
[![Coverage Status](https://coveralls.io/repos/github/LilacRapture/re_calc/badge.svg?branch=master)](https://coveralls.io/github/LilacRapture/re_calc?branch=master)

Reimagined calculator.
Learning project.

This is an implementation of math expressions calculator.
It uses [Shunting-yard algorithm](https://en.wikipedia.org/wiki/Shunting-yard_algorithm) to convert expression from the infix form to [RPN](https://en.wikipedia.org/wiki/Reverse_Polish_notation). Then it calculates the result using [postfix evaluation](https://en.wikipedia.org/wiki/Reverse_Polish_notation#Postfix_evaluation_algorithm).

# Usage

clone project, go to cloned directory

`$ cd re_calc`

then

`$ python -m calculator 1 + 2 - (1 / 6.5) * -5 + 2^3 - (log(9,3) + sqrt(16) + abs(-7))`

or run it without entering project directory

`$ python -m re_calc 1 + 2 - (1 / 6.5) * -5 + 2^3 - (log(9,3) + sqrt(16) + abs(-7))`

### Operations support

`+` - add

`-` - subtract

`*` - multiply

`/` - divide

`^` - power

### Functions support

`log` - logarithm, `log(4, 2)`

`sqrt` - square root

`abs` - absolute value

### Other

Unary signs are also supported. `1 * -5`

## TODO
Implement
* aliases for several functions (e.g. `power`)
