# SPLIT

import sys


# Part 1 : Function

def split_from_wish(string_to_cut, delimiters):
    splitted_string = []
    cursor = 0
    for i, char in enumerate(string_to_cut):
        if char in delimiters:
            splitted_string.append(string_to_cut[cursor:i])
            cursor = i + 1
    splitted_string.append(string_to_cut[cursor:])
    return [string for string in splitted_string if string]

# Part 2 : Error Handling

if len(sys.argv) != 2:
    print("erreur")
    exit()


# Part 3 : Slicing

input_string = sys.argv[1]
delimiters = [ " ", "\n"]
input_splitted = split_from_wish(input_string, delimiters)



# Part 4 : Display

for i in input_splitted:
    print(i)
