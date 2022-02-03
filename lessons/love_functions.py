"""Some examples of tender, loving function definitions."""


def love(name: str) -> str:
    """Givevn a name as a parameter, returns a loving string."""
    return f"I love you {name}!"


def spread_love(to: str, n: int) -> str:
    """Generates a string that repeats a loving message n times."""
    love_note: str = ""
    counter = 0 
    while counter < n:
        love_note += love(to) + "\n"
        counter += 1
    return love_note


def mystery(n: int) -> str:
    """A useless mystery function"""
    i: int = 0
    while i < n:
        if i % 2 == 1:
            return "ooh"
        i += 1
    return "aah"