# Guess a number between 1 and an upper bound.

import random

flag = True
while flag:
    num = input("Type a number for an upper bound: ")

    if num.isdigit():
        print("Let's play!")
        num = int(num)
        flag = False
    else:
        print("Invalid input! Please try again.")

secret = random.randint(1, num)
guess = None
count = 0

while guess != secret:
    guess = input("Please type a number between 1 and " + str(num) + ": ")
    if guess.isdigit():
        guess = int(guess)

    if guess == secret and count == 0:
        print("Amazing! You guessed the number at the first try!")
    elif guess == secret and count >= 1:
        print("Congratulations! It took you " + str(count + 1) + " times to guess the number.")
    else:
        print("Please try again.")
        count += 1


