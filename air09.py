# LEFT ROTATE

import sys

def lrotate(array):
    return ", ".join(array[1:] + array[:1])

if len(sys.argv) < 3:
    print("erreur")
    sys.exit(1)

print(lrotate(sys.argv[1:]))