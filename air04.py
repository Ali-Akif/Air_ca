# ONE AT A TIME

import sys

# Part 1 : Error Handling

if len(sys.argv) != 2:
    print("erreur")
    exit()


# Part 2 : Slicing

given_string = sys.argv[1]
result = ""

# Part 3 : Resolution

for i, char in enumerate(given_string):
    if (i == len(given_string) - 1 and char != result[-1]) or char != given_string[i + 1]:
        result += char


# Part 4 : Display
        
print(result)
