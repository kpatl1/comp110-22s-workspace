"""A program made to work and learn with dictionaries."""

__author__ = "730477803"


def invert(x: dict[str, str]) -> dict[str, str]:
    """Inverts a given dictionary."""
    newDict: dict[str, str] = {}
    for key in x:
        newDict[x[key]] = key 
    if len(x) != len(newDict):
        raise KeyError
    return newDict


def favorite_color(x: dict[str, str]) -> str:
    """Returns the most favorite color given a dictionary with name as key and color as value."""
    colors: dict["str", int] = dict()
    x_keys: list[str] = []
    maxColor: str = ""
    i = 0 
    for key in x:
        x_keys.append(key)
        colors[x[key]] = 0  

    for key in colors:
        j = 0
        while j < len(x):
            if key == x[x_keys[j]]:
                colors[key] += 1
            j += 1
    
    for key in colors:
        if colors[key] > i:
            i = colors[key]
            maxColor = key

    return maxColor


def count(x: list[str]) -> dict[str, int]:
    """Returns count of given items in a list."""
    newDict: dict[str, int] = {}
    for item in x: 
        if item in newDict:
            newDict[item] += 1
        else:
            newDict[item] = 1 
    return newDict