"""A wordle recreation."""

__author__ = "730477803"


def contains_char(input_str: str, char: str) -> bool:
    """Checks if input character matches any of the character in the given word input."""
    assert len(char) == 1
    i = 0 
    j = len(input_str) 
    char_in_word = False
    while i < j: 
        if input_str[i] == char:
            char_in_word = True
        i += 1
    if char_in_word:
        return char_in_word
    else: 
        return False


def emojified(guess: str, secret: str) -> str:
    """Appends emojis to a string corresponding to a users guess and whether a character in the guess matches with one in the secret word. Green if exact, yellow if partial (in word somewhere), white if none."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    emoji_string = ""
    exact_match = False
    i = 0
    while i < len(guess):
        if contains_char(secret, guess[i]):
            if secret[i] == guess[i]:
                exact_match = True
            else:
                exact_match = False
            if exact_match:
                emoji_string += GREEN_BOX
            else:
                emoji_string += YELLOW_BOX
        else:
            emoji_string += WHITE_BOX
        i += 1
    return emoji_string


def input_guess(exp_len: int) -> str:
    """Verifies and askes the user to input a word that is the same length as the given parameter."""
    guess = input(f"Enter a {exp_len} character word: ")
    while len(guess) != exp_len:
        guess = input(f"That wasn't {exp_len} chars! Try again: ")
    return guess


def main() -> None:
    """The entrypoint of the program a main game loop."""
    turns = 1
    win = False
    secret_word: str = "codes"
    guess: str = ""
    while turns < 7 and not win:
        print(f"=== Turn {turns}/6 ===")
        guess = input_guess(len(secret_word))
        print(emojified(guess, secret_word))
        if guess == secret_word:
            print(f"You won in {turns}/6 turns!")
            win = True
        turns += 1
    if not win:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()
