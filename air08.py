# BLEND SORTED ARRAY

import sys

# Part 1 : Function

def sorted_array_blender(array, array2):
    index = index2 = 0
    new_array = []
    while index < len(array) and index2 < len(array2):
        if array[index] < array2[index2]:
            new_array.append(array[index])
            index += 1
        else:
            new_array.append(array2[index2])
            index2 += 1
    while index < len(array):
        new_array.append(array[index])
        index += 1
    while index2 < len(array2):
        new_array.append(array2[index2])
        index2 += 1
    return new_array


# Part 2 : Error Handling

if len(sys.argv) < 4 and not ("fusion" in sys.argv[1:] and sys.argv[1].isdigit() and sys.argv[-1].isdigit() and sys.argv.count("fusion")) == 1:
    print("erreur")
    exit()


# Part 3 : Slicing
    
terminal_arg = sys.argv[1:]
index_fusion = terminal_arg.index("fusion")
array1 = terminal_arg[:index_fusion]
array2 = terminal_arg[index_fusion + 1:]
result = sorted_array_blender(array1,array2)
result = [str(n) for n in result]


# Part 4 : Display

print(", ".join(result))



