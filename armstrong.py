number = int(input("Enter the number : "))

temp = number

total = 0

count = 0

while temp != 0:

    temp = temp // 10

    count = count + 1

temp = number

while temp != 0:

    digit = temp % 10

    total = total + (digit ** count)

    temp = temp // 10

if total == number:

    print(number, "is an armstrong number..")

else:

    print(number, "is not an armstrong number..")