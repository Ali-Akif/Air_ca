# INSERTION IN SORTED ARRAY

import sys


# Part 1 : Function

def insertion_in_sorted_array(int_array, to_add_int):
    result = []
    inserted = False
    for value in int_array:
        if not inserted and to_add_int < value:
            result.append(to_add_int)
            inserted = True
        result.append(str(value))

    if not inserted:
        result.append(to_add_int)
    
    return result


# Part 2 : Error Handling

if len(sys.argv) < 3 and not "".join(sys.argv[1:]).isdigit():
    print("erreur")
    exit()



# Part 3 : Slicing

int_array = [int(value) for value in sys.argv[1:]]
to_add_int = int_array.pop()
final_result = [ str(n) for n in insertion_in_sorted_array(int_array,to_add_int)]


# Part 4 : Display

print(", ".join(final_result))
