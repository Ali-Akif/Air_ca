# FIND INTRUDER

import sys


# Part 1 : Error Handling

if len(sys.argv) < 4:
    print("erreur")
    sys.exit(1)


# Part 2 : Slicing

liste = sys.argv[1:]
impostor = []


# Part 3 : Resolution

for object in liste:
    if liste.count(object) == 1:
        impostor.append(object)
    

# Part 4 : Display
    
if impostor:
    if len(impostor) > 1:
        for i, word in enumerate(impostor):
            print(f"{i + 1}: {word}")
    else:
        print(impostor[0])
else:
    print("not found")

