"""
The Goal
In this exercise, you have to analyze records of temperature to find the closest to zero.

    Rules
Write a program that prints the temperature closest to 0 among input data.
If two numbers are equally close to zero, positive integer has to be considered
closest to zero (for instance, if the temperatures are -5 and 5, then display 5).

    Game Input
Your program must read the data from the standard input and write the result on the standard output.
Input
Line 1: N, the number of temperatures to analyze
Line 2: A string with the N temperatures expressed as integers ranging from -273 to 5526

Output
Display 0 (zero) if no temperatures are provided. Otherwise, display the temperature closest to 0.
Constraints
0 ≤ N < 10000
Example
Input
5
1 -2 -8 4 5
Output
1
"""
import sys
import math

n = int(input())  # the number of temperatures to analyse
output = float('inf')
for i in input().split():  # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)
    if (abs(output) > abs(t)) or (abs(output) == abs(t) and output < t): output = t

if n == 0: output = 0
print(output)

"""
Validators
The following validators differ from the puzzle test cases to prevent hard coded solutions.
This is why you can have some fails here even if all of the tests provided in the IDE have been successfully passed.
01  Simple data set: {7 5 9 1 4}
02  -273 alone
03  5526 alone
04  Inputs contains only negative numbers: : {-15 -7 -9 -14 -12}
05  When two temperatures are as close to 0, then the positive wins: {15 -7 9 14 7 12}
06  When two temperatures are as close to 0, then the positive wins 2: {15 7 9 14 -7 12}
07  Two negative temperatures that are equal: {-10 -10}
08  The solution displays 0 if no temperature
"""
