# FOR EVERY ONE OF THEM

import sys

def operator_for_everyone(array):
    string_int = [int(n) for n in array[: -1]]
    operator = int(array[-1][1])
    operator_sign = array[-1][0]
    string_len = len(string_int)

    if operator_sign == "+":
        for i in range(string_len):
            string_int[i] += operator
    elif operator_sign == "-":
        for i in range(string_len):
            string_int[i] -= operator

    return ", ".join(map(str, string_int))

if len(sys.argv) < 3 or not "".join(sys.argv[1:]).replace("+", "").replace("-","").isdigit() or len(sys.argv[-1]) != 2:
    print("erreur")
    sys.exit(1)

print(operator_for_everyone(sys.argv[1:]))