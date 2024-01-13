# META 

import subprocess

def print_colored(text, color):
      colors = {"green": '\033[92m', "red": '\033[91m', "end": '\033[0m'} 
      print(colors[color] + text + colors["end"])

def run_test(file_name, args=[]):
    commande = ["python", file_name] + args
    try:
        subprocess.run(commande, check=True)
        return True
    except subprocess.CalledProcessError:
        return False
    
file_name = "air12.py"
args = ["6", "5", "4", "3", "2", "d"]
test_result = run_test(file_name, args)

if test_result:
     print_colored("Test réussi", "green")
else:
     print_colored("Test échoué", "red")