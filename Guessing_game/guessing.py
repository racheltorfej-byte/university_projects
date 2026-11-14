
import random

def guessing_game():
    secret_number = random.randint(1, 100)
    attempts = 0

    while attempts < 5:
        guess = int(input("Guess a number between 1 and 100: "))

        attempts += 1

        if guess > secret_number:
            print("Enter a smaller number")

        elif guess < secret_number:
            print("Enter a larger number")

        else:
            print("Congratulations! You guessed the number!")
            return

    print("You lost!")
    print("The secret number was:", secret_number)




def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]

    computer_choice = random.choice(choices)
    player_input = input("Choose rock, paper or scissors: ").lower()

    print("Computer chose:", computer_choice)

    if player_input not in choices:
        print("Invalid choice!")

    elif player_input == computer_choice:
        print("It's a tie!")

    elif (player_input == "rock" and computer_choice == "scissors") or \
            (player_input == "paper" and computer_choice == "rock") or \
            (player_input == "scissors" and computer_choice == "paper"):
        print("You win!")

    else:
        print("You lose!")
