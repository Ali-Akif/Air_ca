# SPLIT

import sys


# Part 1 : Function

def split_from_wish(string_to_cut, string_splitter):
    splitter_indice = [i for i, char in enumerate(string_to_cut) if char in string_splitter]
    splitted_string = []
    cursor = 0
    for i in splitter_indice:
        splitted_string.append(string_to_cut[cursor:i])
        cursor = i + 1
    splitted_string.append(string_to_cut[cursor:])
    return [string for string in splitted_string if string]

# Part 2 : Error Handling

if len(sys.argv) != 2:
    print("erreur")
    exit()


# Part 3 : Slicing

arg = sys.argv[1]
splitt = [ " ", "\n"]
string_in_array = split_from_wish(arg, splitt)



# Part 4 : Display

for i in string_in_array:
    print(i)
