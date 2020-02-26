def convert_to_tuple(val: str) -> tuple:
    """Convert a string passed to an URL to a tuple"""
    letter = val[0]
    num = val[1:]
    new_val: tuple = tuple()
    if letter == "a":
        new_val = tuple((1, int(num)))
    elif letter == "b":
        new_val = tuple((2, int(num)))
    elif letter == "c":
        new_val = tuple((3, int(num)))
    elif letter == "d":
        new_val = tuple((4, int(num)))
    elif letter == "e":
        new_val = tuple((5, int(num)))
    elif letter == "f":
        new_val = tuple((6, int(num)))
    elif letter == "g":
        new_val = tuple((7, int(num)))
    elif letter == "h":
        new_val = tuple((8, int(num)))
    return new_val


def convert_from_tuple(val: tuple) -> str:
    """Convert a tuple back to a string so it is passed in the user-understandable format to JSON"""
    new_val = ""
    letter = val[0]
    num = val[1]
    if letter == 1:
        new_val = f"a{num}"
    elif letter == 2:
        new_val = f"b{num}"
    elif letter == 3:
        new_val = f"c{num}"
    elif letter == 4:
        new_val = f"d{num}"
    elif letter == 5:
        new_val = f"e{num}"
    elif letter == 6:
        new_val = f"f{num}"
    elif letter == 7:
        new_val = f"g{num}"
    elif letter == 8:
        new_val = f"h{num}"
    return new_val
