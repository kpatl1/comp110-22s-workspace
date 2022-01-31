"""One shot wordle exercise"""

__author__ = "730477803"

secret_word = "python"
secret_length: int = len(secret_word)
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

guess_incorrect = True

guess: str = str(input(f"What is your {secret_length}-letter guess? "))


word_index: int = 0 
emoji_result: str = ""
alt_index = 0 
matching_char: str = ""


while secret_length != len(guess):
    guess = input(f"That was not {secret_length} letters! Try again: ")

while word_index < len(guess):
    char_in_word = False
    exact_match = False
    alt_index = 0 
    while alt_index < secret_length:
        if guess[alt_index] == secret_word[word_index]:
            char_in_word = True 
            if alt_index == word_index:
                exact_match = True 
        alt_index += 1
    if char_in_word:
        if exact_match:
            emoji_result += GREEN_BOX
        else:
            emoji_result += YELLOW_BOX
    else:
        emoji_result += WHITE_BOX
    word_index += 1
print(emoji_result)
if guess == secret_word:
    print("Woo! You got it!")
else: 
    print("Not quite. Play again soon!")