import random #Imports a randomiser module
import time #Imports a module to add a pause

# Infinite loop until broken
while True:

    # Defining inputs for yes or no
    yes = ["y", "yes"]
    no = ["n", "no"]

    print("Let's play Rock Paper Scissors!")
    time.sleep(1)

    # Prompts the user to pick between "rock", "paper" or "scissors"
    choice = input("""\n---CHOICE---
Choose from Rock, Paper or Scissors
>>> """)
    print("------------\n")
    choice = choice.lower()

    #checks if choice is "rock" or "paper" or "scissors"
    if choice in ("rock", "paper", "scissors"):

        possible_actions = ["rock", "paper", "scissors"]
        # Picks a random choice for the computer
        computer_action = random.choice(possible_actions)

        print(f"You chose {choice}, computer chose {computer_action}.")
        time.sleep(0.5)
        print("Calculating...")
        time.sleep(1.5)


        # tie
        if choice == computer_action:
            print("It's a tie!")
        # rock
        elif choice == "rock":
            if computer_action == "scissors":
                print("Rock smashes scissors! You win!")
            else:
                print("Paper covers rock! You lose.")
        # paper
        elif choice == "paper":
            if computer_action == "rock":
                print("Paper covers rock! You win!")
            else:
                print("Scissors cuts paper! You lose.")
        # scissors
        elif choice == "scissors":
            if computer_action == "paper":
                print("Scissors cuts paper! You win!")
            else:
                print("Rock smashes scissors! You lose.")
        time.sleep(2)

        # Prompts the user to play again
        new_game = input("""---CHOICE---
        Do you want to play again? (Y/N): 
        >>> """)
        print("------------")
        new_game = new_game.lower()
        if new_game == "n":
            break

    #If the user has input an invalid choice, prompts to try again
    else:
        yes_no = [yes, no]

        choice = input('''---YES/NO---
Invalid input, do you want to try again? (Y/N)
>>> ''')
        print('------------\n')
        choice = choice.lower()
        if choice in no:
            break
        elif choice in yes:
            pass
        else:
            print("Input not understood, breaking loop.")
            break
           
