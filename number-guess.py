import random 

number = random.randint(1, 100)

guess_counter = 0

print("Number Guessing Game")

print("I have chosen a number from 1 to 100.")

print("You have 10 attempts.")

while guess_counter < 10:

    guess = int(input("Enter a guess: "))

    guess_counter = guess_counter + 1

    if guess < number:

        print("Too low! Try again.")

    elif guess > number:

        print("Too high! Try again.")

    else:

        print("Correct! You guess the number!")

        print("Number of guesses:", guess_counter)

        break

else:

    print("Game Over!")