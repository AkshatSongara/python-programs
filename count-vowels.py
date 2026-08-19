text = input("Enter the string : ")

count = 0

for ch in text:

    if (ch == 'a' or ch == 'A') or (ch == 'e' or ch == 'E') or (ch == 'i' or ch == 'I') or (ch == 'o' or ch == 'O') or (ch == 'u' or ch == 'U') :

        count = count + 1

print("Vowels in string is:", count)