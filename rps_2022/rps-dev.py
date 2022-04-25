"""
This is a simple game of Rock, Paper, Scissors.  The code is sourced from
https://realpython.com/python-rock-paper-scissors/#what-is-rock-paper-scissors
Modifications have been made to the original; I am not responsible for any errors or vulnerabilities
caused on your system by the modifications.
"""

import random

user_action = input("Enter a choice (rock, paper, scissors): ")
possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)

print(f"\nYou chose {user_action}, computer chose {computer_action}. \n")

if user_action == computer_action:
    print(f"Both players selected {user_action}. It's a tie!")
elif user_action == "rock":
    if computer_action == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif user_action == "paper":
    if computer_action == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif user_action == "scissors":
    if computer_action == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")
