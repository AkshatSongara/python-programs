string = input("Enter a string: ")

reverse = ""

for char in string:

    reverse = char + reverse

if(reverse == string):

    print("The given String is palindrome")

else:

    print("The given string is not a palindrome")