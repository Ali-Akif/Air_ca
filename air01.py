# SPLIT FROM

import sys


# Part 1 : Function

def split_from_arg(string, separateur):
    tableau = []
    index_separateur = string.find(separateur)
    if index_separateur == -1:
        print("string not in string boi")
        sys.exit(1)
    tableau.extend([string[:index_separateur], string[index_separateur + len(separateur):]])
    return [i for i in tableau if i]


# Part 2 : Error Handling

if not len(sys.argv) == 3 or sys.argv[1] == sys.argv[2]:
    print("erreur")
    sys.exit(1)


# Part 3 : Slicing
    
string = sys.argv[1]
separateur = sys.argv[2]
tableau = split_from_arg(string, separateur)


# Part 4 : Display

for i in tableau:
    print(i)
