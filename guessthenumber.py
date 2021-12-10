import random

final = random.randrange(0,100)

guess = int(input("Guess the number (0-100): "))

while final != guess:
    
    if final > guess:
        print("Greater than")
        guess= int(input("Guess again: "))

    elif final < guess:
        print("Less than")
        guess= int(input("Guess again: "))
else:
    print("You guessed the number!")       
    