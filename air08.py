# Blend sorted arrays

import sys

def is_sorted(lst):
    return all(lst[i] <= lst[i+1] for i in range(len(lst) - 1))

def sorted_array_blender(array):
    index_fusion = args.index("fusion")
    array1 = array[:index_fusion]
    array2 = array[index_fusion + 1:]
    index1 = index2 = 0
    merged_array = []

    if is_sorted(array1) and is_sorted(array2):
        while index1 < len(array1) and index2 < len(array2):
            if array1[index1] < array2[index2]:
                merged_array.append(array1[index1])
                index1 += 1
            else:
                merged_array.append(array2[index2])
                index2 += 1
        merged_array.extend(array1[index1:])
        merged_array.extend(array2[index2:])
        return ", ".join(map(str, merged_array))
    else:
        print("error : array not sorted")
        sys.exit(1)

args = sys.argv[1:]

if not( "fusion" in args and "".join(args).replace("fusion", "").isdigit() ):
    print("error, enter args in format : -sorted array- fusion -sorted array-")
    sys.exit(1)
else:
    print(sorted_array_blender(args))