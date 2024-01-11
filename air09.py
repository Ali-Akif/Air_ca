# LEFT ROTATE

import sys


# Part 1 : Function

def lrotate(array):
    return array[1:] + array[:1]


# Part 2 : Error Handling

if len(sys.argv) < 3:
    print("erreur")
    exit()


# Part 3 : Resolution and Display
    
args = sys.argv[1:]
result = ", ".join(lrotate(args))

print(result)