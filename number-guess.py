import random 

number = random.randint(1, 100)

print("Number Guessing Game")

print("You have chosen a number 1 to 100.")

while True:

    guess = int(input("Enter a guess: "))

    if guess < number:

        print("Too low! Try again.")

    elif guess > number:

        print("Too high! Try again.")

    else:

        print("Correct! You guess the number!")

        break