# Python code to play a game called Rock, Paper, Scissor
import random

flag = True
while flag:
    # user's input for their choice
    user_action = input("Enter a choice (rock, paper, scissors): ")

    # computer's choice
    possible_actions = ["rock", "paper", "scissor"]
    computer_actions = random.choice(possible_actions)

    print(f"\nYou chose {user_action}, computer chose {computer_actions}.\n")

    # determining a winner

    if user_action == computer_actions:
        print(f"Both players selected {user_action}. It's a tie!!!")
    elif user_action == "rock":
        if computer_actions == "scissor":
            print("Rock smashes scissor! You Win!!!")
        else:
            print("Paper covers rock! You lose....")
    elif user_action == "paper":
        if computer_actions == "rock":
            print("Paper covers rock! You win!!!")
        else:
            print("Scissors cuts paper! You lose....")
    elif user_action == "scissor":
        if computer_actions == "paper":
            print("scissors cuts paper! You Win!!!")
        else:
            print("Rock smashes scissor! You lose....")

    play_again = input("Do You want to play again (y/n): ")
    if play_again.lower() != "y":
        flag = False
