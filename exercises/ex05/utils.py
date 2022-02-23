"""A program to work with lists and do various actions to them."""

__author__ = "730477803"


def only_evens(xs: list[int]) -> list[int]:
    """Function that takes an input list of integers and returns a list with only the even numbers from the input."""
    evens: list[int] = list()
    for i in xs: 
        if i % 2 == 0:
            evens.append(i)
    return evens


def sub(x: list[int], start: int, end: int) -> list[int]:
    """Takes an input list, beginning index, end index, and returns a list of the input list only within the range of the input indexes (end not inclusive)."""
    i = start
    j = end 
    subset: list[int] = list()
    if len(x) == 0:
        return subset
    if start >= len(x):
        return subset
    if end <= 0: 
        return subset
    if start < 0: 
        i = 0 
    if end > len(x): 
        j = len(x)
        while i <= j - 1: 
            subset.append(x[i])
            i += 1
    while i < j: 
        subset.append(x[i])
        i += 1
    return subset


def concat(x: list[int], y: list[int]) -> list[int]:
    """Takes two lists and concatenates them."""
    concatlist: list[int] = list()
    for i in x: 
        concatlist.append(i)
    for i in y:
        concatlist.append(i)
    return concatlist