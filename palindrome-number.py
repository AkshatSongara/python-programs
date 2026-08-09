number = int(input("Enter the number : "))

temp = number

reverse = 0

while temp != 0:

    digit = temp % 10

    reverse = reverse * 10 + digit

    temp = temp // 10

if reverse == number:

    print(number,"is an palindrome number")

else:

    print(number, "is not an palindrome number..")