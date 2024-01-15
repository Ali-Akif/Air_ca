# PYRAMID

import sys

def pyramid_printer(character, column):
    spaces = column - 1
    lenght_line = 1

    for i in range(column):
        print(f"{' ' * spaces if i != column - 1 else ''}{character * lenght_line}")
        spaces -= 1
        lenght_line += 2

if not (len(sys.argv) == 3 and len(sys.argv[1]) == 1 and sys.argv[2].isdigit()):
    print("erreur")
    sys.exit(1)

pyramid_printer(sys.argv[1], int(sys.argv[2]))