"""
    The Goal
In stations and airports you often see this type of screen
Have you ever asked yourself how it might be possible to simulate this display on a good old terminal? We have: with ASCII art!

    Rules
ASCII art allows you to represent forms by using characters. To be precise, in our case, these forms are words.
For example, the word "MANHATTAN" could be displayed as follows in ASCII art:
# #  #  ### # #  #  ### ###  #  ###
### # # # # # # # #  #   #  # # # #
### ### # # ### ###  #   #  ### # #
# # # # # # # # # #  #   #  # # # #
# # # # # # # # # #  #   #  # # # #
​Your mission is to write a program that can display a line of text in ASCII art in a style you are given as input.

    Game Input
Input
Line 1: the width L of a letter represented in ASCII art. All letters are the same width.
Line 2: the height H of a letter represented in ASCII art. All letters are the same height.
Line 3: The line of text T, composed of N ASCII characters.
Following lines: the string of characters ABCDEFGHIJKLMNOPQRSTUVWXYZ? Represented in ASCII art.
Output
The text T in ASCII art.
The characters a to z are shown in ASCII art by their equivalent in upper case.
The characters that are not in the intervals [a-z] or [A-Z] will be shown as a question mark in ASCII art.
Constraints
0 < L < 30
0 < H < 30
0 < N < 200
Example 1
Input
4
5
E
 #  ##   ## ##  ### ###  ## # # ###  ## # # #   # # ###  #  ##   #  ##   ## ### # # # # # # # # # # ### ###
# # # # #   # # #   #   #   # #  #    # # # #   ### # # # # # # # # # # #    #  # # # # # # # # # #   #   #
### ##  #   # # ##  ##  # # ###  #    # ##  #   ### # # # # ##  # # ##   #   #  # # # # ###  #   #   #   ##
# # # # #   # # #   #   # # # #  #  # # # # #   # # # # # # #    ## # #   #  #  # # # # ### # #  #  #
# # ##   ## ##  ### #    ## # # ###  #  # # ### # # # #  #  #     # # # ##   #  ###  #  # # # #  #  ###  #
Output
###
#
##
#
###
Example 2
Input
4
5
MANHATTAN
 #  ##   ## ##  ### ###  ## # # ###  ## # # #   # # ###  #  ##   #  ##   ## ### # # # # # # # # # # ### ###
# # # # #   # # #   #   #   # #  #    # # # #   ### # # # # # # # # # # #    #  # # # # # # # # # #   #   #
### ##  #   # # ##  ##  # # ###  #    # ##  #   ### # # # # ##  # # ##   #   #  # # # # ###  #   #   #   ##
# # # # #   # # #   #   # # # #  #  # # # # #   # # # # # # #    ## # #   #  #  # # # # ### # #  #  #
# # ##   ## ##  ### #    ## # # ###  #  # # ### # # # #  #  #     # # # ##   #  ###  #  # # # #  #  ###  #
Output
# #  #  ### # #  #  ### ###  #  ###
### # # # # # # # #  #   #  # # # #
### ### # # ### ###  #   #  ### # #
# # # # # # # # # #  #   #  # # # #
# # # # # # # # # #  #   #  # # # #
"""
# -----------------------------------------------------------------------------------------
import sys
import string

l = int(input())
h = int(input())
text = input()
row = [input() for i in range(h)]
print("text :", text, "\nrow :", row, "\nheight :", h, "\nwidth :", l, file=sys.stderr)
text = text.upper()
alphabet = string.ascii_uppercase
answer = ""
for i in range(h):
    for car in text:
        if car.isalpha():
            # print("alphabet.index(car) & car : ", alphabet.index(car), car)
            start = l*(alphabet.index(car))
            answer += row[i][start:start+l]
        else:
            answer += row[i][l*26:]
    answer += "\n"
print(answer)

"""
Standard Output Stream:
text : MANHATTAN 
row :", row,
height : 11 
 width : 20
 .----------------.  .----------------.  .-----------------. .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .-----------------.
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| | ____    ____ | || |      __      | || | ____  _____  | || |  ____  ____  | || |      __      | || |  _________   | || |  _________   | || |      __      | || | ____  _____  | |
| ||_   \  /   _|| || |     /  \     | || ||_   \|_   _| | || | |_   ||   _| | || |     /  \     | || | |  _   _  |  | || | |  _   _  |  | || |     /  \     | || ||_   \|_   _| | |
| |  |   \/   |  | || |    / /\ \    | || |  |   \ | |   | || |   | |__| |   | || |    / /\ \    | || | |_/ | | \_|  | || | |_/ | | \_|  | || |    / /\ \    | || |  |   \ | |   | |
| |  | |\  /| |  | || |   / ____ \   | || |  | |\ \| |   | || |   |  __  |   | || |   / ____ \   | || |     | |      | || |     | |      | || |   / ____ \   | || |  | |\ \| |   | |
| | _| |_\/_| |_ | || | _/ /    \ \_ | || | _| |_\   |_  | || |  _| |  | |_  | || | _/ /    \ \_ | || |    _| |_     | || |    _| |_     | || | _/ /    \ \_ | || | _| |_\   |_  | |
| ||_____||_____|| || ||____|  |____|| || ||_____|\____| | || | |____||____| | || ||____|  |____|| || |   |_____|    | || |   |_____|    | || ||____|  |____|| || ||_____|\____| | |
| |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
"""

"""
Validators
The following validators differ from the puzzle test cases to prevent hard coded solutions.
This is why you can have some fails here even if all of the tests provided in the IDE have been successfully passed.
01  Test only one letter : G
02  Test HELLOWORLD
03  Test HelloWorld
04  Test AB!!CD
05  Test Lorem ipsum dolor sit amet,...
06  Test full alphabet in CAPS WMADXESFGIJVTHKNOBPLYQRUZC
07  Test HELLO with another ASCII representation
"""