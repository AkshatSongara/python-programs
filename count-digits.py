number = int(input("Enter a number: "))

number = abs(number)

count_digits = 0

if number == 0:

    count_digits = 1

else:

    while number > 0:

        number = number // 10

        count_digits = count_digits + 1

print("Digits in given number is:", count_digits)