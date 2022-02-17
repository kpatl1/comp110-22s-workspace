def repeat(x: str, y: int) -> str:
    i = 0
    j = 0 
    newString = ""
    while i < len(x):
        while j < y:
            newString += x[i]
            j += 1
        i += 1
        j = 0
    return newString


def indices_on(x: str, y: str):
    i = 0 
    indices = ""
    while i < len(x):
        if x[i] == y:
            indices += str(i)
        i += 1
    return indices