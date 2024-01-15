# SPLIT FROM

import sys

def split_from_arg(string, separateur):
    tableau = []
    index_separateur = string.find(separateur)

    if index_separateur == -1:
        print("string not in string boi")
        sys.exit(1)
    tableau.extend([string[:index_separateur], string[index_separateur + len(separateur):]])

    return [i for i in tableau if i]

if not len(sys.argv) == 3 or sys.argv[1] == sys.argv[2]:
    print("error")
    sys.exit(1)

for i in split_from_arg(sys.argv[1], sys.argv[2]):
    print(i)
