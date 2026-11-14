from guessing import guessing_game, rock_paper_scissors

while True:

    print("======Game Menu======")
    print("1. Guessing Game")
    print("2. Rock Paper Scissors")

    choice = int(input("Choose a Game: "))

    if choice == 1:
        guessing_game()

    elif choice == 2:
        rock_paper_scissors()

    else:
        print("Invalid choice")
        continue

    play_again = input("Would you like to play again? (yes/no): ").strip().lower()

    if play_again != "yes":
        print("Thanks for playing!")
        break