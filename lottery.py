import random

def lottery():

    number1 = random.randrange(0, 9)
    number2 = random.randrange(0, 9)
    number3 = random.randrange(0, 9)

    num1 = int(input("Enter first number (0-9): "))
    num2 = int(input("Enter second number (0-9): "))
    num3 = int(input("Enter third number (0-9): "))

    print(f"Winning numbers: {number1} {number2} {number3}")

    if num1 == number1 and num2 == number2 and num3 == number3:
        print("Winner!")
    else:
        print("You lose.")

    tryagain = input("Try again? (y or n): ")
    if tryagain == "y":
        lottery()
    else:
        exit()

lottery()