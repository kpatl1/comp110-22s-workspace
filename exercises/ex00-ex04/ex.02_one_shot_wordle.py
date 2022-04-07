"""One shot wordle exercise"""

__author__ = "730477803"

secret_word = "python"
secret_length: int = len(secret_word)
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
guess_incorrect = True
word_index: int = 0 
emoji_result: str = ""
alt_index = 0 
matching_char: str = ""

guess: str = str(input(f"What is your {secret_length}-letter guess? "))

# Makes sure guess is matching length to the secret word. 
while secret_length != len(guess):
    guess = input(f"That was not {secret_length} letters! Try again: ")

while word_index < len(guess):
    # Initialization of boolean operators to allow for proper iteration.
    char_in_word = False
    exact_match = False
    alt_index = 0 
    while alt_index < secret_length:
        if secret_word[alt_index] == guess[word_index]:
            # Checks each letter in guess and verifies if it matches an index of the secret word. 
            char_in_word = True 
            if alt_index == word_index:
                # Allows for green box because it checks if the index of the matching characters are the same. 
                exact_match = True 
        # Iterating the alternate index to check the next letter of the guess with the same character of the secret 
        alt_index += 1
    if char_in_word:
        # If there was a match of characters, a green box will be appended if alt_index and word_index match. If not, then yellow. If not either, then white.
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