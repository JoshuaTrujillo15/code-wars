# input: array[10]
# output: (000) 000-0000

# my solution
def create_phone_number(n):
    return "(" + "".join(str(e) for e in n[:3]) + ") " + "".join(str(e) for e in n[3:6]) + "-" + "".join(str(e) for e in n[6:])

# optimal solution found
def optimal(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)