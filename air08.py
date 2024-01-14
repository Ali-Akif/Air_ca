# BLEND SORTED ARRAY

import sys

# Part 1 : Function

def is_sorted(lst):
    return all(lst[i] <= lst[i+1] for i in range(len(lst) - 1))

def sorted_array_blender(array1, array2):
    index1 = index2 = 0
    merged_array = []
    while index1 < len(array1) and index2 < len(array2):
        if array1[index1] < array2[index2]:
            merged_array.append(array1[index1])
            index1 += 1
        else:
            merged_array.append(array2[index2])
            index2 += 1
    merged_array.extend(array1[index1:])
    merged_array.extend(array2[index2:])
    return merged_array


# Part 2 : Error Handling and Slicing

terminal_arg = sys.argv[1:]

if not( "fusion" in terminal_arg and "".join(terminal_arg).replace("fusion", "").isdigit() ):
    print('error : enter arg in format : "sorted array" fusion "sorted array"')
    sys.exit(1)

index_fusion = terminal_arg.index("fusion")
array1 = terminal_arg[:index_fusion]
array2 = terminal_arg[index_fusion + 1:]

if not (is_sorted(array1) and is_sorted(array2)): #Hard to put it on the same line as the other without using a try except )
    print("error : array not sorted")
    sys.exit(1)


# Part 3 : Resolution and Display

result = sorted_array_blender(array1,array2)
print(", ".join(map(str,result)))