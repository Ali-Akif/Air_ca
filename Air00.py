# SPLIT

import sys

def split_from_wish(string_to_cut):
    delimiters = [ " ", "\n"]
    splitted_string = []
    cursor = 0

    for i, char in enumerate(string_to_cut):
        if char in delimiters:
            splitted_string.append(string_to_cut[cursor:i])
            cursor = i + 1
    splitted_string.append(string_to_cut[cursor:])
    
    return [string for string in splitted_string if string]

if len(sys.argv) != 2:
    print("error")
    sys.exit(1)

for i in split_from_wish(sys.argv[1]):
    print(i)
