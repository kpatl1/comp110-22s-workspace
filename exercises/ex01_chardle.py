"""EX01: Chardle -- a cute step toward Wordle."""

__author__ = "730477803"


input_word: str = input("Enter a 5 character word: ")
input_letter: str = input("Enter a single character: ")
num_match: int = 0 
word_length: int = len(input_word)

if len(input_word) > 5:
    print("Error: word must contain 5 characters.")
    quit()
if len(input_word) < 5:
    print("Error: word must contain 5 characters.")
    quit()
if len(input_letter) < 1:
    print("Error: Character must be a single character.")
    quit()
if len(input_letter) > 1:
    print("Error: Character must be a single character.")
    quit()

print(f"Searching for {input_letter} in {input_word}")

for i in range(0, word_length):
    if input_word[i] == input_letter:
        print(f"{input_letter} found at index {i}")
        num_match = num_match + 1
if num_match == 0:
    print(f"No instances of {input_letter} found in {input_word}")
elif num_match == 1: 
    print(f"{num_match} instance of {input_letter} found in {input_word}")
elif num_match > 1:
    print(f"{num_match} instances of {input_letter} found in {input_word}")