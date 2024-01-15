# FIND INTRUDER

import sys

def find_intruder(array):
    impostor = []

    for object in array:
        if array.count(object) == 1:
            impostor.append(object)
            
    if impostor:
        if len(impostor) > 1:
            for i, word in enumerate(impostor):
                print(f"{i + 1}: {word}")
        else:
            print(impostor[0])
    else:
        print("not found")

if len(sys.argv) < 4:
    print("error")
    sys.exit(1)

find_intruder(sys.argv[1:])

