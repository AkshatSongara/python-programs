import random

while True:

    guess_counter = 0

    print("Number Guessing Game")

    print("Choose difficulty:")

    print("1. Easy    (1-50)")
    print("2. Medium  (1-100)")
    print("3. Hard    (1-500)")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        number = random.randint(1, 50)
        max_attempts = 15

    elif choice == 2:

        number = random.randint(1, 100)
        max_attempts = 10

    elif choice == 3:

        number = random.randint(1, 500)
        max_attempts = 7

    else:

        print("Invalid Choice!")
        continue
    

    while guess_counter < max_attempts:

        guess = int(input("Enter a guess: "))

        guess_counter = guess_counter + 1

        if guess < number:

            print("Too low! Try again.")

        elif guess > number:

            print("Too high! Try again.")

        else:

            print("Correct! You guessed the number!")

            print("Number of guesses:", guess_counter)

            break

    else:

        print("Game Over!")

        print("The correct number was:", number)


    while True:

        play_again = input("Do you want to play again? (y/n): ").lower()

        if play_again == "n":
            print("Thanks for playing!")
            exit()

        elif play_again == "y":
            break

        else:
            print("Invalid choice. Please enter y or n.")