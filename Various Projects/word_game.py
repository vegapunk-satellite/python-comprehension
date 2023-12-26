from random import randint

secret_word = None
with open("C:/Users/MSI/Desktop/Records/Manga/scripts/words.txt") as file:
    lines = file.read().splitlines()
    secret_word = lines[randint(0, len(lines))]
    print(secret_word)


class SecretCharacter:
    def __init__(self, char):
        self.char = char
        self.found = False


secret_characters = []
for secret_character in secret_word:
    secret_characters.append(SecretCharacter(secret_character))

number_of_turns = 10

while True:
    for secret_character in secret_characters:
        if secret_character.found == True:
            print(secret_character.char, end=" ")
        else:
            secret_character.found == False
            print("_", end=" ")
    print()
    guessed_letter = input("Guess a letter!")
    has_found_any_new_character = False
    has_any_unfound_character = False
    for secret_character in secret_characters:
        if secret_character.found == False:
            if secret_character.char == guessed_letter:
                secret_character.found = True
                has_found_any_new_character = True
            else:
                has_any_unfound_character = True
    if has_any_unfound_character == False:
        print("You have won!")
        break

    if has_found_any_new_character == False:
        number_of_turns -= 1
        if number_of_turns == 0:
            print("You have lost!")
            print(f"Secret word was {secret_word}.")
            break
        else:
            print(f"You have missed {number_of_turns} lives left.")

