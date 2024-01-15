# READ FILE

import sys

def read_file(filename):
    try:
        with open(filename, "r") as file:
            print(file.read())
    except FileNotFoundError or PermissionError:
        print("Erreur")
        sys.exit(1)

if len(sys.argv) != 2:
    print("Erreur : veuillez spécifier un fichier à lire.")
    sys.exit(1)
  
read_file(sys.argv[1])
