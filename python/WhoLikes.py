# if [], "no one likes this"
# if len(arr) > 3 "name, name, and x others like this"
# else "name, name, and name like this

def likes_two_electric_boogaloo(names):
    length = len(names)
    if length < 2:
        who = "no one" if length == 0 else names[0]
        return who + " likes this"
    elif length > 3:
        who = "{}, {} and {} others".format(names[0], names[1], (length - 2))
    else:
        who = "{} and {}".format(names[0], names[1]) if length == 2 else "{}, {} and {}".format(names[0], names[1], names[2])
    return who + " like this"