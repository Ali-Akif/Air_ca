# ONE AT A TIME

import sys

def delete_repeated_chr(string):
    result = ""

    for char in string:
        if not result or char != result[-1]:
            result += char
            
    return result

if len(sys.argv) != 2:
    print("error")
    sys.exit(1)

print(delete_repeated_chr(sys.argv[1:]))