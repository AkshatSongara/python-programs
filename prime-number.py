number = int(input("Enter a Number : "))

if number <= 1:

    print("Not Prime")

else:

    Is_prime = True

    for i in range(2, number):

        if number % i == 0:

            Is_prime = False

            break

    if Is_prime == True:

        print("Prime Number")

    else:

        print("Not Prime Number")