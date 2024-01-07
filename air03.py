# FIND INTRUDER

import sys


# Part 1 : Error Handling

if len(sys.argv) < 4:
    print("erreur")
    exit()


# Part 2 : Slicing

liste = sys.argv[1:]
impostor = "not found"
print


# Part 3 : Resolution

for object in liste:
    if liste.count(object) == 1:
        impostor = object
    

# Part 4 : Display
    
print(impostor)

