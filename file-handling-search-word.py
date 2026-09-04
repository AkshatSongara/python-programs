with open("data.txt", "r") as file:

    data = file.read()

if "Python" in data:
    print("Word is present")

else:
    print("Word is not present")