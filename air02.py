# CONCAT

import sys


# Part 1 : Function

def join_from_wish(array, joiner):

    for i in range(len(array) - 1):
        print(f"{array[i]}{joiner}", end = "")
    print(array[-1])


# Part 2 : Error Handling
    
if len(sys.argv) < 2:
    print("erreur")
    exit()


# Part 3 : Slicing and Resolution
    
terminal_arguments = sys.argv[1:]
last_arg = terminal_arguments.pop(-1)
join_from_wish(terminal_arguments, last_arg)
