import random

def RPSvalue():

 RPSvalue = random.ranint(1,9)
 return RPSvalue

# Infinite loop until broken
while True:
    print("Let's play Rock Paper Scissors!")
    
    # Prompts the user to pick between "rock", "paper" or "scissors"
    choice = input("Choose from Rock, Paper, Scissors: ")
    choice = choice.lower()

    # Picks a random int
    options = [1, 2, 3]
    rngChoice = random.choice(options)
    
    if choice in ('rock', 'paper', 'scissors'):

        # Rock
        if choice == 'rock':
            
            # Defines the outcome of the game based on rngChoice random int
            dict = {
            1: "> I choose Paper! Aw no I lose!",
            2: "> I choose Rock! Welp, it's a tie!",
            3: "> I choose Scissors! I win!",
            }

            # Prints dict (the outcome)
            print(dict[rngChoice])


        # Paper
        if choice == 'paper':
            
            # Defines the outcome of the game based on rngChoice random int            
            dict = {
            1: "> I choose Scissors! Aw no I lose!",
            2: "> I choose Paper! Welp, it's a tie!",
            3: "> I choose Rock! I win!",
            }

            # Prints dict (the outcome)
            print(dict[rngChoice])


        # Scissors
        if choice == 'scissors':

            # Defines the outcome of the game based on rngChoice random int
            dict = {
            1: "> I choose Rock! Aw no I lose!",
            2: "> I choose Scissors! Welp, it's a tie!",
            3: "> I choose Paper! I win!",
            }

            # Prints dict (the outcome)
            print(dict[rngChoice])

        # Prompts the user to play again
        newGame = input("Do you want to play again? (Y/N): ")
        newGame = newGame.lower()
        if newGame == "n":
            break

    #If the user has input an invalid choice, prompts to try again
    else:
        invalidInput = input('Invalid input, do you want to try again? (Y/N): ')
        invalidInput = invalidInput.lower()
        if invalidInput == 'n':
            break