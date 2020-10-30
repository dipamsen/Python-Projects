# https://docs.python.org/3/library/random.html
import random

actual_num = random.randint(1, 10)
user_guess = 0

chances = 0

print("Welcome to Number Guessr!")
print("Choose a number from 1 to 10")

# This is an infinite loop
while True:
    # The program runs continuously until one of these happen: (see next comment)
    user_guess = int(input("Enter Your Guess: "))  # Guess number

    if(user_guess < actual_num):
        print("Your guess is too low")

    elif(user_guess > actual_num):
        print("Your guess is too high")

    elif(user_guess == actual_num):
        # (1) : If user got correct number
        print("Congratulations! You got the number!")
        break

    elif(chances == 4):
        # (2) : if chances are over
        print("Oops! You did not get the number " + str(actual_num))
        break

    chances += 1  # each time chance increases
