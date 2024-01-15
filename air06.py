# HEALTH PASS

import sys

def whos_not_approved(array):
    not_approved = []
    approver = array.pop()
    to_test = array
    for i in array:
        if approver not in i:
            not_approved.append(i)
    if not_approved:
        return ", ".join(not_approved)
    else:
        return "Nothing to see here buddy"

if len(sys.argv) < 3:
    print("erreur")
    sys.exit(1)

print(whos_not_approved(sys.argv[1:]))
