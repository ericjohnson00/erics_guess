import random

print("Created by Eric Johnson 1/4/2024")
print()
print()
print("•○● ericeugene.com ●○•")
print()

def erics_guess():

    number = random.randint(1,100)
    
    while True:
        guess = int(input("Guess a number between 1 and 100 : "))
        
        if guess == number:
            print("You got it!!!")
            play_again = input("Would you like to play again? y or n :")
            if play_again.lower() == "y":
                erics_guess()
            else:
                print("Goodbye")
                break
                
        elif guess < number:
                print("To low, try again")
        else: 
                print("To high, try again")
        
play = input("Would you like to play a game? y or n :")

if play.lower() == "y":
    erics_guess()
else: 
    print("Goodbye")