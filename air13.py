# META 

import subprocess

# Part 1 : Function

def print_colored(text, color):
    colors = {"green": '\033[92m', "red": '\033[91m', "end": '\033[0m'}
    print(colors[color] + text + colors["end"])

def run_test(file_name, args=[]):
    commande = ["python", file_name] + args
    return subprocess.call(commande, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0



# Part 2 : Slicing
    
tests = {
    "air00.py": [["Bonjour les gars"], ["Bonjour les gars"], ["Bonjour", "bonjour"]],
    "air01.py": [["Crevette magique dans la mer des étoiles", "la"], ["55", "5"], ["i"]],
    "air02.py": [["je" "test" "des" "trucs", " "], ["Je" "capte" "quedale", "sa mere"], ["prout"]],
    "air03.py": [["3", "4", "5", "4", "3"], ["bonjour", "monsieur", "bonjour"], ["h"]],   
    "air04.py": [["Hello milady, bien ou quoi ??"], ["pprout"], ["j", "j"]],   
    "air05.py": [["3", "+2"], ["2", "5", "-2"], ["2"]],   
    "air06.py": [["je", "j"], ["je", "l"], ["j"]],   
    "air07.py": [["1", "3", "2"], ["5", "5"], ["b", "j"]],   
    "air08.py": [["10", "fusion", "20"], ["5", "6", "fusion", "2", "8"], ["prout"]],   
    "air09.py": [["Michel", "Albert"], ["Bernard", "Avdul"], ["prout"]],  
    "air10.py": [["air12.py"], ["air00.py"], ["uh"]],   
    "air11.py": [["0", "5"], ["$", "20"], ["uh"]],   
    "air12.py": [["1","2","3","5"], ["5","4","3","2"], ["nuhu"]],   
}
# Every third test will fail

success_count = 0
total_tests = 0


# Part 3 : Resolution and display

for file_name, args_list in tests.items():
    for i, args in enumerate(args_list, start=1):
        test_result = run_test(file_name, args)
        test_status = "success" if test_result else "failure"
        print_colored(f"{file_name[:-3]} ({i}/{len(args_list)}) : {test_status}", "green" if test_result else "red")

        success_count += test_result
        total_tests += 1

print(f"\nTotal success: ({success_count}/{total_tests})\n")
