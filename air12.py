# KING OF SORT

import sys

def quicksort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        left = [x for x in array[1:] if x < pivot]
        right = [x for x in array[1:] if x >= pivot]
        return quicksort(left) + [pivot] + quicksort(right)

if not (len(sys.argv) > 1 and "".join(sys.argv[1:]).replace("+", "").replace("-", "").isdigit()):
    print("erreur")
    sys.exit(1)
 
arr = [int(n) for n in sys.argv[1:]] # Plus efficace de les mettres hors de la fonction bg de Cyril
result = map(str, quicksort(arr))

print(", ".join(result))

