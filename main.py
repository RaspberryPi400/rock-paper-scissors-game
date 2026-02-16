import sys
import random

bot = "rock"
choice_list = ["rock", "paper", "scissors"]
running = True
while running:
    picking = True
    while picking:
        user = input("Type 'rock', 'paper', or 'scissors': ")

        if user == "rock" and bot == "rock":
            print(f"The computer chose ", bot, ".")
            print("Tie! Go again.")
            bot = random.choice(choice_list)
            replay = input("Would you like to go again ('yes'/'no'): ")
            if replay == "yes":
                break
            elif replay == "no":
                print("Exiting...")
                sys.exit(0)
        elif user == "rock" and bot == "scissors":
            print(f"The computer chose ", bot, ".")
            print("Player wins!")
            if bot == "rock":
                bot = "scissors"
            elif bot == "paper":
                bot = "rock"
            elif bot == "scissors":
                bot = "paper"
            replay = input("Would you like to go again ('yes'/'no'): ")
            if replay == "yes":
                break
            elif replay == "no":
                print("Exiting...")
                sys.exit(0)
        elif user == "rock" and bot == "paper":
            print(f"The computer chose ", bot, ".")
            print("Computer wins!")
            if bot == "rock":
                bot = "paper"
            elif bot == "paper":
                bot = "scissors"
            elif bot == "scissors":
                bot = "rock"
            replay = input("Would you like to go again ('yes'/'no'): ")
            if replay == "yes":
                break
            elif replay == "no":
                print("Exiting...")
                sys.exit(0)
        elif user == "paper" and bot == "rock":
            print(f"The computer chose ", bot, ".")
            print("Player wins!")
            if bot == "rock":
                bot = "scissors"
            elif bot == "paper":
                bot = "rock"
            elif bot == "scissors":
                bot = "paper"
            replay = input("Would you like to go again ('yes'/'no'): ")
            if replay == "yes":
                break
            elif replay == "no":
                print("Exiting...")
                sys.exit(0)
        elif user == "paper" and bot == "paper":
            print(f"The computer chose ", bot, ".")
            print("Tie! Go again.")
            bot = random.choice(choice_list)
            replay = input("Would you like to go again ('yes'/'no'): ")
            if replay == "yes":
                break
            elif replay == "no":
                print("Exiting...")
                sys.exit(0)
        elif user == "paper" and bot == "scissors":
            print(f"The computer chose ", bot, ".")
            print("Computer wins!")
            if bot == "rock":
                bot = "paper"
            elif bot == "paper":
                bot = "scissors"
            elif bot == "scissors":
                bot = "rock"
            replay = input("Would you like to go again ('yes'/'no'): ")
            if replay == "yes":
                break
            elif replay == "no":
                print("Exiting...")
                sys.exit(0)
        elif user == "scissors" and bot == "rock":
            print(f"The computer chose ", bot, ".")
            print("Computer wins!")
            if bot == "rock":
                bot = "paper"
            elif bot == "paper":
                bot = "scissors"
            elif bot == "scissors":
                bot = "rock"
            replay = input("Would you like to go again ('yes'/'no'): ")
            if replay == "yes":
                break
            elif replay == "no":
                print("Exiting...")
                sys.exit(0)
        elif user == "scissors" and bot == "paper":
            print(f"The computer chose ", bot, ".")
            print("Player wins!")
            if bot == "rock":
                bot = "scissors"
            elif bot == "paper":
                bot = "rock"
            elif bot == "scissors":
                bot = "paper"
            replay = input("Would you like to go again ('yes'/'no'): ")
            if replay == "yes":
                break
            elif replay == "no":
                print("Exiting...")
                sys.exit(0)
        elif user == "scissors" and bot == "scissors":
            print(f"The computer chose ", bot, ".")
            print("Tie! Go again.")
            bot = random.choice(choice_list)
            replay = input("Would you like to go again ('yes'/'no'): ")
            if replay == "yes":
                break
            elif replay == "no":
                print("Exiting...")
                sys.exit(0)
        else:
            print("ERROR. Please type 'rock', 'paper', or 'scissors'. Make sure it is lowercase and spelled correctly.")
            break