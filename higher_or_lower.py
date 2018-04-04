#made by Elicia Au Duong 04.April.2018

import random

number = random.randint(1,101)
guess = int(input("I'm thinking of a number. Have a guess: "))
while guess != number:
    if guess > number:
        guess = int(input("Too high! Guess again: "))
    elif guess < number:
        guess = int(input("Too low! Guess again: "))
print("Well done! My number was indeed " + str(number) + ".")