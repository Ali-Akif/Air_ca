# PYRAMID

import sys


# Part 1 : Error Handling

if not (len(sys.argv) == 3 and len(sys.argv[1]) == 1 and sys.argv[2].isdigit()):
    print("erreur")
    sys.exit(1)


# Part 2 : Slicing

args = sys.argv[1:]
car, column = args[0], int(args[1])
spaces = column - 1
lenght_line = 1


# Part 3 : Resolution and display

for i in range(1, column + 1):
    print(f"{'' if i == column else ' ' * spaces}{car * lenght_line}")
    spaces -= 1
    lenght_line += 2
