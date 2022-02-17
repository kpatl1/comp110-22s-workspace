
def remove_ws(word: str) -> str:
    """Removes whitespace"""
    newString = ""
    i = 0
    while i < len(word):
        if word[i] != " ":
            newString += word[i]
        i += 1
    return newString
