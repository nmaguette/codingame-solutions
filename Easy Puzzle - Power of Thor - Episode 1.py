"""
    Goal
Your program must allow Thor to reach the light of power.
    Rules
Thor moves on a map which is 40 wide by 18 high. Note that the coordinates (X and Y) start at the top left! This means the most top left cell has the coordinates "X=0,Y=0" and the most bottom right one has the coordinates "X=39,Y=17".

Once the program starts you are given:
the variable lightX: the X position of the light of power that Thor must reach.
the variable lightY: the Y position of the light of power that Thor must reach.
the variable initialTX: the starting X position of Thor.
the variable initialTY: the starting Y position of Thor.
At the end of the game turn, you must output the direction in which you want Thor to go among:

N (North)
NE (North-East)
E (East)
SE (South-East)
S (South)
SW (South-West)
W (West)
NW (North-West)

Each movement makes Thor move by 1 cell in the chosen direction.

Victory Conditions
You win when Thor reaches the light of power

Lose Conditions
Thor moves outside the map

Initial phase
Thor starts on the map at position (3, 6). The light is at position (3, 8).

Round 1
Action S: Thor moves towards south.
New position is (3, 7).

Round 2
Action S: Thor moves towards south.
New position is (3, 8).

    Game Input
The program must first read the initialization data from the standard input, then, in an infinite loop, provides on the
standard output the instructions to move Thor.

Initialization input
Line 1: 4 integers lightX lightY initialTX initialTY. (lightX, lightY) indicates the position of the light.
(initialTX, initialTY) indicates the initial position of Thor.

Input for a game round
Line 1: the number of remaining moves for Thor to reach the light of power: remainingTurns. You can ignore this data
but you must read it.

Output for a game round
A single line providing the move to be made: N NE E SE S SW W ou NW

Constraints
0 ≤ lightX < 40
0 ≤ lightY < 18
0 ≤ initialTX < 40
0 ≤ initialTY < 18
Response time for a game round ≤ 100ms
"""

#--------------------------------Solution distance-------------------------------------------------------
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.
    print("light_x, light_y, initial_tx, initial_ty :", light_x, light_y, initial_tx, initial_ty)
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    distance_x = math.sqrt(abs(light_x ** 2 - initial_tx ** 2))
    distance_y = math.sqrt(abs(light_y ** 2 - initial_ty ** 2))
    print("distance_x & y :", distance_x, distance_y)
    output = ""
    if not (light_y == initial_ty and light_x == initial_tx):
        if light_x == initial_tx:
            output = rstrip("S " * distance_y) if light_y > initial_ty else rstrip("N " * distance_y)
        elif light_y == initial_ty:
            output = rstrip("E " * distance_y) if light_x > initial_tx else rstrip("W " * distance_y)
        else:
            elif light_y > initial_ty and light_x > initial_tx :
        output = rstrip(("SE " * distance_y) + ())

# print("you've done it") if
# A single line providing the move to be made: N NE E SE S SW W or NW
print("remaining_turns :", remaining_turns)
print(output)

#--------------------------------Solution équation de droite-------------------------------------------------------
import sys
import math

light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.
    print("light_x, light_y, initial_tx, initial_ty :", light_x, light_y, initial_tx, initial_ty)
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    # parametres de l'équation de la droite entre l'éclair et Thor
    a = (initial_ty - light_y) / (initial_tx - light_x)
    b = light_y - (a * light_x)
    distance_x = math.sqrt(abs(light_x ** 2 - initial_tx ** 2))
    distance_y = math.sqrt(abs(light_y ** 2 - initial_ty ** 2))
    print("distance_x & y :", distance_x, distance_y)
    output = ""
    if not (light_y == initial_ty and light_x == initial_tx):
        if light_x == initial_tx:
            output = rstrip("S " * distance_y) if light_y > initial_ty else rstrip("N " * distance_y)
        elif light_y == initial_ty:
            output = rstrip("E " * distance_y) if light_x > initial_tx else rstrip("W " * distance_y)
        else:
            elif light_y > initial_ty and light_x > initial_tx:
        output = rstrip(("SE " * distance_y) + ())

# print("you've done it") if
# A single line providing the move to be made: N NE E SE S SW W or NW
print("remaining_turns :", remaining_turns)
print(output)