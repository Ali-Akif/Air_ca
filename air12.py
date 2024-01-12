# KING OF SORT

import sys


# Part 1 : Function

def quicksort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        left = [x for x in array[1:] if x < pivot]
        right = [x for x in array[1:] if x >= pivot]
        return quicksort(left) + [pivot] + quicksort(right)

# Part 2 : Error Handling

if not (len(sys.argv) > 1 and "".join(sys.argv[1:]).replace("+", "").replace("-", "").isdigit()):
    print("erreur")
    exit()


# Part 3 : Slicing
    
arr = [int(n) for n in sys.argv[1:]]
result = map(str, quicksort(arr))
print(", ".join(result))

