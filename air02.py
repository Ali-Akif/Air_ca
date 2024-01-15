# CONCAT

import sys

def join_from_wish(array):
    joiner = array.pop(-1)
    for i in range(len(array) - 1):
        print(f"{array[i]}{joiner}", end = "")
    print(array[-1])
  
if len(sys.argv) < 2:
    print("erreur")
    sys.exit(1)

join_from_wish(sys.argv[1:])
