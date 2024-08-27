import random
import math

def getint(x):
    temp = 0

    while True:
        try:
            temp = int(x)
            break

        except ValueError:
            x = input("That's not an integer. Please try again: ")

    return temp

print("Welcome to Number Guessing Game! \n")
print("We will play with integers only \n")

lower_bound = getint(input("Enter the lower bound: "))
upper_bound = getint(input("Enter the upper bound: "))

if (upper_bound < lower_bound):
    upper_bound, lower_bound = lower_bound, upper_bound

answer = random.randint(lower_bound, upper_bound)
chances = math.ceil(math.log2(upper_bound - lower_bound +1))


guess_no = 0
did_guess = False

while guess_no < chances:

    guess = getint(input("Guess the number: "))
    

    if ( (guess < lower_bound) or (guess > upper_bound) ):

        print(f"Out of bounds please guess within range {lower_bound} to {upper_bound} \n")
        #guess = getint(input("Guess again: \n"))

    elif guess > answer:
        
        print("Guess was too high ;) \n")
        #guess = getint(input("Guess again: \n"))
        guess_no += 1
    
    elif guess < answer:
        
        print("Guess was too low ;) \n")
        #guess = getint(input("Guess again: \n"))
        guess_no += 1

    elif guess == answer:
        
        did_guess = True
        guess_no += 1
        break


if did_guess is True:

    print(f"You guessed it right in {guess_no} guesses! \nThe maximum guess number was {chances}. \nThe number was {answer}.")

else:

    print(f"You ran out of chances! Better luck next time ^^.")