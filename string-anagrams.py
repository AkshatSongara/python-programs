string1 = input("Enter First String : ")

string2 = input("Enter Second String : ")

if len(string1) != len(string2):

    print("Strings are  not anagrams.")

else:

    for ch in string1:

        if string1.count(ch) != string2.count(ch):

            print("Strings are not anagrams.")

            break

    else:

        print("Strings are anagrams.")