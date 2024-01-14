# ONE AT A TIME

import sys

# Part 1 : Error Handling

if len(sys.argv) != 2:
    print("erreur")
    sys.exit(1)


# Part 2 : Slicing

given_string = sys.argv[1]
result = ""

# Part 3 : Resolution

for char in given_string:
    if not result or char != result[-1]:
        result += char


# Part 4 : Display
        
print(result)
