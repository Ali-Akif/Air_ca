# FOR EVERY ONE OF THEM

import sys

# Part 1 : Error Handling

if len(sys.argv) < 3 or not "".join(sys.argv[1:]).replace("+", "").replace("-","").isdigit() or len(sys.argv[-1]) != 2:
    print("erreur")
    exit()


# Part 2 : Slicing

operator_sign = sys.argv[-1][0]
operator = int(sys.argv[-1][1])
string_int = [int(n) for n in sys.argv[1: -1]]


# Part 3 : Resolution

if operator_sign == "+":
    for i in range(len(string_int)):
        string_int[i] += operator
elif operator_sign == "-":
    for i in range(len(string_int)):
        string_int[i] += operator
 
string = [str(n) for n in string_int]


# Part 4 : Display

print(", ".join(string))