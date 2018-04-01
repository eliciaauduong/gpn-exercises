# made by Elicia Au Duong 02.April.2018

import random

print("""
-------------------------------------------------------
Welcome to Human vs. Computer in Scissors, Paper, Rock!
-------------------------------------------------------
Moves: choose scissors, paper or rock by typing in your selection.
Rules: scissors cuts paper, paper covers rock and rock crushes scissors.
Good luck!
------------\n
""")

moves = ["scissors", "paper", "rock"]
counter = 0
win_count = 0
lose_count = 0
tie_count = 0

game_count = int(input("How many games do you want to play? "))

while counter < game_count:
    human_move = input("What is your move? Scissors, paper or rock? ")
    human_move = human_move.lower()
    computer_move = random.choice(moves)
    while human_move not in moves:
        print("Invalid move. Please try again.")
        human_move = input("What is your move? Scissors, paper or rock? ")

    print("human plays: " + human_move)
    print("computer plays: " + computer_move)

    if computer_move == "paper" and human_move == "scissors":
        print("You won the round!")
        win_count = win_count + 1
    elif computer_move == "scissors" and human_move == "rock":
        print("You won the round!")
        win_count = win_count + 1
    elif computer_move == "rock" and human_move == "paper":
        print("You won the round!")
        win_count = win_count + 1
    elif computer_move == "scissors" and human_move == "paper":
        print("You lost the round!")
        lose_count = lose_count + 1
    elif computer_move == "rock" and human_move == "scissors":
        print("You lost the round!")
        lose_count = lose_count + 1
    elif computer_move == "paper" and human_move == "rock":
        print("You lost the round!")
        lose_count = lose_count + 1
    else:
        print("You tied with the computer")
        tie_count = tie_count + 1

    counter = counter + 1
print("Game over!")
print("Human wins: " + str(win_count) + ", computer wins (losses): " + str(lose_count) + " and tied: " + str(tie_count))