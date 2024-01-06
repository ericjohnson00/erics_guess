import random
import time


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

    number = random.randint(1,100)
    
    while True:
        guess = int(input("Guess a number between 1 and 100 : "))
        
        if guess == number:
            print()
            print("You got it!!!")
            print()
            play_again = input("Would you like to play again? y or n : ")
            if play_again.lower() == "y":
                erics_guess()
            else:
                time.sleep(2)
                print("That was fun!")
                time.sleep(2)
                print("Goodbye")
                break
                
        elif guess < number:
                print("To low, try again")
        else: 
                print("To high, try again")
        
play = input("Would you like to play a game? y or n : ")

if play.lower() == "y":
    erics_guess()
else: 
    print("Goodbye")