import random
import time

# Display welcome messages with delays
print("•°¿?¿ERIC'S GUESS¿?¿°•")
time.sleep(3)
print()
print("Created by Eric Johnson 1/4/2024")
time.sleep(2)
print()
print("•○● ericeugene.com ●○•")
time.sleep(2)
print()

def erics_guess():

    # Generate a random number for the player to guess
    number = random.randint(1, 100)
    
    while True:
        # Prompt the user to guess the number
        guess = int(input("Guess a number between 1 and 100: "))
        
        if guess == number:
            print()
            print("You got it!!!")
            print()
            # Ask the user if they want to play again
            play_again = input("Would you like to play again? (y or n): ")
            
            if play_again.lower() == "y":
                # If yes, restart the game
                erics_guess()
            else:
                # If no, provide a closing message and end the game
                time.sleep(2)
                print("That was fun!")
                time.sleep(2)
                print("Goodbye")
                break
                
        elif guess < number:
            print("Too low, try again")
        else: 
            print("Too high, try again")

# Start the game if the user wants to play
play = input("Would you like to play a game? (y or n): ")

if play.lower() == "y":
    erics_guess()
else: 
    print("Goodbye")
