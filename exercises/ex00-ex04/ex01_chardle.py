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

print("Searching for " + input_letter + " in " + input_word)

if input_word[0] == input_letter:
    print(input_letter + " found at index 0")
    num_match = num_match + 1
if input_word[1] == input_letter:
    print(input_letter + " found at index 1")
    num_match = num_match + 1
if input_word[2] == input_letter:
    print(input_letter + " found at index 2")
    num_match = num_match + 1
if input_word[3] == input_letter:
    print(input_letter + " found at index 3")
    num_match = num_match + 1
if input_word[4] == input_letter:
    print(input_letter + " found at index 4")
    num_match = num_match + 1


if num_match == 0:
    print("No instances of " + input_letter + " found in " + input_word)
else:
    if num_match == 1: 
        print(str(num_match) + " instance of " + input_letter + " found in " + input_word)
    else:
        if num_match > 1:
            print(str(num_match) + " instances of " + input_letter + " found in " + input_word)