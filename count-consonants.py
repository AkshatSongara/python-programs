text = input("Enter the string : ")

count = 0

for ch in text:

    if (ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z'):

        if (ch != 'a' and ch != 'A') and (ch != 'e' and ch != 'E') and (ch != 'i' and ch != 'I') and (ch != 'o' and ch != 'O') and (ch != 'u' and ch != 'U'):

            count = count + 1

print("Consonents in string is:", count)