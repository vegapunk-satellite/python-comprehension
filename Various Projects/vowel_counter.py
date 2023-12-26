from math import sqrt

def vowel_counter(string):
    vowel_letters = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
    for letter in string:
        if letter.lower() in vowel_letters:
            vowel_letters[letter.lower()] += 1
    return {k: v for (k, v) in vowel_letters.items() if v > 0}


string = "Californication is a GOOD song"
print(vowel_counter(string))
