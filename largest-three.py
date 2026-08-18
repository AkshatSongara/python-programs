num1 = int(input("Enter the 1st number : "))

num2 = int(input("Enter the 2nd number : "))

num3 = int(input("Enter the 3rd number : "))

if num1 == num2 == num3:

    print("All numbers are equal.")

elif (num1 > num2) and (num1 > num3):

    print("1st number is Greater:", num1)

elif (num2 > num3) and (num2 > num1):

    print("2nd number is Greater:", num2)

else:

    print("3rd number is Greater:", num3)