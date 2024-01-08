# HEALTH PASS

import sys


# Part 1 : Function

def return_only_approved_one(to_test, approver):
    approved = []
    for i in to_test:
        if approver not in i:
            approved.append(i)
    return approved


# Part 2 : Error Handling

if len(sys.argv) < 3:
    print("erreur")
    exit()


# Part 3 : Slicing

to_test = sys.argv[1:-1]
testor = sys.argv[-1]
final = return_only_approved_one(to_test,testor)


# Part 4 : Display

if final:
    print(", ".join(final))
else:
    print("Nothing to see here buddy")

