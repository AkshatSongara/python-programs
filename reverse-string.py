string = input("Enter a string : ")

reverse = " "

for char in string:

    reverse = char + reverse

print("Original String is : ", string)

print("Reverse String is : ", reverse)