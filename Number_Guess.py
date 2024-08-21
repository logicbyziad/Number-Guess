import random
import math

print("Welcome to Number Guessing Game! \n")
print("We will play with integers only \n")

lower_bound = int(input("Enter the lower bound: "))
upper_bound = int(input("Enter the upper bound: "))

answer = random.randint(lower_bound, upper_bound)

chances = math.ceil(math.log2(upper_bound - lower_bound +1))

guess = int(input("Guess the number \n"))

guess_no = 0

while guess_no < chances:

    if (guess < lower_bound) or (guess > upper_bound):

        print(f"Out of bounds pleaase guess within range {lower_bound} to {upper_bound} \n")
        guess = int(input("Guess again: \n"))
        guess_no += 1

    elif guess > answer:
        
        print("Guess was too high ;) \n")
        guess = int(input("Guess again: \n"))
        guess_no += 1
    
    elif guess < answer:
        
        print("Guess was too low ;) \n")
        guess = int(input("Guess again: \n"))
        guess_no += 1

    elif guess == answer:
        
        +guess_no
        did_guess = True
        break


if did_guess is True:

    print(f"You guessed it right in {guess_no} guesses! \nThe maximum guess number was {chances}. \nThe number was {answer}.")

else:

    print(f"You ran out of chances! Better luck next time ^^.")