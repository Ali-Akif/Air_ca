# READ FILE

import sys


# Part 1 : Error Handling

if len(sys.argv) != 2:
    print("Erreur : veuillez spécifier un fichier à lire.")
    sys.exit(1)


# Part 2 : Smol Slicing
    
filename = sys.argv[1]


# Part 3 : Display

try:
    with open(filename, "r") as file:
        print(file.read())
except FileNotFoundError:
    print("Erreur : Le fichier spécifié n'as pas été trouvé.")
    sys.exit(1)
except PermissionError:
    print("Erreur : Permission refuséee pour ouvrir le fichier.")
    sys.exit(1)