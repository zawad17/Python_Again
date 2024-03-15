import random

List = ["rock", "paper", "scissors"]

while True:
    computer_count = 0
    your_count = 0

    your_choice = int(input('''
                GAME START....
                1.Yes
                2.No | Exit
                '''))

    # if you_choice == 1:
    for a in range(0, 5):
            you_choice = int(input('''
                1. Rock
                2. Paper
                3. Scissor
                '''))

            computer_choice = random.choice(List)

            if you_choice == computer_choice:
                print("Draw")
                your_count += 1
                computer_count += 1
            elif (you_choice == 1 and computer_choice == "scissors") or (you_choice == 2 and computer_choice == "rock") or (you_choice == 3 and computer_choice == "paper"):
                print("You win!")
                your_count += 1
            else:
                print("You lose.")
                computer_count += 1

    print("Final Scores:")
    print("Your Score:", your_count)
    print("Computer Score:", computer_count)

    # else:
    #     print("Invalid number")
    #     break


# play_again = input("Play again? (y/n): ")
#            if play_again.lower() != 'y':
#                  break


