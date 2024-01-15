# INSERTION IN SORTED ARRAY

import sys

def insertion_in_sorted_array(array):
    array = [int(value) for value in array]
    to_add = array.pop()
    result = []
    inserted = False
    for value in array:
        if not inserted and to_add < value:
            result.append(to_add)
            inserted = True
        result.append(value)
    if not inserted:
        result.append(to_add)
    return ", ".join([str(n) for n in result])

if len(sys.argv) < 3 or not "".join(sys.argv[1:]).isdigit():
    print("erreur")
    sys.exit(1)

print(insertion_in_sorted_array(sys.argv[1:]))
